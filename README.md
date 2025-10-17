# Vagrant-test
# 🧱 DevOps Hackathon Project

## 🚀 Overview
This project demonstrates a complete end-to-end DevOps pipeline running entirely inside a **Vagrant VM**.  
It provisions and configures all the essential tools required to **build, test, and deploy** a simple web application into a lightweight **k3s Kubernetes cluster** using **Jenkins** as the CI/CD engine.

### 🧩 Stack Overview
| Component | Purpose |
|------------|----------|
| **Vagrant (Ubuntu)** | Spins up a clean Linux environment with all dependencies |
| **Docker** | Builds and runs containerized application images |
| **Jenkins** | Automates CI/CD pipeline execution |
| **k3s** | Lightweight single-node Kubernetes cluster for deployment |
| **Flask (Python)** | Simple sample web app |
| **GitHub** | Source control and project documentation |

---

## 📁 Folder Structure
    devops-hackathon/
        ├── Vagrantfile
        ├── README.md
        │
        ├── app.py
        ├── requirements.txt
        ├── Dockerfile
        │
        ├── jenkins/
        │ └── Jenkinsfile
        │
        ├── k3s/
        │ ├── deployment.yaml
        │ ├── service.yaml
        │ └── ingress.yaml # optional
        │
        ├── scripts/ # optional helper scripts
        │ ├── build.sh
        │ └── deploy.sh
        │
        └── docs/
        ├── DESIGN.md
        ├── TROUBLESHOOTING.md
        └── ARCHITECTURE.png # optional diagram
            




---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/devops-hackathon.git
cd devops-hackathon


 2. Launch Vagrant VM

This will automatically provision Ubuntu, install Docker, Jenkins, and k3s.

command: vagrant up

After provisioning completes:

command: vagrant ssh


3. Access Jenkins

Once Jenkins starts inside the VM:

URL: http://localhost:8080

Retrieve the admin password:

command: sudo cat /var/lib/jenkins/secrets/initialAdminPassword


Log in, install suggested plugins, and create your admin user.


🧱 Application

The web app is a simple Flask service defined in app.py.
It is containerized using the provided Dockerfile and deployed to k3s.



🔁 CI/CD Pipeline Flow

The pipeline is defined in jenkins/Jenkinsfile.

Stages

Checkout → Pull source code from GitHub

Build → Build Docker image from Dockerfile

Push → Push image to local Docker registry (or keep locally)

Deploy → Apply manifests in k3s/ using kubectl

Verify → Confirm pods and service are running


Example Jenkinsfile Snippet
pipeline {
  agent any
  environment {
    KUBECONFIG = '/var/lib/jenkins/.kube/config'
    IMAGE = 'local-flask-app:latest'
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t $IMAGE .'
      }
    }
    stage('Deploy to K3s') {
      steps {
        sh 'kubectl apply -f k3s/deployment.yaml'
        sh 'kubectl apply -f k3s/service.yaml'
      }
    }
  }
}


---

🧩 Deployment Verification

Once the pipeline completes, verify your deployment inside the VM:

kubectl get pods
kubectl get svc


If using a NodePort service:

curl http://127.0.0.1:<NodePort>


You should see your Flask app’s response.


-------


🧰 Design Decisions

Jenkins is installed directly on the VM, not inside Docker, to simplify access to Docker and k3s.

Single-node k3s provides a production-like Kubernetes environment with minimal footprint.

The Vagrantfile handles all provisioning to ensure reproducibility.

TLS and permission issues are pre-handled in Jenkins configuration using a copied kubeconfig.



-------------
🧭 Troubleshooting
Issue	Solution
permission denied for kubeconfig	Ensure /var/lib/jenkins/.kube/config has correct ownership (jenkins:jenkins)
x509: certificate invalid for IP	Use 127.0.0.1 as the Kubernetes API endpoint
Jenkins cannot run docker	Add jenkins user to docker group and restart Jenkins



