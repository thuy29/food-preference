# tests/test_api_integration.py

import pytest
import requests

@pytest.fixture(scope="session")
def start_api():
    """
    Lance l'API (par exemple via subprocess) et attend qu'elle soit prête.
    Ou supposer qu'elle est déjà lancée en local (uvicorn main:app --port 8000).
    """
    # Code pour démarrer l'API si besoin (ou pas si vous la lancez à la main)
    yield
    # Code pour arrêter l'API si nécessaire

def test_api_predict(start_api):
    """
    Vérifie qu'on obtient bien un statut 200
    et que la réponse contient les clés Food, Juice, Dessert.
    """
    url = "http://127.0.0.1:8000/predict"
    payload = {
        "Gender": "Male",
        "Nationality": "Indian",
        "Age": 25
    }

    response = requests.post(url, json=payload)
    
    assert response.status_code == 200

    json_data = response.json()

    # Clés attendues dans la réponse
    assert "Food" in json_data, "Pas de clé 'Food' dans la réponse JSON"
    assert "Juice" in json_data, "Pas de clé 'Juice' dans la réponse JSON"
    assert "Dessert" in json_data, "Pas de clé 'Dessert' dans la réponse JSON"

    # Vous pouvez aller plus loin :
    # Vérifier que 'Food' est un string, par exemple
    assert isinstance(json_data["Food"], str), "Le champ Food devrait être une chaîne"


def test_integration_api_missing_field():
    """
    Test d'intégration : Vérifie le comportement de l'API lorsqu'un champ obligatoire est manquant.
    """
    url = "http://127.0.0.1:8000/predict"
    payload = {
        "Gender": "Male",
        "Age": 25  # Nationality manquante
    }
    response = requests.post(url, json=payload)
    
    assert response.status_code == 422, "L'API devrait renvoyer un statut 422 pour une requête avec un champ manquant."

def test_api_predict_large_age(start_api):
    """
    Vérifie que l'API renvoie une erreur 422 lorsqu'un âge trop grand est fourni.
    """
    url = "http://127.0.0.1:8000/predict"
    payload = {
        "Gender": "Female",
        "Nationality": "Indian",
        "Age": 150  # Âge invalide
    }
    response = requests.post(url, json=payload)

    assert response.status_code == 422, "L'API devrait renvoyer une erreur 422 pour un âge supérieur à la limite autorisée"
