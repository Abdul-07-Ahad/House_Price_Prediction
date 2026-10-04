# 🏠 House Price Prediction

A machine learning web application that predicts house prices from property features. The project has been developed from a basic machine learning model into a containerized application with PostgreSQL, Kubernetes, and automated GitHub workflows.

## 🚀 Features

* Machine learning model for house price prediction
* Flask web application
* PostgreSQL database integration
* Docker containerization
* Docker Compose for multi-container development
* Kubernetes deployment configuration
* GitHub Actions automation
* Health-check endpoint
* Web-based prediction interface

## 🛠️ Tech Stack

* **Python**
* **Scikit-learn**
* **Pandas**
* **Flask**
* **PostgreSQL**
* **Docker**
* **Docker Compose**
* **Kubernetes**
* **GitHub Actions**
* **HTML / CSS**

## 📁 Project Structure

```text
House_Price_Prediction/
│
├── .github/
│   └── workflows/
├── data/
├── database/
├── kubernetes/
├── models/
├── src/
├── static/
├── templates/
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

1. Property information is provided through the web interface.
2. The Flask application receives the input.
3. The trained machine learning model processes the features.
4. A predicted house price is generated.
5. PostgreSQL is used as the application's database layer.
6. Docker provides a reproducible application environment.
7. Kubernetes manifests provide deployment configuration.
8. GitHub Actions automate parts of the project workflow.

## 🐳 Run with Docker Compose

Clone the repository and enter the project directory:

```bash
git clone https://github.com/Abdul-07-Ahad/House_Price_Prediction.git
cd House_Price_Prediction
```

Start the application:

```bash
docker compose up --build
```

The application can then be accessed through the configured Flask port.

## ☸️ Kubernetes

The repository also contains Kubernetes manifests in the `kubernetes/` directory for deploying the application.

## 📌 Project Goal

This project started as a machine learning exercise and evolved into a practical AI/ML engineering project. The goal was to learn not only how to train a model, but also how to package, deploy, and automate an ML application using modern development and DevOps tools.

## 🔮 Future Improvements

* Improve model accuracy and evaluation
* Add model versioning
* Add automated testing
* Improve CI/CD pipeline
* Add monitoring and logging
* Develop a more advanced ML model
* Expand the prediction features

## 👨‍💻 Author

**Abdul Ahad**

AI Engineering Student interested in Machine Learning, Deep Learning, AI applications, DevOps and MLOps.
