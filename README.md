# DevOps Assignments Repository

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**GitHub Repository:** https://github.com/ponnaganti24bcs10350-svg/devops-assignment5  

---

## 1. Monitoring, Observability & GitOps (Session 20)
- **Task 1: Monitoring Systems & Live Metrics Demo:** Microservice in [`monitoring-observability-gitops/01-monitoring/`](file:///Users/srividya/devops-assign/monitoring-observability-gitops/01-monitoring/) exposing Prometheus `/metrics`, `/healthz` liveness probes, CPU/Memory telemetry, structured JSON logs, and Alertmanager alert rules.
- **Task 2: Observability Architecture (The Three Pillars):** Comprehensive guide on **Metrics**, **Logs**, and **Distributed Tracing (OpenTelemetry / Jaeger)** in [`monitoring-observability-gitops/02-observability/`](file:///Users/srividya/devops-assign/monitoring-observability-gitops/02-observability/) explaining how observability solves "unknown unknowns" in cloud-native microservices.
- **Task 3: GitOps Principles & ArgoCD Continuous Reconciliation:** Declarative configuration in [`monitoring-observability-gitops/03-gitops/`](file:///Users/srividya/devops-assign/monitoring-observability-gitops/03-gitops/) covering Git as the single source of truth, pull-based synchronization, drift detection, and automated self-healing.
- **Full Report & Screenshots:** [MONITORING_OBSERVABILITY_GITOPS_SUBMISSION.md](file:///Users/srividya/devops-assign/MONITORING_OBSERVABILITY_GITOPS_SUBMISSION.md)

---

## 2. Cloud & Terraform in Action (Session 19)
- **Task: End-to-End AWS Production Cloud Infrastructure:** Full-stack Terraform infrastructure in [`terraform-cloud-infra/`](file:///Users/srividya/devops-assign/terraform-cloud-infra/) provisioning:
  - **Networking:** Custom VPC (`10.0.0.0/16`), Public Subnet (`10.0.1.0/24`), Internet Gateway, and Route Table.
  - **Security & IAM:** Ingress Security Group (HTTP/SSH) and IAM Instance Profile for credential-less S3 access.
  - **Compute:** EC2 Instance (Amazon Linux 2023) bootstrapped with automated `user_data` script running an Apache HTTP server and live infrastructure status dashboard.
  - **Storage:** S3 Bucket with SSE-S3 AES-256 encryption, versioning, public access blocks, and initial configuration object upload.
  - **Terraform Engine:** Full lifecycle coverage (`init`, `fmt`, `validate`, `plan`, `apply`, `output`, `destroy`) with explicit/implicit dependency graphs.
- **Full Report & Screenshots:** [TERRAFORM_CLOUD_ACTION_SUBMISSION.md](file:///Users/srividya/devops-assign/TERRAFORM_CLOUD_ACTION_SUBMISSION.md)

---

## 3. Terraform & Infrastructure as Code (Session 18)
- **Task 1: Terraform S3 Demo:** End-to-end Infrastructure as Code (IaC) setup in [`terraform-s3-demo/`](file:///Users/srividya/devops-assign/terraform-s3-demo/) demonstrating `init`, `fmt`, `validate`, `plan`, `apply`, `show`, `output`, and `destroy` with encryption, versioning, and public access blocks.
- **Task 2: AWS Services Research & Guides:** Five detailed architecture guides in [`aws-services/`](file:///Users/srividya/devops-assign/aws-services/):
  - [01. IAM - Governance Guide](file:///Users/srividya/devops-assign/aws-services/01-iam/README.md) (Users, Groups, Roles, Policies, Principle of Least Privilege)
  - [02. EC2 - Compute Guide](file:///Users/srividya/devops-assign/aws-services/02-ec2/README.md) (AMIs, Instance Types, Key Pairs, Security Groups, EBS, Lifecycle)
  - [03. S3 - Storage Guide](file:///Users/srividya/devops-assign/aws-services/03-s3/README.md) (Buckets, Objects, Storage Classes, Versioning, Lifecycle Rules, Encryption)
  - [04. VPC - Networking Guide](file:///Users/srividya/devops-assign/aws-services/04-vpc/README.md) (CIDRs, Subnets, Route Tables, IGW, NAT GW, Security Groups vs NACLs)
  - [05. DynamoDB & RDS - Database Services Guide](file:///Users/srividya/devops-assign/aws-services/05-dynamodb-rds/README.md) (Serverless NoSQL vs Relational Multi-AZ & Read Replicas)
- **Full Report & Screenshots:** [TERRAFORM_AWS_SUBMISSION.md](file:///Users/srividya/devops-assign/TERRAFORM_AWS_SUBMISSION.md)

---

## 4. Complete CI/CD & DevSecOps (Session 17)
- **Task: Production DevSecOps Pipeline Project:** End-to-end "Shift-Left" security pipeline in [`11-devsecops-pipeline/`](file:///Users/srividya/devops-assign/11-devsecops-pipeline/).
- **Multi-Tier Security Audits:** SAST (Semgrep), SCA (npm audit / Trivy), Secret Scanning (Gitleaks), and Container Image Scanning (Trivy).
- **Security Gates:** Automated policy enforcement failing builds on High/Critical CVEs or unencrypted secrets.
- **Runtime Hardening:** Non-root execution (`runAsNonRoot: true`, UID `10001`), read-only root filesystem, dropped capabilities, and strict `NetworkPolicy` microsegmentation.
- **Workflow Pipeline:** Multi-stage GitHub Actions workflow in [`.github/workflows/devsecops-pipeline.yml`](file:///Users/srividya/devops-assign/.github/workflows/devsecops-pipeline.yml).
- **Full Report & Screenshots:** [DEVSECOPS_SUBMISSION.md](file:///Users/srividya/devops-assign/DEVSECOPS_SUBMISSION.md)

---

## 5. CI/CD & GitHub Actions (Session 16)
- **Task: Production CI/CD Demo Project:** End-to-end automated pipeline in [`10-final-cicd-pipeline/`](file:///Users/srividya/devops-assign/10-final-cicd-pipeline/).
- **Automated Testing (CI):** 100% test coverage using Jest and Supertest.
- **Optimized Packaging:** Multi-stage Dockerfile producing a minimal, secure 49.8MB container image.
- **Workflow Pipeline:** Multi-job GitHub Actions workflow in [`.github/workflows/ci-cd.yml`](file:///Users/srividya/devops-assign/.github/workflows/ci-cd.yml) (CI Test & Audit -> Build & Artifact Archival -> CD Kubernetes Zero-Downtime Deployment).
- **Full Report & Screenshots:** [CICD_GITHUB_ACTIONS_SUBMISSION.md](file:///Users/srividya/devops-assign/CICD_GITHUB_ACTIONS_SUBMISSION.md)

---

## 6. Helm Package Management (Session 15)
- **Task 1: Essential Helm Commands:** Practical execution of `create`, `install`, `list`, `status`, `get`, `upgrade`, `history`, `rollback`, `uninstall`, `repo`, and `search` in [`helm-assignments/01-helm-commands/README.md`](file:///Users/srividya/devops-assign/helm-assignments/01-helm-commands/README.md).
- **Task 2: Rollback Workflow:** Complete multi-revision lifecycle (Install -> Upgrade -> Upgrade -> Rollback) documented in [`helm-assignments/02-helm-rollback/README.md`](file:///Users/srividya/devops-assign/helm-assignments/02-helm-rollback/README.md).
- **Task 3: Production Custom Helm Chart:** Enterprise chart architecture (`webapp-chart`) with dynamic ConfigMaps/Secrets, health probes, conditional HPA, and NodePort service in [`helm-assignments/03-helm-mini-project/`](file:///Users/srividya/devops-assign/helm-assignments/03-helm-mini-project/).
- **Full Report & Screenshots:** [HELM_SUBMISSION.md](file:///Users/srividya/devops-assign/HELM_SUBMISSION.md)

---

## 7. Kubernetes Troubleshooting (Session 14)
- **Task 1: Essential Troubleshooting Commands:** Deep-dive manual for `get -o wide`, `describe`, `logs -p`, `exec`, `events`, `explain`, and `top` in [`k8s-troubleshooting/01-commands/README.md`](file:///Users/srividya/devops-assign/k8s-troubleshooting/01-commands/README.md).
- **Task 2: Common Issues Playbook:** Root Cause Analysis and remediation manifests for `CrashLoopBackOff`, `ImagePullBackOff`, `Pending`, `ContainerCreating`, `Endpoints: <none>`, DNS, and `CreateContainerConfigError` in [`k8s-troubleshooting/02-common-issues/`](file:///Users/srividya/devops-assign/k8s-troubleshooting/02-common-issues/).
- **Task 3: Production Mini-Project:** Multi-fault microservice diagnostic lab and resolution in [`k8s-troubleshooting/03-mini-project/`](file:///Users/srividya/devops-assign/k8s-troubleshooting/03-mini-project/).
- **Full Report & Screenshots:** [K8S_TROUBLESHOOTING_SUBMISSION.md](file:///Users/srividya/devops-assign/K8S_TROUBLESHOOTING_SUBMISSION.md)

---

## 8. Kubernetes Storage, HPA & Probes (Session 13)
- **Task 1: Kubernetes Volumes Guide:** Deep dive into `emptyDir`, `hostPath`, `PersistentVolume`, `PersistentVolumeClaim`, `StorageClass`, and Dynamic Provisioning in [`01-kubernetes-volumes/README.md`](file:///Users/srividya/devops-assign/01-kubernetes-volumes/README.md).
- **Task 2: HPA Hands-on:** Deployment with resource requests/limits, live CPU metrics generation, and autoscaling from 1 to 4+ replicas in [`02-hpa/`](file:///Users/srividya/devops-assign/02-hpa/).
- **Task 3: Production Mini-Project:** Multi-tier architecture featuring MySQL on dynamic PVC storage, web application with triple-tier health probes (**Startup**, **Readiness**, and **Liveness**), and HPA in [`mini-project/`](file:///Users/srividya/devops-assign/mini-project/).
- **Full Report & Screenshots:** [K8S_STORAGE_HPA_PROBES_SUBMISSION.md](file:///Users/srividya/devops-assign/K8S_STORAGE_HPA_PROBES_SUBMISSION.md)

---

## 9. Kubernetes Ingress, ConfigMaps & Secrets (Session 12)
- **Task 1: ConfigMap Demo:** Decoupled key-value pairs & properties file injected via environment variables and mounted volume.
- **Task 2: Secret Demo:** Secure credentials injection & security analysis on why Secrets must not be committed to Git.
- **Task 3: Ingress Demo:** NGINX Ingress Controller setup with path-based routing (`/apple` and `/banana`).
- **Task 4: Ingress vs Ingress Controller:** Detailed comparison guide in [`ingress-vs-controller/README.md`](file:///Users/srividya/devops-assign/ingress-vs-controller/README.md).
- **Task 5: Troubleshooting Case Study:** Root Cause Analysis (RCA) and resolution of broken service selectors in [`troubleshooting/README.md`](file:///Users/srividya/devops-assign/troubleshooting/README.md).
- **Full Report & Screenshots:** [K8S_INGRESS_CONFIGMAP_SECRETS_SUBMISSION.md](file:///Users/srividya/devops-assign/K8S_INGRESS_CONFIGMAP_SECRETS_SUBMISSION.md)

---

## 10. Kubernetes Networking & Services (Session 11)
- **Task 1: All 5 Service Types:** ClusterIP, NodePort, LoadBalancer, ExternalName, and Headless services.
- **Task 2: Workload & Object Comparisons:** Deployment vs ReplicaSet, Deployment vs DaemonSet vs StatefulSet, ReplicaSet vs Service.
- **Task 3: FQDN Guide:** In-depth guide in [`fqdn/README.md`](file:///Users/srividya/devops-assign/fqdn/README.md).
- **Task 4: CoreDNS & Service Discovery:** In-depth guide in [`coredns/README.md`](file:///Users/srividya/devops-assign/coredns/README.md).
- **Manifests Folder:** [`k8s-services/`](file:///Users/srividya/devops-assign/k8s-services/)
- **Full Report & Screenshots:** [K8S_SERVICES_NETWORKING_SUBMISSION.md](file:///Users/srividya/devops-assign/K8S_SERVICES_NETWORKING_SUBMISSION.md)

---

## 11. Kubernetes Deployment Strategies & Pod Lifecycle (Session 10)
- **4 Deployment Strategies:** Rolling Update, Blue-Green, Canary, and Recreate strategies with YAML manifests.
- **Pod Lifecycle Exploration:** Running (with liveness probes), Completed (Job/One-shot), and CrashLoopBackOff states.
- **Manifests Folder:** [`k8s-manifests/`](file:///Users/srividya/devops-assign/k8s-manifests/)
- **Full Report & Screenshots:** [K8S_DEPLOYMENTS_LIFECYCLE_SUBMISSION.md](file:///Users/srividya/devops-assign/K8S_DEPLOYMENTS_LIFECYCLE_SUBMISSION.md)

---

## 12. Kubernetes Fundamentals & Minikube Hands-on
- **Cluster Status & Minikube Configuration:** `minikube status`, `kubectl cluster-info`, `kubectl get nodes`.
- **Architecture Notes:** Control plane (`kube-apiserver`, `etcd`, `kube-scheduler`, `kube-controller-manager`) & Worker node (`kubelet`, `kube-proxy`, `container runtime`).
- **Hands-on Tutorial:** Deploying `kubernetes-bootcamp`, exposing via NodePort Service, scaling to 3 replicas, and verifying live HTTP responses.
- **Full Report & Screenshots:** [KUBERNETES_FUNDAMENTALS_SUBMISSION.md](file:///Users/srividya/devops-assign/KUBERNETES_FUNDAMENTALS_SUBMISSION.md)

---

## 13. Docker Networking & Volume Homework
- **Task 1:** Multi-tier container networking with frontend, backend (in 2 networks), and database.
- **Task 2:** Host networking with Apache HTTP Server on port 80.
- **Task 3:** Bind mount verification with live updates without container restart.
- **Task 4:** Research and architecture of Docker Overlay networks.
- **Full Report & Screenshots:** [DOCKER_NETWORKING_VOLUME_SUBMISSION.md](file:///Users/srividya/devops-assign/DOCKER_NETWORKING_VOLUME_SUBMISSION.md)

---

## 14. Docker Multi-Stage Build Homework
- **Task 1 & 2:** Multi-stage Dockerfile build, running on port 8080, and `docker ps` verification.
- **Task 3:** Multi-application deployment (Node.js, Python, Java).
- **Full Report & Screenshot:** [DOCKER_MULTISTAGE_SUBMISSION.md](file:///Users/srividya/devops-assign/DOCKER_MULTISTAGE_SUBMISSION.md)

---

## 15. Docker Hello World Applications
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

## 16. Git Homework Assignment
- **Task 1:** `git commit -a -m` vs `git commit -m` testing & comparison.
- **Task 2:** Git cherry-pick walkthrough from feature branch into `main`.
- **Full Report & Screenshots:** [GIT_HOMEWORK_SUBMISSION.md](file:///Users/srividya/devops-assign/GIT_HOMEWORK_SUBMISSION.md)
