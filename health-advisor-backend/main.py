"""
Health Advisor AI Backend - FastAPI Application
Professional healthcare AI system with LLM integration
"""
import logging
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import uvicorn

from config import (
    API_TITLE,
    API_VERSION,
    API_DESCRIPTION,
    API_HOST,
    API_PORT,
    CORS_ORIGINS,
    CORS_CREDENTIALS,
    CORS_METHODS,
    CORS_HEADERS,
    LOG_LEVEL
)
from models import (
    HealthAnalysisRequest,
    HealthAnalysisResponse,
    ErrorResponse
)
from services import HealthAnalysisService

# Configure logging
logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global service instance
health_service: HealthAnalysisService = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan"""
    # Startup
    global health_service
    try:
        logger.info("Initializing Health Advisor AI Backend...")
        health_service = HealthAnalysisService()
        logger.info("✓ Health Advisor AI Backend initialized successfully")
    except Exception as e:
        logger.error(f"✗ Failed to initialize backend: {str(e)}")
        raise
    
    yield
    
    # Shutdown
    logger.info("Shutting down Health Advisor AI Backend...")


# Create FastAPI app
app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    description=API_DESCRIPTION,
    lifespan=lifespan,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=CORS_CREDENTIALS,
    allow_methods=CORS_METHODS,
    allow_headers=CORS_HEADERS,
)


# ============================================================================
# Health Check Endpoints
# ============================================================================

@app.get("/", tags=["Health"])
async def root():
    """Root endpoint"""
    return {
        "message": "Health Advisor AI Backend",
        "version": API_VERSION,
        "status": "running"
    }


@app.get("/api/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Health Advisor AI",
        "version": API_VERSION
    }


# ============================================================================
# Analysis Endpoints
# ============================================================================

@app.post(
    "/api/analyze",
    response_model=HealthAnalysisResponse,
    status_code=status.HTTP_200_OK,
    tags=["Analysis"],
    summary="Analyze patient health information",
    description="Provide patient information for comprehensive health analysis"
)
async def analyze_health(request: HealthAnalysisRequest):
    """
    Analyze patient health information and provide recommendations
    
    **Request Body:**
    - `patient_data`: Patient information as text (min 10, max 5000 characters)
    
    **Returns:**
    - Health summary
    - List of healthy habits
    - List of unhealthy habits
    - Recommendations for improvement
    - Medical disclaimer
    """
    try:
        if not request.patient_data or len(request.patient_data.strip()) < 10:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Patient data must be at least 10 characters long"
            )
        
        logger.info("Processing health analysis request...")
        
        # Perform analysis
        analysis_result = health_service.analyze_patient_health(
            request.patient_data
        )
        
        # Convert to response model
        response = HealthAnalysisResponse(
            summary=analysis_result['summary'],
            healthy_habits=analysis_result['healthy_habits'],
            unhealthy_habits=analysis_result['unhealthy_habits'],
            recommendations=analysis_result['recommendations'],
            disclaimer=analysis_result['disclaimer']
        )
        
        logger.info("✓ Health analysis completed successfully")
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"✗ Error during analysis: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during health analysis. Please try again."
        )


# ============================================================================
# Error Handlers
# ============================================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail,
            "status_code": exc.status_code
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Handle general exceptions"""
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "Internal server error",
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
        }
    )


# ============================================================================
# Startup and Run
# ============================================================================

if __name__ == "__main__":
    logger.info(f"Starting Health Advisor AI Backend on {API_HOST}:{API_PORT}")
    
    uvicorn.run(
        app,
        host=API_HOST,
        port=API_PORT,
        log_level=LOG_LEVEL.lower()
    )
