# End-to-End DevOps Project: Kubernetes, CI/CD, and Python Scripting

This repository showcases a comprehensive DevOps project demonstrating a complete software lifecycle, from containerization and automated deployment to runtime security and health monitoring.

---
## ✨ Key Features

* **CI/CD Automation:** An automated pipeline using **GitHub Actions** to build and push Docker images.
* **Containerization:** A web application containerized with **Docker**.
* **Kubernetes Deployment:** Full deployment on a Kubernetes cluster using **Deployments**, **Services**, and an **Ingress** for secure access.
* **Runtime Security:** A zero-trust security policy implemented with **KubeArmor** to protect the running application.
* **System Monitoring:** Custom **Python scripts** for monitoring system health and application endpoints.

---
## 🛠️ Technologies Used

-   **CI/CD:** GitHub Actions
-   **Containerization:** Docker
-   **Orchestration:** Kubernetes (Minikube)
-   **Security:** KubeArmor
-   **Scripting:** Python
-   **Version Control:** Git & GitHub
-   **Configuration:** YAML

---
## 📂 Project Structure

This project is organized into folders based on the problem statements:

* **/problem-statement-1/**: Contains all Kubernetes manifests for deploying the "Wisecow" web application. This includes the `Dockerfile`, `deployment.yaml`, `service.yaml`, and `ingress.yaml` files.

* **/problem-statement-2/**: Includes two Python scripts:
    * `system-health-monitor`: A script to monitor system resources like CPU, disk, and memory.
    * `application-health-checker`: A script to periodically check the health of a given application endpoint.
    * *See the README inside this folder for detailed usage instructions.*

* **/problem-statement-3/**: Contains the `kubearmor-policy.yaml`, a zero-trust KubeArmor policy designed to secure the running workload by restricting process execution and file access. A screenshot demonstrating a policy violation is also included.
