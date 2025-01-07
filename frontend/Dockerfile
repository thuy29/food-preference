FROM node:16 AS build

WORKDIR /app

# Copier les fichiers package.json et package-lock.json
COPY frontend/package*.json ./
RUN npm install

# Copier tout le contenu de frontend
COPY frontend/ ./
RUN npm run build

# Étape finale pour servir l'application
FROM node:16
WORKDIR /app
COPY --from=build /app/build /app
RUN npm install -g http-server

EXPOSE 3000
CMD ["http-server", ".", "-p", "3000"]
