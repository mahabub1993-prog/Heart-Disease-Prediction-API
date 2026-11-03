
from fastapi import FastAPI
from pathlib import Path
import joblib
import pandas as pd

from app.schemas import HeartDiseaseInput

# Project base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load trained ML model
MODEL_PATH = BASE_DIR / "model" / "heart_model.joblib"

model_data = joblib.load(MODEL_PATH)

model = model_data["model"]
features = model_data["features"]
model_type = model_data["model_type"]

# Initialize FastAPI application
app = FastAPI(
    title="Heart Disease Prediction API",
    description=(
        "Machine Learning API for educational "
        "heart disease prediction. "
        "Not for medical diagnosis."
    ),
    version="1.0.0"
)


# Health Check Endpoint
@app.get("/health")
def health():
    return {"status": "healthy"}


# Model Information Endpoint
@app.get("/info")
def info():
    return {
        "model_type": model_type,
        "features": features,
        "test_accuracy": model_data.get("accuracy")
    }


# Heart Disease Prediction Endpoint
@app.post("/predict")
def predict(data: HeartDiseaseInput):

    input_data = data.model_dump()

    input_df = pd.DataFrame(
        [input_data],
        columns=features
    )

    prediction = int(model.predict(input_df)[0])

    return {
        "heart_disease": bool(prediction),
        "disclaimer": (
            "Educational prediction only. "
            "Not a medical diagnosis."
        )
    }
