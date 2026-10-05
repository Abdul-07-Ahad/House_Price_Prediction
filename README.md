# 🏠 House Price Prediction

An end-to-end machine learning web application that predicts house prices from property features. The project evolved from a basic machine learning model into a containerized, database-backed application deployed with Kubernetes and automated through a CI/CD and GitOps workflow.

## 🚀 Features

* Machine learning model for house price prediction
* Flask web application
* PostgreSQL database integration
* User authentication and prediction history
* Input validation
* Docker containerization
* Docker Compose for local multi-container development
* Kubernetes deployment
* Persistent PostgreSQL storage using Kubernetes PVC
* Kubernetes ConfigMap and Secret configuration
* Health-check endpoint
* Automated testing with Pytest
* GitHub Actions CI/CD pipeline
* Docker image publishing to Docker Hub
* GitOps deployment with Argo CD
* Immutable Docker image tagging using Git commit SHA
* Automated Kubernetes synchronization and self-healing through Argo CD

## 🛠️ Tech Stack

| Category           | Technologies           |
| ------------------ | ---------------------- |
| Programming        | Python                 |
| Machine Learning   | Scikit-learn, Pandas   |
| Web                | Flask, HTML, CSS       |
| Database           | PostgreSQL             |
| Testing            | Pytest                 |
| Containerization   | Docker, Docker Compose |
| Orchestration      | Kubernetes             |
| CI/CD              | GitHub Actions         |
| Container Registry | Docker Hub             |
| GitOps / CD        | Argo CD                |
| Version Control    | Git, GitHub            |

## 📁 Project Structure

```text
House_Price_Prediction/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
├── database/
├── kubernetes/
│   ├── namespace.yaml
│   ├── flask-config.yaml
│   ├── flask-deployment.yaml
│   ├── flask-service.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-service.yaml
│   ├── postgres-pvc.yaml
│   └── ingress.yaml
│
├── models/
├── src/
├── static/
├── templates/
├── tests/
│
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── app.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

1. A user enters property information through the Flask web interface.
2. Flask validates the input.
3. The trained machine learning model processes the property features.
4. A predicted house price is generated.
5. The prediction is stored in PostgreSQL.
6. Docker packages the application and its dependencies into a reproducible container.
7. Docker Compose runs the Flask application and PostgreSQL together during local development.
8. Kubernetes provides the deployment and service infrastructure.
9. GitHub Actions automatically tests the application and builds the Docker image.
10. On changes merged to `main`, GitHub Actions publishes an immutable Docker image tagged with the Git commit SHA.
11. GitHub Actions updates the Kubernetes deployment manifest with the new image.
12. Argo CD detects the Git change and automatically synchronizes the Kubernetes cluster.

## 🔄 CI/CD + GitOps Workflow

```text
Developer
    │
    ▼
 GitHub
    │
    ▼
GitHub Actions
    │
    ├── Run tests
    ├── Check Python syntax
    ├── Build Docker image
    │
    └── On main branch
            │
            ▼
       Docker Hub
            │
            ▼
  Update Kubernetes manifest
            │
            ▼
        GitHub main
            │
            ▼
         Argo CD
            │
            ├── Auto Sync
            ├── Self Heal
            └── Prune
            │
            ▼
      Kubernetes Cluster
            │
       ┌────┴────┐
       ▼         ▼
    Flask    PostgreSQL
```

### CI Pipeline

For pull requests and pushes to `main`, GitHub Actions:

* Installs Python dependencies
* Checks Python syntax
* Runs automated tests
* Builds the Docker image

### Continuous Delivery / GitOps

When code is pushed to `main`:

1. GitHub Actions builds the application image.
2. The image is tagged with the Git commit SHA.
3. The image is pushed to Docker Hub.
4. The Kubernetes deployment manifest is updated with the new image tag.
5. The manifest change is committed back to GitHub.
6. Argo CD detects the desired-state change in Git.
7. Argo CD synchronizes Kubernetes automatically.

This separates **CI** from **deployment reconciliation** and demonstrates a practical GitOps workflow.

## 🐳 Run with Docker Compose

Clone the repository:

```bash
git clone https://github.com/Abdul-07-Ahad/House_Price_Prediction.git
cd House_Price_Prediction
```

Start the application and PostgreSQL:

```bash
docker compose up --build
```

The Flask application will be available on the configured application port.

To stop the containers:

```bash
docker compose down
```

## ☸️ Kubernetes

The `kubernetes/` directory contains the Kubernetes resources required to deploy the application.

The deployment includes:

* Flask application Deployment
* PostgreSQL Deployment
* Flask Service
* PostgreSQL Service
* PostgreSQL PersistentVolumeClaim
* ConfigMap
* Kubernetes Secret references
* Ingress
* Namespace

The Flask deployment also uses Kubernetes readiness and liveness probes through the `/health` endpoint.

## 🧪 Testing

Automated tests are written using Pytest.

Run the tests locally with:

```bash
pytest -q
```

The test suite covers:

* Application health endpoint
* Successful prediction flow
* Prediction input validation

## 🔐 Configuration and Secrets

Sensitive configuration is not stored directly in the repository.

Local environment variables are used for database credentials and Flask configuration.

In Kubernetes, sensitive database credentials are provided through a Kubernetes Secret, while non-sensitive configuration is provided through a ConfigMap.

## 📌 Project Evolution

This project started as a simple machine learning exercise and was gradually developed into an end-to-end AI/ML engineering project.

The progression was:

```text
Machine Learning Model
        ↓
Flask Web Application
        ↓
PostgreSQL Integration
        ↓
Docker
        ↓
Docker Compose
        ↓
Automated Testing
        ↓
GitHub Actions
        ↓
Docker Hub
        ↓
Kubernetes
        ↓
Argo CD
        ↓
GitOps-based Deployment
```

The main goal was to learn not only how to train a machine learning model, but also how to package, test, deploy, and continuously deliver an ML application using modern engineering and DevOps practices.

## 🔮 Future Improvements

* Improve model accuracy and experiment with additional algorithms
* Add model versioning and experiment tracking
* Add ML-specific evaluation and monitoring
* Add application monitoring and logging
* Improve Kubernetes scalability
* Add more comprehensive automated tests
* Add a dedicated ML pipeline for model retraining

## 👨‍💻 Author

**Abdul Ahad**

AI Engineering Student interested in Machine Learning, Deep Learning, AI Engineering, DevOps, MLOps, and GitOps.

