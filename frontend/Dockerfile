# Utiliser une image de base officielle Node.js pour construire le frontend
FROM node:16 AS build

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers package.json et package-lock.json
COPY frontend/package*.json /app/

# Installer les dépendances
RUN npm install

# Copier le reste des fichiers du frontend
COPY frontend/ /app

# Construire l'application React
RUN npm run build

# Utiliser une image de base Nginx pour servir l'application React
FROM nginx:alpine

# Copier les fichiers de build dans le répertoire par défaut de Nginx
COPY --from=build /app/build /usr/share/nginx/html

# Exposer le port 80 pour le serveur Nginx
EXPOSE 80

# Commande de démarrage de Nginx
CMD ["nginx", "-g", "daemon off;"]
