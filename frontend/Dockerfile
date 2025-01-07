FROM node:16 AS build

WORKDIR /app

COPY frontend/package*.json /app/
RUN npm install

COPY . /app
RUN npm run build

EXPOSE 3000
CMD ["npx", "serve", "-s", "build", "-l", "3000"]
