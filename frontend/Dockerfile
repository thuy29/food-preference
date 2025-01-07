# Étape de build
FROM node:16 AS build

WORKDIR /app

# Copier uniquement les fichiers nécessaires pour l'installation des dépendances
COPY frontend/package*.json ./
RUN npm install

# Copier le reste des fichiers et construire le frontend
COPY frontend/ ./
RUN npm run build

# Étape finale pour servir l'application avec http-server
FROM node:16
WORKDIR /app
COPY --from=build /app/build /app
RUN npm install -g http-server

EXPOSE 3000
CMD ["http-server", ".", "-p", "3000"]
