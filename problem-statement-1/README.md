# End-to-End CI/CD Pipeline for a Web Application on Kubernetes

This project demonstrates a complete, automated pipeline for containerizing a web application, deploying it to a Kubernetes cluster, and securing it with TLS/HTTPS. The entire process, from code commit to deployment, is automated using a CI/CD workflow with GitHub Actions.



---
## 🚀 Features

* **Containerization:** The application is packaged into a lightweight, portable container using **Docker**.
* **Kubernetes Deployment:** The container is deployed on a Kubernetes cluster (Minikube) using declarative manifests for **Deployments** and **Services**.
* **CI/CD Automation:** A **GitHub Actions** workflow automatically builds and pushes the Docker image to a container registry (Docker Hub) on every push to the `main` branch.
* **Secure Access:** An **NGINX Ingress Controller** is used to manage external access, with **cert-manager** automatically providing a **TLS certificate** for secure HTTPS communication.

---
## 🛠️ Technologies Used

* **Containerization:** Docker
* **Orchestration:** Kubernetes (Minikube)
* **CI/CD:** GitHub Actions
* **Version Control:** Git & GitHub
* **Networking:** NGINX Ingress Controller
* **Security:** cert-manager (for TLS)
* **Configuration:** YAML

---
## 📋 Prerequisites

* [Docker](https://www.docker.com/products/docker-desktop/)
* [Minikube](https://minikube.sigs.k8s.io/docs/start/)
* [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* A Docker Hub account
* A GitHub account

---
## ⚙️ Setup and Usage

### 1. Configure GitHub Secrets

Before running the workflow, you must add the following secrets to your GitHub repository under **Settings > Secrets and variables > Actions**:
* `DOCKERHUB_USERNAME`: Your Docker Hub username.
* `DOCKERHUB_TOKEN`: A Docker Hub Access Token with Read, Write, Delete permissions.

### 2. Manual Deployment on Minikube

To deploy the application manually on a local Minikube cluster, follow these steps:

**a. Start Minikube:**
```bash
minikube start
```

**b. Apply Kubernetes Manifests:**
Apply the deployment, service, and other configurations.
```bash
kubectl apply -f k8s/
```

**c. Enable Ingress and Set Up Hosts File:**
Follow the steps in the project guide to enable the Ingress addon, install cert-manager, and modify your local `hosts` file to map `wisecow.local` to your Minikube IP.

**d. Create a Network Tunnel:**
To access the Ingress on Minikube, you must have the tunnel running.
```bash
minikube tunnel
```

**e. Access the Application:**
Open your browser and navigate to `https://wisecow.local`.

---
## 🔄 CI/CD Workflow

The CI/CD pipeline is defined in the `.github/workflows/ci-pipeline.yaml` file. It automatically performs the following steps on every `git push` to the `main` branch:

1.  **Checkout Code:** Checks out the latest version of the repository.
2.  **Login to Docker Hub:** Authenticates using the configured GitHub secrets.
3.  **Build and Push Image:** Builds the Docker image from the `Dockerfile` and pushes it to your Docker Hub registry.