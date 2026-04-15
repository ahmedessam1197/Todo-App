# DevSecOps Todo Application

A production-style Todo application demonstrating a complete DevSecOps pipeline using modern cloud-native technologies.

The project showcases how a simple Flask application can be containerized, scanned for vulnerabilities, deployed to Kubernetes, and continuously delivered using GitOps practices.

---

# Project Architecture

Developer → GitHub → Jenkins CI → Docker Build → Trivy Security Scan → DockerHub → ArgoCD → Kubernetes Cluster → Prometheus & Grafana Monitoring

---

# Tech Stack

**Application**

* Python Flask
* SQL Server

**Containerization**

* Docker

**Container Orchestration**

* Kubernetes (Minikube)

**CI/CD**

* Jenkins

**Security**

* Trivy container vulnerability scanning

**GitOps**

* ArgoCD

**Monitoring**

* Prometheus
* Grafana

---

# CI/CD Pipeline

1. Developer pushes code to GitHub
2. Jenkins pipeline triggers automatically
3. Docker image is built
4. Image scanned using Trivy
5. Secure image pushed to DockerHub
6. Kubernetes manifests updated
7. ArgoCD syncs deployment automatically

---

# Kubernetes Deployment

Application is deployed using:

* Deployment
* Service
* Secrets
* Horizontal Pod Autoscaler (HPA)
* Ingress

Features implemented:

* Resource limits
* Liveness & Readiness probes
* Secure environment variables
* Auto scaling

---

# Monitoring

Cluster monitoring is implemented using:

* Prometheus for metrics collection
* Grafana for visualization dashboards

Metrics monitored:

* CPU usage
* Memory usage
* Pod health
* Cluster performance

---

# How to Run the Project

Clone the repository

```
git clone https://github.com/ahmedessam1197/Todo-App.git
```

Build Docker image

```
docker build -t todo-app .
```

Run with Docker

```
docker run -p 5000:5000 todo-app
```

Deploy to Kubernetes

```
kubectl apply -f Kubernetes/
```

---

# DevSecOps Concepts Demonstrated

* CI/CD Pipeline
* Container Security Scanning
* Infrastructure as Code
* GitOps Deployment
* Kubernetes Best Practices
* Cloud Native Monitoring

---

# Future Improvements

* Helm charts
* Terraform infrastructure
* Kubernetes RBAC
* Alertmanager notifications
* Production cloud deployment (AWS / Azure / GCP)

---

# Author

Ahmed Essam
