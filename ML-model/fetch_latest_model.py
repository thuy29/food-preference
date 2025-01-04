import mlflow
from mlflow.tracking import MlflowClient
import os

# Charger le token DagsHub depuis les variables d'environnement
dagshub_token = os.getenv("DAGSHUB_TOKEN")

# Configurer l'URI de suivi MLflow pour DagsHub
repo_owner = "thuylinh.co"
repo_name = "MLProduction_project"
mlflow.set_tracking_uri(f"https://dagshub.com/{repo_owner}/{repo_name}.mlflow")

# Initialiser le client MLflow
client = MlflowClient()

# Fonction pour télécharger la dernière version d'un modèle
def fetch_latest_model(model_name):
    latest_version = client.get_latest_versions(model_name, stages=["Production"])[0].version
    model_uri = f"models:/{model_name}/{latest_version}"
    local_path = f"models/{model_name}"
    
    # Télécharger le modèle localement
    mlflow.artifacts.download_artifacts(model_uri, dst_path=local_path)
    print(f"Downloaded {model_name} version {latest_version} to {local_path}")

# Télécharger les derniers modèles
fetch_latest_model("Food_model")
fetch_latest_model("Juice_model")
fetch_latest_model("Dessert_model")
