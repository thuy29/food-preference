from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
import mlflow.sklearn
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

# Charger les variables d'environnement
load_dotenv()

# Récupérer les variables d'environnement
dagshub_token = os.getenv("DAGSHUB_TOKEN")
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

repo_owner = "thuylinh.co"
repo_name = "MLProduction_project"
mlflow.set_tracking_uri(f"https://dagshub.com/{repo_owner}/{repo_name}.mlflow")

from mlflow.tracking import MlflowClient

client = MlflowClient()
food_version = client.get_latest_versions("Food_model", stages=["Production"])[0].version
juice_version = client.get_latest_versions("Juice_model", stages=["Production"])[0].version
dessert_version = client.get_latest_versions("Dessert_model", stages=["Production"])[0].version

food_model = mlflow.sklearn.load_model(f"models:/Food_model/{food_version}")
juice_model = mlflow.sklearn.load_model(f"models:/Juice_model/{juice_version}")
dessert_model = mlflow.sklearn.load_model(f"models:/Dessert_model/{dessert_version}")

# Initialiser l'application FastAPI
app = FastAPI(title="Food Preference Prediction API")

# Configurer CORS pour autoriser les requêtes provenant de ton frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Autorise cette origine spécifique
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autorise tous les headers
)

# Définir un schéma de requête avec validation
class UserInput(BaseModel):
    Gender: str = Field(..., description="Gender must be 'Male' or 'Female'")
    Nationality: str
    Age: int = Field(..., gt=0, le=120, description="Age must be between 1 and 120")

    @validator("Gender")
    def validate_gender(cls, value):
        """
        Valide que le genre est soit 'Male', soit 'Female'.
        """
        valid_genders = ["Male", "Female"]
        if value not in valid_genders:
            raise ValueError(f"Invalid gender: {value}. Must be 'Male' or 'Female'.")
        return value

@app.post("/predict")
def predict_preferences(user_input: UserInput):
    try:
        # Créer un DataFrame "brut" avec les mêmes colonnes que X
        input_df = pd.DataFrame([{
            "Gender": user_input.Gender,
            "Nationality": user_input.Nationality,
            "Age": user_input.Age
        }])

        # Appeler directement le modèle chargé via MLflow
        food_prediction = food_model.predict(input_df)[0]
        juice_prediction = juice_model.predict(input_df)[0]
        dessert_prediction = dessert_model.predict(input_df)[0]

        return {
            "Food": food_prediction,
            "Juice": juice_prediction,
            "Dessert": dessert_prediction
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


# Endpoint pour récupérer les métriques des modèles
@app.get("/metrics")
def get_metrics():
    return {
        "message": "Endpoint to show metrics"
    }
