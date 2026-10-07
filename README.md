# DevOps Assignments Repository

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**GitHub Repository:** https://github.com/ponnaganti24bcs10350-svg/devops-assignment5  

---

## 1. CI/CD & GitHub Actions (Session 16)
- **Task: Production CI/CD Demo Project:** End-to-end automated pipeline in [`10-final-cicd-pipeline/`](file:///Users/srividya/devops-assign/10-final-cicd-pipeline/).
- **Automated Testing (CI):** 100% test coverage using Jest and Supertest.
- **Optimized Packaging:** Multi-stage Dockerfile producing a minimal, secure 49.8MB container image.
- **Workflow Pipeline:** Multi-job GitHub Actions workflow in [`.github/workflows/ci-cd.yml`](file:///Users/srividya/devops-assign/.github/workflows/ci-cd.yml) (CI Test & Audit -> Build & Artifact Archival -> CD Kubernetes Zero-Downtime Deployment).
- **Full Report & Screenshots:** [CICD_GITHUB_ACTIONS_SUBMISSION.md](file:///Users/srividya/devops-assign/CICD_GITHUB_ACTIONS_SUBMISSION.md)

---

## 2. Helm Package Management (Session 15)
- **Task 1: Essential Helm Commands:** Practical execution of `create`, `install`, `list`, `status`, `get`, `upgrade`, `history`, `rollback`, `uninstall`, `repo`, and `search` in [`helm-assignments/01-helm-commands/README.md`](file:///Users/srividya/devops-assign/helm-assignments/01-helm-commands/README.md).
- **Task 2: Rollback Workflow:** Complete multi-revision lifecycle (Install -> Upgrade -> Upgrade -> Rollback) documented in [`helm-assignments/02-helm-rollback/README.md`](file:///Users/srividya/devops-assign/helm-assignments/02-helm-rollback/README.md).
- **Task 3: Production Custom Helm Chart:** Enterprise chart architecture (`webapp-chart`) with dynamic ConfigMaps/Secrets, health probes, conditional HPA, and NodePort service in [`helm-assignments/03-helm-mini-project/`](file:///Users/srividya/devops-assign/helm-assignments/03-helm-mini-project/).
- **Full Report & Screenshots:** [HELM_SUBMISSION.md](file:///Users/srividya/devops-assign/HELM_SUBMISSION.md)

---

## 3. Kubernetes Troubleshooting (Session 14)
- **Task 1: Essential Troubleshooting Commands:** Deep-dive manual for `get -o wide`, `describe`, `logs -p`, `exec`, `events`, `explain`, and `top` in [`k8s-troubleshooting/01-commands/README.md`](file:///Users/srividya/devops-assign/k8s-troubleshooting/01-commands/README.md).
- **Task 2: Common Issues Playbook:** Root Cause Analysis and remediation manifests for `CrashLoopBackOff`, `ImagePullBackOff`, `Pending`, `ContainerCreating`, `Endpoints: <none>`, DNS, and `CreateContainerConfigError` in [`k8s-troubleshooting/02-common-issues/`](file:///Users/srividya/devops-assign/k8s-troubleshooting/02-common-issues/).
- **Task 3: Production Mini-Project:** Multi-fault microservice diagnostic lab and resolution in [`k8s-troubleshooting/03-mini-project/`](file:///Users/srividya/devops-assign/k8s-troubleshooting/03-mini-project/).
- **Full Report & Screenshots:** [K8S_TROUBLESHOOTING_SUBMISSION.md](file:///Users/srividya/devops-assign/K8S_TROUBLESHOOTING_SUBMISSION.md)

---

## 4. Kubernetes Storage, HPA & Probes (Session 13)
- **Task 1: Kubernetes Volumes Guide:** Deep dive into `emptyDir`, `hostPath`, `PersistentVolume`, `PersistentVolumeClaim`, `StorageClass`, and Dynamic Provisioning in [`01-kubernetes-volumes/README.md`](file:///Users/srividya/devops-assign/01-kubernetes-volumes/README.md).
- **Task 2: HPA Hands-on:** Deployment with resource requests/limits, live CPU metrics generation, and autoscaling from 1 to 4+ replicas in [`02-hpa/`](file:///Users/srividya/devops-assign/02-hpa/).
- **Task 3: Production Mini-Project:** Multi-tier architecture featuring MySQL on dynamic PVC storage, web application with triple-tier health probes (**Startup**, **Readiness**, and **Liveness**), and HPA in [`mini-project/`](file:///Users/srividya/devops-assign/mini-project/).
- **Full Report & Screenshots:** [K8S_STORAGE_HPA_PROBES_SUBMISSION.md](file:///Users/srividya/devops-assign/K8S_STORAGE_HPA_PROBES_SUBMISSION.md)

---

## 5. Kubernetes Ingress, ConfigMaps & Secrets (Session 12)
- **Task 1: ConfigMap Demo:** Decoupled key-value pairs & properties file injected via environment variables and mounted volume.
- **Task 2: Secret Demo:** Secure credentials injection & security analysis on why Secrets must not be committed to Git.
- **Task 3: Ingress Demo:** NGINX Ingress Controller setup with path-based routing (`/apple` and `/banana`).
- **Task 4: Ingress vs Ingress Controller:** Detailed comparison guide in [`ingress-vs-controller/README.md`](file:///Users/srividya/devops-assign/ingress-vs-controller/README.md).
- **Task 5: Troubleshooting Case Study:** Root Cause Analysis (RCA) and resolution of broken service selectors in [`troubleshooting/README.md`](file:///Users/srividya/devops-assign/troubleshooting/README.md).
- **Full Report & Screenshots:** [K8S_INGRESS_CONFIGMAP_SECRETS_SUBMISSION.md](file:///Users/srividya/devops-assign/K8S_INGRESS_CONFIGMAP_SECRETS_SUBMISSION.md)

---

## 6. Kubernetes Networking & Services (Session 11)
- **Task 1: All 5 Service Types:** ClusterIP, NodePort, LoadBalancer, ExternalName, and Headless services.
- **Task 2: Workload & Object Comparisons:** Deployment vs ReplicaSet, Deployment vs DaemonSet vs StatefulSet, ReplicaSet vs Service.
- **Task 3: FQDN Guide:** In-depth guide in [`fqdn/README.md`](file:///Users/srividya/devops-assign/fqdn/README.md).
- **Task 4: CoreDNS & Service Discovery:** In-depth guide in [`coredns/README.md`](file:///Users/srividya/devops-assign/coredns/README.md).
- **Manifests Folder:** [`k8s-services/`](file:///Users/srividya/devops-assign/k8s-services/)
- **Full Report & Screenshots:** [K8S_SERVICES_NETWORKING_SUBMISSION.md](file:///Users/srividya/devops-assign/K8S_SERVICES_NETWORKING_SUBMISSION.md)

---

## 7. Kubernetes Deployment Strategies & Pod Lifecycle (Session 10)
- **4 Deployment Strategies:** Rolling Update, Blue-Green, Canary, and Recreate strategies with YAML manifests.
- **Pod Lifecycle Exploration:** Running (with liveness probes), Completed (Job/One-shot), and CrashLoopBackOff states.
- **Manifests Folder:** [`k8s-manifests/`](file:///Users/srividya/devops-assign/k8s-manifests/)
- **Full Report & Screenshots:** [K8S_DEPLOYMENTS_LIFECYCLE_SUBMISSION.md](file:///Users/srividya/devops-assign/K8S_DEPLOYMENTS_LIFECYCLE_SUBMISSION.md)

---

## 8. Kubernetes Fundamentals & Minikube Hands-on
- **Cluster Status & Minikube Configuration:** `minikube status`, `kubectl cluster-info`, `kubectl get nodes`.
- **Architecture Notes:** Control plane (`kube-apiserver`, `etcd`, `kube-scheduler`, `kube-controller-manager`) & Worker node (`kubelet`, `kube-proxy`, `container runtime`).
- **Hands-on Tutorial:** Deploying `kubernetes-bootcamp`, exposing via NodePort Service, scaling to 3 replicas, and verifying live HTTP responses.
- **Full Report & Screenshots:** [KUBERNETES_FUNDAMENTALS_SUBMISSION.md](file:///Users/srividya/devops-assign/KUBERNETES_FUNDAMENTALS_SUBMISSION.md)

---

## 9. Docker Networking & Volume Homework
- **Task 1:** Multi-tier container networking with frontend, backend (in 2 networks), and database.
- **Task 2:** Host networking with Apache HTTP Server on port 80.
- **Task 3:** Bind mount verification with live updates without container restart.
- **Task 4:** Research and architecture of Docker Overlay networks.
- **Full Report & Screenshots:** [DOCKER_NETWORKING_VOLUME_SUBMISSION.md](file:///Users/srividya/devops-assign/DOCKER_NETWORKING_VOLUME_SUBMISSION.md)

---

## 10. Docker Multi-Stage Build Homework
- **Task 1 & 2:** Multi-stage Dockerfile build, running on port 8080, and `docker ps` verification.
- **Task 3:** Multi-application deployment (Node.js, Python, Java).
- **Full Report & Screenshot:** [DOCKER_MULTISTAGE_SUBMISSION.md](file:///Users/srividya/devops-assign/DOCKER_MULTISTAGE_SUBMISSION.md)

---

## 11. Docker Hello World Applications
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

## 12. Git Homework Assignment
- **Task 1:** `git commit -a -m` vs `git commit -m` testing & comparison.
- **Task 2:** Git cherry-pick walkthrough from feature branch into `main`.
- **Full Report & Screenshots:** [GIT_HOMEWORK_SUBMISSION.md](file:///Users/srividya/devops-assign/GIT_HOMEWORK_SUBMISSION.md)
