# DevOps Engineering Repository

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**GitHub Repository:** [ponnaganti24bcs10350-svg/devops-assignment5](https://github.com/ponnaganti24bcs10350-svg/devops-assignment5)  

---

## Repository Session Structure

This repository is structured session-by-session directly at the root, containing all homework assignments, application source codes, Dockerfiles, Kubernetes manifests, Helm charts, Terraform configurations, and CI/CD pipelines.

| Session Folder | Topic & Modules Covered | Key Deliverables & Practical Labs |
| :--- | :--- | :--- |
| [**`session5-git-github/`**](session5-git-github/) | **Git Fundamentals & Workflow** | `git commit -a -m` vs `git commit -m` testing, branch cherry-pick walkthrough & verification. |
| [**`session6-7-docker/`**](session6-7-docker/) | **Docker Apps & Multi-Stage Builds** | 6 Hello World apps (Node.js, Python, Java, Apache, React, Nginx) + Multi-stage Go build on port 8080. |
| [**`session8-docker-networking-volume/`**](session8-docker-networking-volume/) | **Docker Networking & Volumes** | Multi-tier bridge networks, dual-homed backend, host networking, live bind mounts, overlay network research. |
| [**`session9-k8s/`**](session9-k8s/) | **Kubernetes Fundamentals** | Minikube cluster setup, Control plane vs worker node architecture, deployment scaling, NodePort verification. |
| [**`session10-k8s-core-objects/`**](session10-k8s-core-objects/) | **Pods, ReplicaSets & Deployments** | 4 deployment strategies (Rolling, Blue-Green, Canary, Recreate), Pod lifecycle phases. |
| [**`session-11-kubernetes-services/`**](session-11-kubernetes-services/) | **Kubernetes Networking & Services** | 5 Service types (ClusterIP, NodePort, LoadBalancer, ExternalName, Headless), Object comparisons, FQDN & CoreDNS. |
| [**`session-12-ingress-configmaps-secrets/`**](session-12-ingress-configmaps-secrets/) | **Ingress, ConfigMaps & Secrets** | ConfigMap & Secret injection, Nginx Ingress path routing (`/apple`, `/banana`), Ingress vs Controller, RCA. |
| [**`session-13-storage-hpa-probes/`**](session-13-storage-hpa-probes/) | **Storage, HPA & Probes** | Volume types (emptyDir, hostPath, PV, PVC, StorageClass), CPU-based HPA autoscaling, 3-tier health probes. |
| [**`session-14-kubernetes-troubleshooting/`**](session-14-kubernetes-troubleshooting/) | **Kubernetes Troubleshooting** | Diagnostic commands (`describe`, `logs -p`, `events`), RCA for CrashLoopBackOff, ImagePullBackOff, Pending. |
| [**`session-15-helm/`**](session-15-helm/) | **Helm Package Management** | CLI lifecycle (`create`, `install`, `upgrade`, `history`, `rollback`), multi-revision rollback, custom chart. |
| [**`session-16-github-actions/`**](session-16-github-actions/) | **CI/CD & GitHub Actions** | Multi-job workflow with Jest testing, multi-stage container build, zero-downtime Kubernetes deployment. |
| [**`session-17-devsecops/`**](session-17-devsecops/) | **Complete CI/CD & DevSecOps** | Shift-Left pipeline: Semgrep SAST, Trivy SCA, Gitleaks Secret Scan, Trivy Container Scan, Security Gates. |
| [**`session18-terraform-iac/`**](session18-terraform-iac/) | **Terraform & IaC (AWS)** | Terraform S3 full lifecycle, 5 AWS deep dives (IAM, EC2, S3, VPC, DynamoDB & RDS). |
| [**`session19-cloud-terraform/`**](session19-cloud-terraform/) | **Cloud & Terraform in Action** | Complete AWS production stack: VPC, Subnet, Route Table, IGW, Security Group, EC2 Apache server, S3 bucket. |
| [**`session20-monitoring-observability-gitops/`**](session20-monitoring-observability-gitops/) | **Monitoring, Observability & GitOps** | Live Prometheus metrics & Alertmanager, 3 pillars of observability (Metrics, Logs, Traces), ArgoCD GitOps. |
| [**`session21-devops-capstone/`**](session21-devops-capstone/) | **Final Production Capstone Project** | End-to-end GitOps SRE Operations & Incident Platform (CloudPulse) with DevSecOps, Helm, HPA, Prometheus. |

---

## Detailed Session Workflows & Deliverables

### [`session6-7-docker/`](session6-7-docker/) - Docker Applications & Multi-Stage Builds
- **Part 1 (Session 6):** 6 Containerized web applications:
  - `nodejs-app/`: Node.js HTTP server (Port 3000)
  - `python-app/`: Python 3.11 HTTP server (Port 5000)
  - `java-app/`: Java JDK 17 HTTP server (Port 8080)
  - `Apache-app/`: Apache HTTP Server `httpd:alpine` (Port 80)
  - `React-app/`: React 18 component served with Nginx (Port 80)
  - `nginx-app/`: Nginx Web Server `nginx:alpine` (Port 80)
- **Part 2 (Session 7):** Multi-stage build Go application in `multistage-app/`:
  - Builder stage (`golang:1.21-alpine`) compiles binary; minimal runner stage (`alpine:latest`) serves on port 8080.
  - Verification: Confirmed output `Hello World from Docker multi-stage build` and captured `docker ps`.
- **Evidence:** `screenshots/05_multistage_docker_run.png`
- **Documentation:** [README in session6-7-docker](session6-7-docker/README.md)

---

### [`session8-docker-networking-volume/`](session8-docker-networking-volume/) - Docker Networking & Volumes
- **Task 1: Multi-Tier Isolation:** 3 bridge networks (`frontend-net`, `backend-net`, `db-net`) with frontend, backend (dual-homed), and database containers.
- **Task 2: Host Network:** Apache HTTP server running with `--network host` on port 80.
- **Task 3: Live Bind Mount:** Local directory `bindmount-html/` mounted to Nginx container verifying live HTML updates without restart.
- **Task 4: Overlay Network Architecture:** Documented VXLAN encapsulation and swarm multi-host routing.
- **Evidence:** `screenshots/06_task1_container_networking.png`, `screenshots/07_task2_host_network.png`, `screenshots/08_task3_bind_mount.png`
- **Documentation:** [README in session8-docker-networking-volume](session8-docker-networking-volume/README.md)

---

### [`session9-k8s/`](session9-k8s/) - Kubernetes Fundamentals & Minikube Hands-on
- **Minikube Setup:** Configured local cluster; verified status with `minikube status`, `kubectl cluster-info`, and `kubectl get nodes`.
- **Architecture Notes:** Control Plane (`kube-apiserver`, `etcd`, `kube-scheduler`, `kube-controller-manager`) & Worker Node (`kubelet`, `kube-proxy`, `container runtime`).
- **Hands-on Deployment:** Deployed `kubernetes-bootcamp`, exposed via NodePort service (port 31835), scaled to 3 replicas, and verified live HTTP responses.
- **Evidence:** `screenshots/09_k8s_cluster_status.png`, `screenshots/10_k8s_deployment_and_service.png`, `screenshots/11_k8s_scaling_and_access.png`
- **Documentation:** [README in session9-k8s](session9-k8s/README.md)

---

### [`session10-k8s-core-objects/`](session10-k8s-core-objects/) - Pods, ReplicaSets & Deployments
- **Manifests Directory:** `k8s-manifests/`
- **4 Deployment Strategies:**
  - **Rolling Update:** Zero-downtime progressive replacement (`maxSurge: 1`, `maxUnavailable: 0`).
  - **Blue-Green Deployment:** Independent parallel environments switched instantaneously via Service selector update.
  - **Canary Deployment:** Simultaneous deployment of stable (90%) and canary (10%) versions.
  - **Recreate Deployment:** Full teardown of old pods before new pods are scheduled.
- **Pod Lifecycle:** Hands-on study of Running (with liveness probe), Completed (Job one-shot), and CrashLoopBackOff diagnostic states.
- **Evidence:** `screenshots/12_k8s_rolling_update.png` through `16_k8s_pod_lifecycle.png`
- **Documentation:** [README in session10-k8s-core-objects](session10-k8s-core-objects/README.md)

---

### [`session-11-kubernetes-services/`](session-11-kubernetes-services/) - Kubernetes Networking & Services
- **Manifests Directory:** `k8s-services/`
- **5 Service Types:** ClusterIP, NodePort, LoadBalancer, ExternalName, and Headless services.
- **Object Comparisons:** Deployment vs ReplicaSet, Deployment vs DaemonSet vs StatefulSet, ReplicaSet vs Service.
- **FQDN & CoreDNS Guides:** Deep dives in `fqdn/README.md` and `coredns/README.md`.
- **Evidence:** `screenshots/17_k8s_clusterip_nodeport.png`, `screenshots/18_k8s_loadbalancer_externalname.png`, `screenshots/19_k8s_headless_service.png`
- **Documentation:** [README in session-11-kubernetes-services](session-11-kubernetes-services/README.md)

---

### [`session-12-ingress-configmaps-secrets/`](session-12-ingress-configmaps-secrets/) - Ingress, ConfigMaps & Secrets
- **Manifests Directories:** `k8s-configmaps-secrets/`, `k8s-ingress/`
- **ConfigMap & Secret:** Decoupled configurations and sensitive credentials injected via env vars and mounted volumes.
- **Path Routing:** NGINX Ingress Controller routing `/apple` and `/banana` traffic.
- **Architecture & Troubleshooting Guides:** `ingress-vs-controller/README.md` and `troubleshooting/README.md`.
- **Evidence:** `screenshots/20_k8s_configmap.png` through `23_k8s_troubleshooting.png`
- **Documentation:** [README in session-12-ingress-configmaps-secrets](session-12-ingress-configmaps-secrets/README.md)

---

### [`session-13-storage-hpa-probes/`](session-13-storage-hpa-probes/) - Storage, HPA & Probes
- **Directories:** `01-kubernetes-volumes/`, `02-hpa/`, `mini-project/`
- **Volumes Guide:** `emptyDir`, `hostPath`, `PersistentVolume`, `PersistentVolumeClaim`, `StorageClass`, and Dynamic Provisioning.
- **HPA Autoscaling:** Live CPU metrics load generation autoscaling replicas from 1 to 4+.
- **Mini-Project:** MySQL on dynamic PVC storage + Web application with Startup, Readiness, and Liveness probes.
- **Evidence:** `screenshots/24_k8s_volumes.png`, `screenshots/25_k8s_hpa_scaling.png`, `screenshots/26_k8s_probes_miniproject.png`
- **Documentation:** [README in session-13-storage-hpa-probes](session-13-storage-hpa-probes/README.md)

---

### [`session-14-kubernetes-troubleshooting/`](session-14-kubernetes-troubleshooting/) - Kubernetes Troubleshooting
- **Modules Directory:** `troubleshooting-modules/`
- **Diagnostic Commands:** `get -o wide`, `describe`, `logs -p`, `exec`, `events`, `explain`, `top`.
- **Common Issues Playbook:** Root Cause Analysis (RCA) and resolution for CrashLoopBackOff, ImagePullBackOff, Pending, DNS failure, and broken Endpoints.
- **Mini-Project:** Multi-fault microservice triage and recovery lab.
- **Evidence:** `screenshots/27_k8s_troubleshoot_commands.png` through `30_k8s_troubleshoot_miniproject.png`
- **Documentation:** [README in session-14-kubernetes-troubleshooting](session-14-kubernetes-troubleshooting/README.md)

---

### [`session-15-helm/`](session-15-helm/) - Helm Package Management
- **Modules Directory:** `helm-assignments/`
- **Commands & Lifecycle:** Hands-on practice with `create`, `install`, `upgrade`, `history`, `rollback`, `repo`, `search`.
- **Multi-Revision Rollback:** Upgrade v1 -> v2 -> rollback to v1 verification.
- **Production Chart:** Enterprise `webapp-chart` with dynamic ConfigMaps/Secrets, health probes, conditional HPA, and NodePort service.
- **Evidence:** `screenshots/31_helm_commands_repo.png` through `34_helm_miniproject.png`
- **Documentation:** [README in session-15-helm](session-15-helm/README.md)

---

### [`session-16-github-actions/`](session-16-github-actions/) - CI/CD & GitHub Actions
- **Pipeline Directory:** `10-final-cicd-pipeline/`
- **Workflow Manifest:** [`.github/workflows/ci-cd.yml`](.github/workflows/ci-cd.yml)
- **Features:** Automated Jest testing (100% pass), multi-stage Docker packaging (49.8MB), artifact archival, and zero-downtime rolling update deployment to Kubernetes.
- **Evidence:** `screenshots/35_cicd_unit_tests.png` through `38_cicd_k8s_deployment.png`
- **Documentation:** [README in session-16-github-actions](session-16-github-actions/README.md)

---

### [`session-17-devsecops/`](session-17-devsecops/) - Complete CI/CD & DevSecOps
- **Pipeline Directory:** `11-devsecops-pipeline/`
- **Workflow Manifest:** [`.github/workflows/devsecops-pipeline.yml`](.github/workflows/devsecops-pipeline.yml)
- **Shift-Left Security:**
  - SAST: Semgrep static code analysis.
  - SCA: npm audit and Trivy dependency scanning.
  - Secret Scanning: Gitleaks repository audit.
  - Container Scanning: Trivy image CVE audit with security gates.
  - Hardened Kubernetes Runtime: `runAsNonRoot: true`, read-only root filesystem, dropped capabilities, and strict NetworkPolicy.
- **Evidence:** `screenshots/39_devsecops_sast_sca.png` through `42_devsecops_pipeline_k8s.png`
- **Documentation:** [README in session-17-devsecops](session-17-devsecops/README.md)

---

### [`session18-terraform-iac/`](session18-terraform-iac/) - Terraform & IaC (AWS)
- **Directories:** `terraform-s3-demo/`, `aws-services/`
- **Terraform S3 Demo:** Full lifecycle execution (`init`, `fmt`, `validate`, `plan`, `apply`, `show`, `output`, `destroy`) with SSE-S3 AES-256 encryption, versioning, and public access blocks.
- **5 AWS Architecture Guides:** IAM Governance, EC2 Compute, S3 Storage, VPC Networking, and DynamoDB & RDS Database services.
- **Evidence:** `screenshots/43_terraform_init_plan.png` through `46_aws_services_architecture.png`
- **Documentation:** [README in session18-terraform-iac](session18-terraform-iac/README.md)

---

### [`session19-cloud-terraform/`](session19-cloud-terraform/) - Cloud & Terraform in Action
- **Project Directory:** `terraform-cloud-infra/`
- **Full-Stack AWS Infrastructure:** Custom VPC (`10.0.0.0/16`), Public Subnet (`10.0.1.0/24`), Internet Gateway, Route Table, Security Group, IAM Instance Profile, EC2 instance with user-data Apache server, and S3 bucket.
- **Evidence:** `screenshots/47_cloud_terraform_init_plan.png` through `50_cloud_terraform_destroy.png`
- **Documentation:** [README in session19-cloud-terraform](session19-cloud-terraform/README.md)

---

### [`session20-monitoring-observability-gitops/`](session20-monitoring-observability-gitops/) - Monitoring, Observability & GitOps
- **Directories:** `01-monitoring/`, `02-observability/`, `03-gitops/`
- **Monitoring:** Live Prometheus `/metrics` endpoint, health probes, CPU/Memory telemetry, JSON logs, Alertmanager rules.
- **Observability:** In-depth guide on the Three Pillars: Metrics, Structured Logs, and Distributed Tracing (OpenTelemetry / Jaeger).
- **GitOps:** Declarative configuration, continuous reconciliation, drift detection, and automated self-healing with ArgoCD.
- **Evidence:** `screenshots/51_monitoring_metrics_health.png` through `54_gitops_argocd_reconciliation.png`
- **Documentation:** [README in session20-monitoring-observability-gitops](session20-monitoring-observability-gitops/README.md)

---

### [`session21-devops-capstone/`](session21-devops-capstone/) - Final Production Capstone Project
- **Project Directory:** `final-devops-project/`
- **CloudPulse Platform:** Live incident response and SRE operations platform at `http://localhost:3000`.
- **Integrated Architecture:** Complete DevSecOps pipeline, enterprise Helm chart with HPA autoscaling, Prometheus observability, and ArgoCD continuous reconciliation.
- **Evidence:** `screenshots/55_final_devsecops_pipeline.png` through `58_final_gitops_troubleshooting.png`
- **Documentation:** [README in session21-devops-capstone](session21-devops-capstone/README.md)

---

### [`session5-git-github/`](session5-git-github/) - Git Homework Assignment
- **Task 1:** `git commit -a -m` vs `git commit -m` testing & comparison.
- **Task 2:** Git cherry-pick walkthrough from feature branch into `main`.
- **Evidence:** `screenshots/01_task1_commit_comparison.png` through `04_task2_cherry_pick_and_verification.png`
- **Documentation:** [README in session5-git-github](session5-git-github/README.md)

---

*Repository maintained and documented by Srividya Ponnaganti (Enrollment No: 24BCS10350)*
