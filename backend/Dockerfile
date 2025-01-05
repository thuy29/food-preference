# Utiliser une image de base officielle Python 
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt /app/
COPY ML-model/fetch_latest_model.py /app/ML-model/
COPY backend/ /app/

# Installer les dépendances
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Récupérer les derniers modèles depuis MLflow/DagsHub
ENV DAGSHUB_TOKEN=${DAGSHUB_TOKEN}
RUN python /app/ML-model/fetch_latest_model.py

# Exposer le port utilisé par l'API
EXPOSE 8000

# Commande pour lancer l'application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
