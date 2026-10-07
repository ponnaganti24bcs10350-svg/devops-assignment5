# DevOps Assignments Repository

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**GitHub Repository:** https://github.com/ponnaganti24bcs10350-svg/devops-assignment5  

---

## 1. Kubernetes Deployment Strategies & Pod Lifecycle
- **4 Deployment Strategies:** Rolling Update, Blue-Green, Canary, and Recreate strategies with YAML manifests.
- **Pod Lifecycle Exploration:** Running (with liveness probes), Completed (Job/One-shot), and CrashLoopBackOff states.
- **Manifests Folder:** [`k8s-manifests/`](file:///Users/srividya/devops-assign/k8s-manifests/)
- **Full Report & Screenshots:** [K8S_DEPLOYMENTS_LIFECYCLE_SUBMISSION.md](file:///Users/srividya/devops-assign/K8S_DEPLOYMENTS_LIFECYCLE_SUBMISSION.md)

---

## 2. Kubernetes Fundamentals & Minikube Hands-on
- **Cluster Status & Minikube Configuration:** `minikube status`, `kubectl cluster-info`, `kubectl get nodes`.
- **Architecture Notes:** Control plane (`kube-apiserver`, `etcd`, `kube-scheduler`, `kube-controller-manager`) & Worker node (`kubelet`, `kube-proxy`, `container runtime`).
- **Hands-on Tutorial:** Deploying `kubernetes-bootcamp`, exposing via NodePort Service, scaling to 3 replicas, and verifying live HTTP responses.
- **Full Report & Screenshots:** [KUBERNETES_FUNDAMENTALS_SUBMISSION.md](file:///Users/srividya/devops-assign/KUBERNETES_FUNDAMENTALS_SUBMISSION.md)

---

## 3. Docker Networking & Volume Homework
- **Task 1:** Multi-tier container networking with frontend, backend (in 2 networks), and database.
- **Task 2:** Host networking with Apache HTTP Server on port 80.
- **Task 3:** Bind mount verification with live updates without container restart.
- **Task 4:** Research and architecture of Docker Overlay networks.
- **Full Report & Screenshots:** [DOCKER_NETWORKING_VOLUME_SUBMISSION.md](file:///Users/srividya/devops-assign/DOCKER_NETWORKING_VOLUME_SUBMISSION.md)

---

## 4. Docker Multi-Stage Build Homework
- **Task 1 & 2:** Multi-stage Dockerfile build, running on port 8080, and `docker ps` verification.
- **Task 3:** Multi-application deployment (Node.js, Python, Java).
- **Full Report & Screenshot:** [DOCKER_MULTISTAGE_SUBMISSION.md](file:///Users/srividya/devops-assign/DOCKER_MULTISTAGE_SUBMISSION.md)

---

## 5. Docker Hello World Applications
Simple Hello World web applications containerized with Docker:
- **`nodejs-app/`** - Node.js web application (Port 3000)
- **`python-app/`** - Python HTTP web application (Port 5000)
- **`java-app/`** - Java HTTP web application (Port 8080)
- **`Apache-app/`** - Apache HTTP Server (Port 80)
- **`React-app/`** - React 18 application (Port 80)
- **`nginx-app/`** - Nginx Web Server (Port 80)
- **`multistage-app/`** - Multi-stage build Go application (Port 8080)
- **Full Build & Run Guide:** [DOCKER_HOMEWORK_SUBMISSION.md](file:///Users/srividya/devops-assign/DOCKER_HOMEWORK_SUBMISSION.md)

---

## 6. Git Homework Assignment
- **Task 1:** `git commit -a -m` vs `git commit -m` testing & comparison.
- **Task 2:** Git cherry-pick walkthrough from feature branch into `main`.
- **Full Report & Screenshots:** [GIT_HOMEWORK_SUBMISSION.md](file:///Users/srividya/devops-assign/GIT_HOMEWORK_SUBMISSION.md)
