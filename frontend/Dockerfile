FROM node:16 AS build

WORKDIR /app

COPY package*.json /app/
RUN npm install

COPY . /app
RUN npm run build

# Étape finale pour servir l'application
FROM node:16
WORKDIR /app
COPY --from=build /app/build /app
RUN npm install -g serve

EXPOSE 3000
CMD ["serve", "-s", ".", "-l", "3000"]