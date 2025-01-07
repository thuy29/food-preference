FROM node:16 AS build

WORKDIR /app
COPY frontend/package*.json /app/
RUN npm install
COPY . /app
RUN npm run build

FROM node:16-alpine

WORKDIR /app
COPY --from=build /app/build /app
RUN npm install -g http-server

EXPOSE 3000
CMD ["http-server", ".", "-p", "3000"]
