"""
Configuration settings for Health Advisor AI Backend
"""
import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8000))
API_TITLE = "Health Advisor AI API"
API_VERSION = "1.0.0"
API_DESCRIPTION = "Professional Health Advisor AI System powered by LLM"

# CORS Configuration
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
]
CORS_CREDENTIALS = True
CORS_METHODS = ["*"]
CORS_HEADERS = ["*"]

# LLM Configuration
LLM_MODEL = os.getenv("LLM_MODEL", "qwen2:7b")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", 0.5))
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", 2048))

# Health Analysis Configuration
HEALTH_ANALYSIS_PROMPT_TEMPLATE = """
You are a professional Health Advisor AI assistant with expertise in preventive medicine and wellness.

Patient Information:
{patient_data}

Based on the above patient information, provide a comprehensive health analysis with the following structure:

1. **Health Summary**: Brief overview of the patient's current health status (2-3 sentences)

2. **Healthy Habits**: List the positive health practices identified
   - Use bullet points
   - Be specific and encouraging

3. **Areas for Improvement**: Identify unhealthy habits or risk factors
   - Use bullet points
   - Be constructive and non-judgmental

4. **Recommendations**: Practical suggestions for improvement
   - Include lifestyle changes
   - Mention preventive measures
   - Suggest when to consult a healthcare provider

5. **Important Disclaimer**: Include a medical disclaimer

Please provide professional, evidence-based advice while being empathetic and supportive.
"""

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
