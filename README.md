# Heart Disease Prediction API

A Machine Learning-powered REST API built with **Python, Scikit-learn, FastAPI, and Docker** to predict heart disease risk from patient health attributes.

> **Disclaimer:** This project is for educational purposes only. It is not a medical diagnostic tool and must not replace professional medical advice.

## Project Overview

This project uses a Random Forest classifier to predict whether a person belongs to the positive or negative heart disease class based on 13 input features.

The trained model is served through a REST API built with FastAPI and containerized using Docker.

## Technologies Used

- Python 3.12
- Pandas and NumPy
- Scikit-learn
- FastAPI
- Pydantic
- Joblib
- Docker
- Docker Compose

## Dataset

- Dataset: Heart Disease Dataset (Kaggle)
- Original records: 1,025
- Records after duplicate removal: 302
- Input features: 13
- Target column: `target`

The dataset CSV is excluded from this repository. Add your own `heart.csv` file to the project root if you want to retrain the model.

## Model Performance

| Metric | Score |
|---|---:|
| Cross-validation Accuracy | 85.05% |
| Test Accuracy | 80.33% |
| Precision | 83.87% |
| Recall | 78.79% |
| F1 Score | 81.25% |

**Algorithm:** Random Forest Classifier

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API health |
| GET | `/info` | Get model information |
| POST | `/predict` | Generate a prediction |
| GET | `/docs` | Interactive Swagger documentation |

## Run Locally

Clone the repository:

```bash
git clone https://github.com/mahabub1993-prog/Heart-Disease-Prediction-API.git
cd Heart-Disease-Prediction-API
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs](https://heart-disease-prediction-api-1-8mf3.onrender.com/docs
```

## Run with Docker

Build the Docker image:

```bash
docker compose build
```

Start the container:

```bash
docker compose up
```

Open:

```text
http://127.0.0.1:8000/docs](https://heart-disease-prediction-api-1-8mf3.onrender.com/docs
```

Stop the container:

```bash
docker compose down
```

## Sample Prediction Input

Send a POST request to `/predict`:

```json
{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
```

## Project Structure

```text
Heart-Disease-Prediction-API/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
├── model/
│   └── heart_model.joblib
├── train_model.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── .gitignore
```

## Author

**Md. Mahabub Hossain**

GitHub: https://github.com/mahabub1993-prog

## License

This project is intended for educational and learning purposes.
