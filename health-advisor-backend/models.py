"""
Pydantic models for request/response validation
"""
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class PatientInfo(BaseModel):
    """Patient information input model"""
    patient_data: str = Field(
        ...,
        description="Patient information text",
        min_length=10,
        max_length=5000
    )
    patient_name: Optional[str] = Field(None, description="Optional patient name")
    
    class Config:
        json_schema_extra = {
            "example": {
                "patient_name": "John Doe",
                "patient_data": "Age: 35, Weight: 85kg, Height: 180cm, Exercise: 2 times/week, Diet: Mixed, Sleep: 6 hours"
            }
        }


class HealthSummary(BaseModel):
    """Health summary model"""
    summary: str = Field(..., description="Brief health overview")


class HealthyHabits(BaseModel):
    """Healthy habits model"""
    habits: List[str] = Field(..., description="List of healthy habits identified")


class UnhealthyHabits(BaseModel):
    """Unhealthy habits model"""
    habits: List[str] = Field(..., description="List of unhealthy habits to address")


class Recommendations(BaseModel):
    """Recommendations model"""
    recommendations: List[str] = Field(..., description="List of health recommendations")
    disclaimer: str = Field(..., description="Medical disclaimer")


class HealthAnalysisResponse(BaseModel):
    """Complete health analysis response model"""
    summary: str = Field(..., description="Health summary")
    healthy_habits: List[str] = Field(..., description="List of healthy habits")
    unhealthy_habits: List[str] = Field(..., description="List of unhealthy habits")
    recommendations: List[str] = Field(..., description="List of recommendations")
    disclaimer: str = Field(..., description="Medical disclaimer")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Analysis timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "summary": "Patient appears to be in moderate health with some areas needing attention.",
                "healthy_habits": ["Exercises regularly", "Maintains balanced diet"],
                "unhealthy_habits": ["Gets only 6 hours of sleep", "High stress levels"],
                "recommendations": ["Increase sleep to 7-8 hours", "Reduce stress through meditation"],
                "disclaimer": "This analysis is for informational purposes only...",
                "timestamp": "2024-01-15T10:30:00"
            }
        }


class ErrorResponse(BaseModel):
    """Error response model"""
    detail: str = Field(..., description="Error message")
    status_code: int = Field(..., description="HTTP status code")


class HealthAnalysisRequest(BaseModel):
    """Request model for comprehensive health analysis"""
    patient_data: str = Field(
        ...,
        description="Complete patient information",
        min_length=10,
        max_length=5000
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "patient_data": "Patient: Jane Doe, Age: 28, Weight: 65kg, Height: 168cm, Exercises: 4 times/week, Sleep: 8 hours, Diet: Vegetarian, Stress: Moderate, Allergies: None"
            }
        }
