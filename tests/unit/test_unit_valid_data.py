import pytest
from fastapi.testclient import TestClient
import sys
import os

# Ajouter dynamiquement le chemin du dossier parent au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.api import app  # Import après avoir modifié le PYTHONPATH


client = TestClient(app)

def test_api_invalid_gender():
    """
    Test unitaire pour vérifier que l’API renvoie une erreur avec un genre invalide.
    """
    payload = {
        "Gender": "Unknown",  # Genre invalide
        "Nationality": "Indian",
        "Age": 25
    }
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 422, "L’API devrait renvoyer un statut 422 pour une entrée invalide."

def test_api_invalid_age():
    """
    Test unitaire pour vérifier que l’API renvoie une erreur avec un âge hors limite.
    """
    payload = {
        "Gender": "Male",
        "Nationality": "Indian",
        "Age": -5  # Âge invalide
    }
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 422, "L’API devrait renvoyer un statut 422 pour un âge négatif."
