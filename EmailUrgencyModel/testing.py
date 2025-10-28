import gradio as gr
import joblib
import numpy as np
from sentence_transformers import SentenceTransformer

regressor = joblib.load("urgency_predictor.pkl")  
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def predict_urgency(email_text):
    if not email_text.strip():
        return "Please enter an email to analyze."

    # Generate embeddings
    embedding = embedder.encode([email_text])
    
    # Predict urgency score
    urgency_score = regressor.predict(embedding)[0]

    # Classify into levels for easier interpretation
    if urgency_score >= 0.8:
        level = "🚨 High Urgency"
    elif urgency_score >= 0.5:
        level = "⚠️ Medium Urgency"
    else:
        level = "🕐 Low Urgency"

    return {
        "Urgency Score": round(float(urgency_score), 3),
        "Category": level
    }

interface = gr.Interface(
    fn=predict_urgency,
    inputs=gr.Textbox(
        lines=8,
        placeholder="Paste your email content here...",
        label="Email Content"
    ),
    outputs=[
        gr.JSON(label="Predicted Urgency")
    ],
    title="AI Email Urgency Predictor",
    description="Paste your email text and get an AI-estimated urgency score using NLP + Regression."
)

interface.launch(share=True)
