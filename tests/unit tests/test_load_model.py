import pytest
import mlflow.sklearn
from mlflow.tracking import MlflowClient

def test_load_model_from_mlflow():
    """
    Test unitaire pour vérifier que les modèles peuvent être chargés depuis MLflow.
    """
    # Configurer le tracking URI pour pointer vers Dagshub
    repo_owner = "thuylinh.co"
    repo_name = "MLProduction_project"
    mlflow.set_tracking_uri(f"https://dagshub.com/{repo_owner}/{repo_name}.mlflow")

    model_name = "Food_model"
    client = MlflowClient()

    # Récupérer la dernière version du modèle en Production
    latest_version = client.get_latest_versions(model_name, stages=["Production"])[0].version
    model_uri = f"models:/{model_name}/{latest_version}"
    
    try:
        model = mlflow.sklearn.load_model(model_uri)
    except Exception as e:
        pytest.fail(f"Le chargement du modèle a échoué : {e}")
    
    assert model is not None, "Le modèle chargé ne devrait pas être None."
