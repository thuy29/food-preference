# Food Preference Prediction App

This project was developed as part of the **Machine Learning in Production** course. It is a full-stack web application that predicts user food preferences (food type, juice choice, and dessert) based on demographic inputs. The app integrates a machine learning model served via an API and includes complete CI/CD workflows, data versioning, and cloud deployment.

## Project Overview

- **Frontend:** React.js (UI for input and results display)
- **Backend:** FastAPI (serves ML model predictions)
- **ML Model:** Random Forest (trained using scikit-learn)
- **ML Management:** MLflow (experiments, model registry), DVC (data versioning)
- **CI/CD:** GitHub Actions
- **Deployment:** DockerHub + AWS Elastic Beanstalk (backend), GitHub Pages (frontend)
- **Data Storage:** AWS S3 (via DVC)
- **Tracking URI:** DagsHub

## Features

- Predicts food preferences from Gender, Nationality, and Age
- ML model automatically versioned and deployed from MLflow
- Data version control with DVC
- Unit, integration, and end-to-end tests integrated in CI
- Dockerized backend and frontend
- CI/CD pipeline: from staging to production via GitHub Actions

## Tech Stack

| Component      | Technology                  |
|----------------|------------------------------|
| Frontend       | React.js                     |
| Backend        | FastAPI                      |
| ML pipeline    | scikit-learn + imbalanced-learn |
| Experiment Tracking | MLflow + DagsHub       |
| Data Versioning | DVC + AWS S3                |
| CI/CD          | GitHub Actions               |
| Containers     | Docker                       |
| Deployment     | AWS Elastic Beanstalk, GitHub Pages |

## Project Structure
dev-ops-final-project/
├── backend/ # FastAPI app with ML model loading
├── frontend/ # ReactJS app for user interaction
├── ML-model/ # fetch_latest_model.py and utilities
├── .github/workflows/ # CI/CD GitHub Action workflows
├── requirements.txt
├── Dockerfile (backend/frontend)
└── README.md


## Testing

- ✅ 3 Unit tests (model logic, API validation)
- ✅ 3 Integration tests (React form, backend API endpoint)
- ✅ 3 End-to-end tests (data-to-prediction flow)

## Setup Instructions

### Clone the repository

```bash
git clone https://github.com/thuy29/food-preference.git
cd food-preference
```

Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn api:app --reload
```

# Build and run the app using Docker
```bash
docker build -t backend-api:latest -f backend/Dockerfile .
docker build -t frontend-app:latest -f frontend/Dockerfile .
docker run -d --network host backend-api
docker run -d -p 3000:80 frontend-app
```

Demo
Frontend URL: https://<your-gh-username>.github.io/<your-repo-name>

Model & Data Management
ML model trained and logged with MLflow on DagsHub

Model version fetched dynamically in production Docker image

Data versioned and tracked with DVC on AWS S3

