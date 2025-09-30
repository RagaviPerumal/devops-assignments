# Problem Statement 3: Runtime Security with KubeArmor

This directory contains the solution for implementing runtime security on a Kubernetes workload using **KubeArmor**.

The primary goal was to create a **zero-trust security policy** that denies all process executions by default and only allows the specific binaries required for the "Wisecow" application to function.

---
## ✨ Policy Features

* **Least Privilege:** The policy strictly adheres to the principle of least privilege, allowing only `/usr/games/fortune` and `/usr/bin/ncat`.
* **Process Blocking:** Explicitly blocks the execution of common shell utilities like `ls`, `cat`, `whoami`, etc.
* **File Access Control:** Prevents read/write access to sensitive system files, including `/etc/passwd` and `/etc/shadow`.
* **Default Deny:** All actions not explicitly allowed are blocked by default.

---
## 🛠️ Contents

* `kubearmor-policy.yaml`: The declarative KubeArmor policy manifest.
* `violation-screenshot.jpg`: A screenshot demonstrating a successful policy violation where a blocked process was denied execution.

---
## 🚀 How to Apply

1.  **Prerequisites:** Ensure you have a running Kubernetes cluster (like Minikube) with KubeArmor installed (`karmor install`).

2.  **Apply the Policy:** From the main project directory, run the following command:
    ```bash
    kubectl apply -f ./problem-statement-3/kubearmor-policy.yaml
    ```

