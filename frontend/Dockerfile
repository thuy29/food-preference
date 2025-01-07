FROM node:16 AS build

WORKDIR /app

COPY requirements.txt /app/
COPY frontend/package*.json /app/

RUN npm install

COPY frontend/ /app



# Étape finale pour servir l'application
FROM node:16
WORKDIR /app
COPY --from=build /app/build /app
RUN npm install -g http-server

EXPOSE 3000
CMD ["http-server", ".", "-p", "3000"]
