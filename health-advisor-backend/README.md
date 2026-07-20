# Health Advisor AI - Backend

Professional Healthcare AI System Backend powered by FastAPI and LangChain

## 🏥 Features

- **Professional Health Analysis**: Comprehensive patient health assessment
- **AI-Powered Insights**: LLM-based analysis using Ollama
- **Structured Output**: Organized health recommendations
- **Medical Disclaimer**: Automated compliance warnings
- **RESTful API**: Easy integration with frontend
- **CORS Enabled**: Cross-origin support
- **Production Ready**: Proper error handling and logging

## 🛠️ Prerequisites

- Python 3.9+
- Ollama (with qwen2:7b or similar model)
- pip/poetry for dependency management

## 📦 Installation

### 1. Set up Ollama
```bash
# Install Ollama from https://ollama.ai
# Pull the qwen2 model
ollama pull qwen2:7b

# Start Ollama server
ollama serve
```

### 2. Install Backend Dependencies
```bash
cd health-advisor-backend
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
cp .env.example .env
# Edit .env with your settings
```

## 🚀 Running the Backend

```bash
# Development mode with auto-reload
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Production mode
python main.py
```

## 📚 API Documentation

### Interactive Docs
- Swagger UI: `http://localhost:8000/api/docs`
- ReDoc: `http://localhost:8000/api/redoc`

### Endpoints

#### Health Check
```
GET /api/health
```
Returns service status

#### Analyze Patient Health
```
POST /api/analyze
Content-Type: application/json

{
  "patient_data": "Age: 35, Weight: 85kg, Height: 180cm, Exercise: 2 times/week, Diet: Mixed, Sleep: 6 hours"
}
```

**Response:**
```json
{
  "summary": "Health summary...",
  "healthy_habits": ["Exercises regularly", "..."],
  "unhealthy_habits": ["Insufficient sleep", "..."],
  "recommendations": ["Increase sleep hours", "..."],
  "disclaimer": "Medical disclaimer...",
  "timestamp": "2024-01-15T10:30:00"
}
```

## 🔧 Configuration

Edit `.env` file to customize:

```
# API Settings
API_HOST=0.0.0.0
API_PORT=8000

# LLM Settings
LLM_MODEL=qwen2:7b
LLM_TEMPERATURE=0.5
LLM_MAX_TOKENS=2048

# Logging
LOG_LEVEL=INFO
```

## 📝 Project Structure

```
health-advisor-backend/
├── main.py              # FastAPI application
├── config.py            # Configuration settings
├── models.py            # Pydantic models
├── services.py          # Health analysis service
├── requirements.txt     # Python dependencies
├── .env.example         # Environment template
└── README.md            # This file
```

## 🧪 Testing

### Using cURL
```bash
curl -X POST "http://localhost:8000/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "patient_data": "Age: 28, Weight: 65kg, Height: 168cm, Exercises: 4 times/week, Sleep: 8 hours, Stress: Low"
  }'
```

### Using Python
```python
import requests

response = requests.post(
    "http://localhost:8000/api/analyze",
    json={
        "patient_data": "Age: 35, Weight: 85kg, Height: 180cm, Exercise: 2 times/week, Sleep: 6 hours"
    }
)

print(response.json())
```

## 🐛 Troubleshooting

### Connection Error to Ollama
```
Error: Failed to connect to Ollama
Solution: Ensure Ollama server is running (ollama serve)
```

### Model Not Found
```
Error: Model qwen2:7b not found
Solution: Pull the model (ollama pull qwen2:7b)
```

### CORS Issues
Add frontend URL to CORS_ORIGINS in config.py:
```python
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://yourfrontend.com"
]
```

## 📊 Logging

Logs are outputted to console. Configure log level in `.env`:
- DEBUG: Detailed information
- INFO: General information
- WARNING: Warning messages
- ERROR: Error messages

## 🔒 Security Notes

- Validate all input data
- Use HTTPS in production
- Implement rate limiting
- Add authentication/authorization
- Keep dependencies updated

## 🤝 Integration with Frontend

Frontend should send POST requests to `/api/analyze` endpoint with patient data.

Example React component:
```javascript
const response = await fetch('http://localhost:8000/api/analyze', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ patient_data: userInput })
});
```

## 📄 License

MIT License

## 👨‍💼 Author

Sajid Flutter Developer

## 📞 Support

For issues and questions, create an issue in the repository.
