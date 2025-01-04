# tests/test_e2e.py

import pytest
import requests
import pandas as pd

def test_e2e_food_preference_prediction():
    """
    Test de bout en bout (End-to-End) qui couvre l'ensemble du pipeline :
    1. Charger un dataset d'exemple
    2. Envoyer des requêtes à l'API pour prédiction
    3. Vérifier que les résultats sont cohérents
    """
    # Exemple de dataset d'entrée
    data = [
        {"Gender": "Male", "Nationality": "Indian", "Age": 25},
        {"Gender": "Female", "Nationality": "Pakistani", "Age": 30},
        {"Gender": "Male", "Nationality": "Canadian", "Age": 40},
    ]
    df_input = pd.DataFrame(data)

    # URL de l'API
    url = "http://127.0.0.1:8000/predict"

    for index, row in df_input.iterrows():
        payload = {
            "Gender": row["Gender"],
            "Nationality": row["Nationality"],
            "Age": row["Age"]
        }
        response = requests.post(url, json=payload)
        
        # Vérifier que la réponse a le bon statut
        assert response.status_code == 200, f"Echec avec le statut {response.status_code} pour la requête {payload}"
        
        json_data = response.json()
        
        # Vérification des clés dans la réponse
        assert "Food" in json_data, "La réponse ne contient pas la clé 'Food'"
        assert "Juice" in json_data, "La réponse ne contient pas la clé 'Juice'"
        assert "Dessert" in json_data, "La réponse ne contient pas la clé 'Dessert'"
        
        # Vérifier que les prédictions sont des strings non vides
        assert isinstance(json_data["Food"], str) and json_data["Food"], "La prédiction 'Food' doit être une chaîne non vide"
        assert isinstance(json_data["Juice"], str) and json_data["Juice"], "La prédiction 'Juice' doit être une chaîne non vide"
        assert isinstance(json_data["Dessert"], str) and json_data["Dessert"], "La prédiction 'Dessert' doit être une chaîne non vide"

def test_e2e_invalid_request():
    """
    Test de bout en bout avec une requête invalide.
    Vérifie que l'API renvoie un statut 422 pour une entrée incorrecte.
    """
    url = "http://127.0.0.1:8000/predict"
    payload = {
        "Gender": "Unknown",  # Genre invalide
        "Nationality": "Indian",
        "Age": 25
    }
    response = requests.post(url, json=payload)
    
    assert response.status_code == 422, "L'API devrait renvoyer un statut 422 pour une entrée invalide."

def test_e2e_large_input():
    """
    Test de bout en bout avec un grand nombre de requêtes pour vérifier la stabilité de l'API.
    """
    url = "http://127.0.0.1:8000/predict"
    data = [
        {"Gender": "Male", "Nationality": "Indian", "Age": i} for i in range(1, 101)
    ]

    for payload in data:
        response = requests.post(url, json=payload)
        assert response.status_code == 200, f"Echec avec le statut {response.status_code} pour la requête {payload}"
        json_data = response.json()
        assert "Food" in json_data, "La réponse ne contient pas la clé 'Food'"
        assert "Juice" in json_data, "La réponse ne contient pas la clé 'Juice'"
        assert "Dessert" in json_data, "La réponse ne contient pas la clé 'Dessert'"
