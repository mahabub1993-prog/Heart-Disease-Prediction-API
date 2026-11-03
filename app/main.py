from fastapi import FastAPI
from pathlib import Path
import joblib
import pandas as pd

from app.schemas import HeartDiseaseInput


# STEP 1: Load Trained ML Model

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "heart_model.joblib"

model_data = joblib.load(MODEL_PATH)

model = model_data["model"]
features = model_data["features"]
model_type = model_data["model_type"]


# STEP 2: Create FastAPI Application

app = FastAPI(
    title="Heart Disease Prediction API",
    description="Machine Learning API for educational heart disease prediction. Not for medical diagnosis.",
    version="1.0.0"
)


# STEP 3: Health Check API

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


# STEP 4: Model Information API

@app.get("/info")
def info():

    return {
        "model_type": model_type,
        "features": features,
        "test_accuracy": model_data.get("accuracy")
    }


# STEP 5: Prediction API

@app.post("/predict")
def predict(data: HeartDiseaseInput):

    input_data = data.model_dump()

    input_df = pd.DataFrame(
        [input_data],
        columns=features
    )

    prediction = int(model.predict(input_df)[0])

    return {
        "prediction": prediction,

        "prediction_label": (
            "Positive model prediction"
            if prediction == 1
            else "Negative model prediction"
        ),

        "disclaimer": (
            "Educational prediction only. "
            "Not a medical diagnosis."
        )
    }