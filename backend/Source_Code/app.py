"""
Fintech AI Assistant - Backend API
Version: 1.0
Author: AI Assistant
Description: Flask-based API for handling financial predictions,
             AI-driven chat assistance, and data synchronization.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from model_loader import ModelLoader
from predictor import FinancePredictor
from ai_assistant import ai_finance_assistant
import os
import logging

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Load model and initialize predictor at startup
try:
    model = ModelLoader.load_model()
    if model:
        predictor = FinancePredictor(model)
        logger.info("Machine Learning model loaded successfully.")
    else:
        predictor = None
        logger.warning("Prediction model not found. Some endpoints will be disabled.")
except Exception as e:
    logger.error(f"Error initializing model: {e}")
    predictor = None

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint for AI Financial Assistant Chat"""
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data.get('message')
    user_data = data.get('userData', {}) # Optional user context (budget, etc.)

    logger.info(f"Received chat message: {user_message[:50]}...")

    try:
        response = ai_finance_assistant(user_message, user_data)
        return jsonify(response)
    except Exception as e:
        logger.error(f"Chat processing error: {e}")
        return jsonify({"error": "Internal server error during chat processing"}), 500

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint for financial trend prediction"""
    if predictor is None:
        return jsonify({"error": "Model not loaded on server"}), 503

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    amounts = data.get('amounts', [])
    user_email = data.get('userEmail', 'unknown')

    if not amounts:
        return jsonify({
            "final_prediction": 0,
            "trend": "0%",
            "model_status": "No data",
            "insights": []
        })

    try:
        final_prediction = predictor.predict_total(amounts)
        # Simple heuristic for previous average comparison
        previous_avg = sum(amounts) / len(amounts) * 30 / 7 if len(amounts) > 0 else 0
        trend = predictor.calculate_trend(final_prediction, previous_avg)
        insights = predictor.generate_insights(amounts, final_prediction)

        return jsonify({
            "status": "success",
            "final_prediction": round(final_prediction, 2),
            "xgboost_prediction": round(final_prediction, 2),
            "trend": trend,
            "transaction_count": len(amounts),
            "model_status": "XGBoost Active",
            "insights": insights
        })
    except Exception as e:
        logger.error(f"Prediction error for {user_email}: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "ok",
        "model_loaded": predictor is not None,
        "api_version": "1.0.0"
    })

if __name__ == '__main__':
    # Default port 5000, listening on all interfaces
    port = int(os.environ.get("PORT", 5000))
    logger.info(f"Starting Fintech AI Backend on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=False)
