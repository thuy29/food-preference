# Utiliser une image de base officielle Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

COPY requirements.txt /app/

# Copier les fichiers de l'application dans le conteneur
COPY backend/ /app

# Installer les dépendances
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Exposer le port utilisé par l'API
EXPOSE 8000

# Commande pour lancer l'application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
