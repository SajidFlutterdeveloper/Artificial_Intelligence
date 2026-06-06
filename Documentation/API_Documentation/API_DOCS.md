# API Documentation - Fintech AI Assistant

The backend service provides several endpoints for data synchronization and AI-driven insights.

**Base URL**: `http://<server-ip>:5000/`

## Endpoints

### 1. Get spending Prediction
Predicts the user's spending for the next month.

- **URL**: `/predict/{email}`
- **Method**: `GET`
- **Path Parameters**:
  - `email`: The registered user's email address.
- **Response**:
  ```json
  {
    "predicted_expense": 1250.50,
    "confidence": 0.85,
    "insights": "Your spending on utilities is expected to rise."
  }
  ```

### 2. Add Expense (Manual Sync)
Synchronizes a manually entered expense to the server.

- **URL**: `/add_expense`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "amount": 25.00,
    "category": "Food",
    "date": "2024-05-20",
    "email": "user@example.com"
  }
  ```
- **Response**: `200 OK`

### 3. Add Expense (AI/Auto)
Processes a natural language or OCR request to extract and save an expense.

- **URL**: `/add_expense_auto`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "query": "Spent 20 for taxi today",
    "email": "user@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "extracted_amount": 20.0,
    "extracted_category": "Transport",
    "status": "success"
  }
  ```

### 4. AI Chat Assistant
Interact with the AI assistant for financial advice.

- **URL**: `/chat`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "message": "Give me a budget tip.",
    "email": "user@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "reply": "Consider the 50/30/20 rule: 50% for needs, 30% for wants, and 20% for savings.",
    "timestamp": "2024-05-20T10:00:00Z"
  }
  ```

## Authentication
Currently, the API uses the user's `email` as a unique identifier for requests. Future versions will implement JWT-based authentication.
