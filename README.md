# DevOps Engineering Assignments Repository

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**GitHub Repository:** [ponnaganti24bcs10350-svg/devops-assignment5](https://github.com/ponnaganti24bcs10350-svg/devops-assignment5)  

---

## Master Session Index (Session 06 - Session 20)

All homework tasks and session projects are organized into dedicated folders under [`sessions/`](sessions/) as well as comprehensive root reports.

| Session | Topic | Key Deliverables & Practical Labs | Dedicated Session Folder | Full Report |
| :--- | :--- | :--- | :--- | :--- |
| **Session 06** | **Docker Hello World Apps** | 6 containerized web apps: Node.js, Python, Java, Apache, React, Nginx | [`sessions/session-06`](sessions/session-06-docker-hello-world/README.md) | [DOCKER_HOMEWORK_SUBMISSION.md](DOCKER_HOMEWORK_SUBMISSION.md) |
| **Session 07** | **Docker Multi-Stage Build** | Multi-stage Go build, minimal Alpine final image, port 8080 verification, 3-app deployment | [`sessions/session-07`](sessions/session-07-docker-multistage-build/README.md) | [DOCKER_MULTISTAGE_SUBMISSION.md](DOCKER_MULTISTAGE_SUBMISSION.md) |
| **Session 08** | **Docker Networking & Volumes** | Multi-tier bridge networks, dual-homed backend, host networking, live bind mounts, Overlay network research | [`sessions/session-08`](sessions/session-08-docker-networking-volumes/README.md) | [DOCKER_NETWORKING_VOLUME_SUBMISSION.md](DOCKER_NETWORKING_VOLUME_SUBMISSION.md) |
| **Session 09** | **Kubernetes Fundamentals** | Minikube setup, Control Plane vs Worker Node architecture, deployment scaling, NodePort verification | [`sessions/session-09`](sessions/session-09-kubernetes-fundamentals/README.md) | [KUBERNETES_FUNDAMENTALS_SUBMISSION.md](KUBERNETES_FUNDAMENTALS_SUBMISSION.md) |
| **Session 10** | **Pods, ReplicaSets & Deployments** | 4 deployment strategies (Rolling, Blue-Green, Canary, Recreate), Pod lifecycle phases | [`sessions/session-10`](sessions/session-10-k8s-pods-replicasets-deployments/README.md) | [K8S_DEPLOYMENTS_LIFECYCLE_SUBMISSION.md](K8S_DEPLOYMENTS_LIFECYCLE_SUBMISSION.md) |
| **Session 11** | **Networking & Services** | 5 Service types (ClusterIP, NodePort, LoadBalancer, ExternalName, Headless), Object comparisons, FQDN & CoreDNS | [`sessions/session-11`](sessions/session-11-k8s-networking-services/README.md) | [K8S_SERVICES_NETWORKING_SUBMISSION.md](K8S_SERVICES_NETWORKING_SUBMISSION.md) |
| **Session 12** | **Ingress, ConfigMaps & Secrets** | ConfigMap & Secret injection, Nginx Ingress path routing (`/apple`, `/banana`), Ingress vs Controller, RCA | [`sessions/session-12`](sessions/session-12-k8s-ingress-configmaps-secrets/README.md) | [K8S_INGRESS_CONFIGMAP_SECRETS_SUBMISSION.md](K8S_INGRESS_CONFIGMAP_SECRETS_SUBMISSION.md) |
| **Session 13** | **Storage, HPA & Probes** | Volume types (emptyDir, hostPath, PV, PVC, StorageClass), CPU-based HPA autoscaling, 3-tier health probes | [`sessions/session-13`](sessions/session-13-k8s-storage-hpa-probes/README.md) | [K8S_STORAGE_HPA_PROBES_SUBMISSION.md](K8S_STORAGE_HPA_PROBES_SUBMISSION.md) |
| **Session 14** | **Kubernetes Troubleshooting** | Diagnostic commands (`describe`, `logs -p`, `events`), RCA for CrashLoopBackOff, ImagePullBackOff, Pending | [`sessions/session-14`](sessions/session-14-k8s-troubleshooting/README.md) | [K8S_TROUBLESHOOTING_SUBMISSION.md](K8S_TROUBLESHOOTING_SUBMISSION.md) |
| **Session 15** | **Helm Package Management** | CLI lifecycle (`create`, `install`, `upgrade`, `history`, `rollback`), multi-revision rollback, custom chart | [`sessions/session-15`](sessions/session-15-helm/README.md) | [HELM_SUBMISSION.md](HELM_SUBMISSION.md) |
| **Session 16** | **CI/CD & GitHub Actions** | Multi-job workflow with Jest testing, multi-stage container build, zero-downtime Kubernetes deployment | [`sessions/session-16`](sessions/session-16-cicd-github-actions/README.md) | [CICD_GITHUB_ACTIONS_SUBMISSION.md](CICD_GITHUB_ACTIONS_SUBMISSION.md) |
| **Session 17** | **Complete CI/CD & DevSecOps** | Shift-Left pipeline: Semgrep SAST, Trivy SCA, Gitleaks Secret Scan, Trivy Container Scan, Security Gates | [`sessions/session-17`](sessions/session-17-cicd-devsecops/README.md) | [DEVSECOPS_SUBMISSION.md](DEVSECOPS_SUBMISSION.md) |
| **Session 18** | **Terraform & IaC (AWS)** | Terraform S3 full lifecycle, 5 AWS deep dives (IAM, EC2, S3, VPC, DynamoDB & RDS) | [`sessions/session-18`](sessions/session-18-terraform-iac-aws/README.md) | [TERRAFORM_AWS_SUBMISSION.md](TERRAFORM_AWS_SUBMISSION.md) |
| **Session 19** | **Cloud & Terraform in Action** | Complete AWS production stack: VPC, Subnet, Route Table, IGW, Security Group, EC2 Apache server, S3 bucket | [`sessions/session-19`](sessions/session-19-cloud-terraform-action/README.md) | [TERRAFORM_CLOUD_ACTION_SUBMISSION.md](TERRAFORM_CLOUD_ACTION_SUBMISSION.md) |
| **Session 20** | **Monitoring, Observability & GitOps** | Live Prometheus metrics & Alertmanager, 3 pillars of observability (Metrics, Logs, Traces), ArgoCD GitOps | [`sessions/session-20`](sessions/session-20-monitoring-observability-gitops/README.md) | [MONITORING_OBSERVABILITY_GITOPS_SUBMISSION.md](MONITORING_OBSERVABILITY_GITOPS_SUBMISSION.md) |
| **Capstone** | **Final Production Project** | End-to-end GitOps SRE Operations & Incident Platform (CloudPulse) with DevSecOps, Helm, HPA, Prometheus | [`final-devops-project`](final-devops-project/) | [FINAL_DEVOPS_PROJECT_SUBMISSION.md](FINAL_DEVOPS_PROJECT_SUBMISSION.md) |

---

## Detailed Session Workflows & Deliverables

### Session 06: Docker Hello World Applications
- **Application Folders:**
  - [`nodejs-app/`](nodejs-app/): Node.js HTTP server (Port 3000)
  - [`python-app/`](python-app/): Python 3.11 HTTP server (Port 5000)
  - [`java-app/`](java-app/): Java JDK 17 HTTP server (Port 8080)
  - [`Apache-app/`](Apache-app/): Apache HTTP Server `httpd:alpine` (Port 80)
  - [`React-app/`](React-app/): React 18 component served with Nginx (Port 80)
  - [`nginx-app/`](nginx-app/): Nginx Web Server `nginx:alpine` (Port 80)
- **Key Tasks:** Built Dockerfiles for each stack, ran standalone containers, and verified that "Hello World" is rendered in a web browser.
- **Dedicated Documentation:** [`sessions/session-06-docker-hello-world/README.md`](sessions/session-06-docker-hello-world/README.md)
- **Root Report:** [DOCKER_HOMEWORK_SUBMISSION.md](DOCKER_HOMEWORK_SUBMISSION.md)

---

### Session 07: Docker Multi-Stage Build Homework
- **Application Folder:** [`multistage-app/`](multistage-app/)
- **Task 1: Run Multi-Stage Dockerfile:** Built Go application using a builder stage (`golang:1.21-alpine`) and copied only the minimal binary into a production final stage (`alpine:latest`), reducing image footprint and attack surface.
- **Task 2: Verification & Documentation:** Confirmed container runs on port 8080, verified output displays `Hello World from Docker multi-stage build`, and captured `docker ps`.
- **Task 3: Docker Application Deployment:** Multi-application deployment covering Node.js, Python, and Java.
- **Evidence:** `screenshots/05_multistage_docker_run.png`
- **Dedicated Documentation:** [`sessions/session-07-docker-multistage-build/README.md`](sessions/session-07-docker-multistage-build/README.md)
- **Root Report:** [DOCKER_MULTISTAGE_SUBMISSION.md](DOCKER_MULTISTAGE_SUBMISSION.md)

---

### Session 08: Docker Networking & Volume Homework Tasks
- **Task 1: Docker Container Networking:** Created 3 isolated user-defined bridge networks (`frontend-net`, `backend-net`, `db-net`) and 3 containers (`frontend-svc`, `backend-svc`, `db-svc`). Attached `backend-svc` to both frontend and backend networks to allow controlled multi-tier communication while keeping the database fully isolated.
- **Task 2: Host Network:** Ran Apache2 with `--network host` and accessed the web application directly on host port 80.
- **Task 3: Bind Mount:** Created local directory [`bindmount-html/`](bindmount-html/) with `index.html` mounted into an Nginx container. Demonstrated live updates without restarting the container.
- **Task 4: Overlay Network Architecture:** Documented VXLAN encapsulation, swarm manager control plane (port 2377/tcp), and cross-host multi-node container communication.
- **Evidence:** `screenshots/06_task1_container_networking.png`, `screenshots/07_task2_host_network.png`, `screenshots/08_task3_bind_mount.png`
- **Dedicated Documentation:** [`sessions/session-08-docker-networking-volumes/README.md`](sessions/session-08-docker-networking-volumes/README.md)
- **Root Report:** [DOCKER_NETWORKING_VOLUME_SUBMISSION.md](DOCKER_NETWORKING_VOLUME_SUBMISSION.md)

---

### Session 09: Kubernetes Fundamentals & Minikube Hands-on
- **Cluster Status & Minikube Setup:** Configured local Minikube cluster and verified node readiness using `minikube status`, `kubectl cluster-info`, and `kubectl get nodes`.
- **Kubernetes Architecture:** Comprehensive documentation of Control Plane components (`kube-apiserver`, `etcd`, `kube-scheduler`, `kube-controller-manager`) and Worker Node components (`kubelet`, `kube-proxy`, `container runtime`).
- **Hands-on Bootcamp Deployment:** Deployed `kubernetes-bootcamp`, exposed via NodePort Service on port 31835, scaled to 3 replicas, and verified HTTP load distribution across pods.
- **Evidence:** `screenshots/09_k8s_cluster_status.png`, `screenshots/10_k8s_deployment_and_service.png`, `screenshots/11_k8s_scaling_and_access.png`
- **Dedicated Documentation:** [`sessions/session-09-kubernetes-fundamentals/README.md`](sessions/session-09-kubernetes-fundamentals/README.md)
- **Root Report:** [KUBERNETES_FUNDAMENTALS_SUBMISSION.md](KUBERNETES_FUNDAMENTALS_SUBMISSION.md)

---

### Session 10: Kubernetes Pods, ReplicaSets & Deployments
- **Manifests Directory:** [`k8s-manifests/`](k8s-manifests/)
- **Task 1: 4 Deployment Strategies:**
  - **Rolling Update:** Zero-downtime progressive replacement with `maxSurge: 1` and `maxUnavailable: 0`.
  - **Blue-Green Deployment:** Independent parallel environments switched instantaneously via Service selector update.
  - **Canary Deployment:** Simultaneous deployment of stable (90%) and canary (10%) versions sharing the same label selector.
  - **Recreate Deployment:** Strict teardown of all old pods before new pods are scheduled (`strategy: Recreate`).
- **Task 2: Pod Lifecycle:** Hands-on study of Running (with liveness probes), Completed (Job one-shot execution), and CrashLoopBackOff diagnostic states.
- **Evidence:** `screenshots/12_k8s_rolling_update.png` through `16_k8s_pod_lifecycle.png`
- **Dedicated Documentation:** [`sessions/session-10-k8s-pods-replicasets-deployments/README.md`](sessions/session-10-k8s-pods-replicasets-deployments/README.md)
- **Root Report:** [K8S_DEPLOYMENTS_LIFECYCLE_SUBMISSION.md](K8S_DEPLOYMENTS_LIFECYCLE_SUBMISSION.md)

---

### Session 11: Kubernetes Networking & Services
- **Manifests Directory:** [`k8s-services/`](k8s-services/)
- **Task 1: All 5 Kubernetes Service Types:**
  - `ClusterIP`: Internal stable virtual IP with kube-proxy iptables load balancing.
  - `NodePort`: Exposing static port (30000-32767) across all cluster node interfaces.
  - `LoadBalancer`: Cloud-native public IP provisioning with external load balancer integration.
  - `ExternalName`: CNAME redirection for external endpoints without proxying.
  - `Headless`: Service with `clusterIP: None` returning direct pod A/AAAA records for stateful sets.
- **Task 2: Object Comparisons:** Deployment vs ReplicaSet, Deployment vs DaemonSet vs StatefulSet, ReplicaSet vs Service.
- **Task 3: FQDN Guide:** Deep dive in [`fqdn/README.md`](fqdn/README.md) on Kubernetes DNS hierarchy (`<service>.<namespace>.svc.cluster.local`).
- **Task 4: CoreDNS Guide:** Deep dive in [`coredns/README.md`](coredns/README.md) on Corefile configuration, query caching, forwarders, and DNS troubleshooting.
- **Evidence:** `screenshots/17_k8s_clusterip_nodeport.png`, `screenshots/18_k8s_loadbalancer_externalname.png`, `screenshots/19_k8s_headless_service.png`
- **Dedicated Documentation:** [`sessions/session-11-k8s-networking-services/README.md`](sessions/session-11-k8s-networking-services/README.md)
- **Root Report:** [K8S_SERVICES_NETWORKING_SUBMISSION.md](K8S_SERVICES_NETWORKING_SUBMISSION.md)

---

### Session 12: Kubernetes Ingress, ConfigMaps & Secrets
- **Manifests Directories:** [`k8s-configmaps-secrets/`](k8s-configmaps-secrets/), [`k8s-ingress/`](k8s-ingress/)
- **Task 1: ConfigMap Demo:** Decoupled key-value pairs & properties file injected via environment variables and mounted volume.
- **Task 2: Secret Demo:** Secure credentials injection & security analysis on why Secrets must not be committed to Git.
- **Task 3: Ingress Demo:** NGINX Ingress Controller setup with path-based routing (`/apple` and `/banana`).
- **Task 4: Ingress vs Ingress Controller:** Detailed comparison guide in [`ingress-vs-controller/README.md`](ingress-vs-controller/README.md).
- **Task 5: Troubleshooting Case Study:** Root Cause Analysis (RCA) and resolution of broken service selectors in [`troubleshooting/README.md`](troubleshooting/README.md).
- **Evidence:** `screenshots/20_k8s_configmap.png` through `23_k8s_troubleshooting.png`
- **Dedicated Documentation:** [`sessions/session-12-k8s-ingress-configmaps-secrets/README.md`](sessions/session-12-k8s-ingress-configmaps-secrets/README.md)
- **Root Report:** [K8S_INGRESS_CONFIGMAP_SECRETS_SUBMISSION.md](K8S_INGRESS_CONFIGMAP_SECRETS_SUBMISSION.md)

---

### Session 13: Kubernetes Storage, HPA & Probes
- **Directories:** [`01-kubernetes-volumes/`](01-kubernetes-volumes/), [`02-hpa/`](02-hpa/), [`mini-project/`](mini-project/)
- **Task 1: Kubernetes Volumes Guide:** Deep dive into `emptyDir`, `hostPath`, `PersistentVolume`, `PersistentVolumeClaim`, `StorageClass`, and Dynamic Provisioning in [`01-kubernetes-volumes/README.md`](01-kubernetes-volumes/README.md).
- **Task 2: HPA Hands-on:** Deployment with resource requests/limits, live CPU metrics generation, and autoscaling from 1 to 4+ replicas in [`02-hpa/`](02-hpa/).
- **Task 3: Production Mini-Project:** Multi-tier architecture featuring MySQL on dynamic PVC storage, web application with triple-tier health probes (**Startup**, **Readiness**, and **Liveness**), and HPA in [`mini-project/`](mini-project/).
- **Evidence:** `screenshots/24_k8s_volumes.png`, `screenshots/25_k8s_hpa_scaling.png`, `screenshots/26_k8s_probes_miniproject.png`
- **Dedicated Documentation:** [`sessions/session-13-k8s-storage-hpa-probes/README.md`](sessions/session-13-k8s-storage-hpa-probes/README.md)
- **Root Report:** [K8S_STORAGE_HPA_PROBES_SUBMISSION.md](K8S_STORAGE_HPA_PROBES_SUBMISSION.md)

---

### Session 14: Kubernetes Troubleshooting
- **Directories:** [`k8s-troubleshooting/01-commands/`](k8s-troubleshooting/01-commands/), [`k8s-troubleshooting/02-common-issues/`](k8s-troubleshooting/02-common-issues/), [`k8s-troubleshooting/03-mini-project/`](k8s-troubleshooting/03-mini-project/)
- **Task 1: Essential Troubleshooting Commands:** Deep-dive manual for `get -o wide`, `describe`, `logs -p`, `exec`, `events`, `explain`, and `top`.
- **Task 2: Common Issues Playbook:** Root Cause Analysis and remediation manifests for `CrashLoopBackOff`, `ImagePullBackOff`, `Pending`, `ContainerCreating`, `Endpoints: <none>`, DNS, and `CreateContainerConfigError`.
- **Task 3: Production Mini-Project:** Multi-fault microservice diagnostic lab and resolution in [`k8s-troubleshooting/03-mini-project/`](k8s-troubleshooting/03-mini-project/).
- **Evidence:** `screenshots/27_k8s_troubleshoot_commands.png` through `30_k8s_troubleshoot_miniproject.png`
- **Dedicated Documentation:** [`sessions/session-14-k8s-troubleshooting/README.md`](sessions/session-14-k8s-troubleshooting/README.md)
- **Root Report:** [K8S_TROUBLESHOOTING_SUBMISSION.md](K8S_TROUBLESHOOTING_SUBMISSION.md)

---

### Session 15: Helm Package Management
- **Directories:** [`helm-assignments/01-helm-commands/`](helm-assignments/01-helm-commands/), [`helm-assignments/02-helm-rollback/`](helm-assignments/02-helm-rollback/), [`helm-assignments/03-helm-mini-project/`](helm-assignments/03-helm-mini-project/)
- **Task 1: Essential Helm Commands:** Practical execution of `create`, `install`, `list`, `status`, `get`, `upgrade`, `history`, `rollback`, `uninstall`, `repo`, and `search`.
- **Task 2: Rollback Workflow:** Complete multi-revision lifecycle (Install -> Upgrade -> Upgrade -> Rollback) documented in [`helm-assignments/02-helm-rollback/README.md`](helm-assignments/02-helm-rollback/README.md).
- **Task 3: Production Custom Helm Chart:** Enterprise chart architecture (`webapp-chart`) with dynamic ConfigMaps/Secrets, health probes, conditional HPA, and NodePort service.
- **Evidence:** `screenshots/31_helm_commands_repo.png` through `34_helm_miniproject.png`
- **Dedicated Documentation:** [`sessions/session-15-helm/README.md`](sessions/session-15-helm/README.md)
- **Root Report:** [HELM_SUBMISSION.md](HELM_SUBMISSION.md)

---

### Session 16: CI/CD & GitHub Actions
- **Project Directory:** [`10-final-cicd-pipeline/`](10-final-cicd-pipeline/)
- **Workflow Manifest:** [`.github/workflows/ci-cd.yml`](.github/workflows/ci-cd.yml)
- **Task: Production CI/CD Demo Project:** End-to-end automated pipeline featuring:
  - **CI Phase:** 100% test coverage using Jest and Supertest, security vulnerability audits.
  - **Packaging Phase:** Multi-stage Dockerfile producing a minimal 49.8MB container image.
  - **CD Phase:** Kubernetes zero-downtime rolling update deployment with rollout status verification.
- **Evidence:** `screenshots/35_cicd_unit_tests.png` through `38_cicd_k8s_deployment.png`
- **Dedicated Documentation:** [`sessions/session-16-cicd-github-actions/README.md`](sessions/session-16-cicd-github-actions/README.md)
- **Root Report:** [CICD_GITHUB_ACTIONS_SUBMISSION.md](CICD_GITHUB_ACTIONS_SUBMISSION.md)

---

### Session 17: Complete CI/CD & DevSecOps
- **Project Directory:** [`11-devsecops-pipeline/`](11-devsecops-pipeline/)
- **Workflow Manifest:** [`.github/workflows/devsecops-pipeline.yml`](.github/workflows/devsecops-pipeline.yml)
- **Task: Production DevSecOps Pipeline Project:** End-to-end "Shift-Left" security pipeline:
  - **SAST:** Static Application Security Testing via Semgrep.
  - **SCA:** Software Composition Analysis via `npm audit` and Trivy vulnerability scanner.
  - **Secret Scanning:** Repository and commit history scanning via Gitleaks.
  - **Container Image Scanning:** Full CVE image scan via Trivy with severity gating.
  - **Runtime Hardening:** Non-root execution (`runAsNonRoot: true`, UID `10001`), read-only root filesystem, dropped capabilities, and strict `NetworkPolicy` microsegmentation.
- **Evidence:** `screenshots/39_devsecops_sast_sca.png` through `42_devsecops_pipeline_k8s.png`
- **Dedicated Documentation:** [`sessions/session-17-cicd-devsecops/README.md`](sessions/session-17-cicd-devsecops/README.md)
- **Root Report:** [DEVSECOPS_SUBMISSION.md](DEVSECOPS_SUBMISSION.md)

---

### Session 18: Terraform & Infrastructure as Code
- **Directories:** [`terraform-s3-demo/`](terraform-s3-demo/), [`aws-services/`](aws-services/)
- **Task 1: Terraform S3 Demo:** End-to-end Infrastructure as Code (IaC) setup demonstrating `init`, `fmt`, `validate`, `plan`, `apply`, `show`, `output`, and `destroy` with encryption, versioning, and public access blocks.
- **Task 2: AWS Services Research & Guides:** Five detailed architecture guides in [`aws-services/`](aws-services/):
  - [01. IAM - Governance Guide](aws-services/01-iam/README.md) (Users, Groups, Roles, Policies, Principle of Least Privilege)
  - [02. EC2 - Compute Guide](aws-services/02-ec2/README.md) (AMIs, Instance Types, Key Pairs, Security Groups, EBS, Lifecycle)
  - [03. S3 - Storage Guide](aws-services/03-s3/README.md) (Buckets, Objects, Storage Classes, Versioning, Lifecycle Rules, Encryption)
  - [04. VPC - Networking Guide](aws-services/04-vpc/README.md) (CIDRs, Subnets, Route Tables, IGW, NAT GW, Security Groups vs NACLs)
  - [05. DynamoDB & RDS - Database Services Guide](aws-services/05-dynamodb-rds/README.md) (Serverless NoSQL vs Relational Multi-AZ & Read Replicas)
- **Evidence:** `screenshots/43_terraform_init_plan.png` through `46_aws_services_architecture.png`
- **Dedicated Documentation:** [`sessions/session-18-terraform-iac-aws/README.md`](sessions/session-18-terraform-iac-aws/README.md)
- **Root Report:** [TERRAFORM_AWS_SUBMISSION.md](TERRAFORM_AWS_SUBMISSION.md)

---

### Session 19: Cloud & Terraform in Action
- **Project Directory:** [`terraform-cloud-infra/`](terraform-cloud-infra/)
- **Task: End-to-End AWS Production Cloud Infrastructure:** Full-stack Terraform infrastructure provisioning:
  - **Networking:** Custom VPC (`10.0.0.0/16`), Public Subnet (`10.0.1.0/24`), Internet Gateway, and Route Table.
  - **Security & IAM:** Ingress Security Group (HTTP/SSH) and IAM Instance Profile for credential-less S3 access.
  - **Compute:** EC2 Instance (Amazon Linux 2023) bootstrapped with automated `user_data` script running an Apache HTTP server and live infrastructure status dashboard.
  - **Storage:** S3 Bucket with SSE-S3 AES-256 encryption, versioning, public access blocks, and initial configuration object upload.
  - **Terraform Engine:** Full lifecycle coverage (`init`, `fmt`, `validate`, `plan`, `apply`, `output`, `destroy`) with explicit/implicit dependency graphs.
- **Evidence:** `screenshots/47_cloud_terraform_init_plan.png` through `50_cloud_terraform_destroy.png`
- **Dedicated Documentation:** [`sessions/session-19-cloud-terraform-action/README.md`](sessions/session-19-cloud-terraform-action/README.md)
- **Root Report:** [TERRAFORM_CLOUD_ACTION_SUBMISSION.md](TERRAFORM_CLOUD_ACTION_SUBMISSION.md)

---

### Session 20: Monitoring, Observability & GitOps
- **Project Directory:** [`monitoring-observability-gitops/`](monitoring-observability-gitops/)
- **Task 1: Monitoring Systems & Live Metrics Demo:** Microservice in [`01-monitoring/`](monitoring-observability-gitops/01-monitoring/) exposing Prometheus `/metrics`, `/healthz` liveness probes, CPU/Memory telemetry, structured JSON logs, and Alertmanager alert rules.
- **Task 2: Observability Architecture (The Three Pillars):** Comprehensive guide on **Metrics**, **Logs**, and **Distributed Tracing (OpenTelemetry / Jaeger)** in [`02-observability/`](monitoring-observability-gitops/02-observability/) explaining how observability solves "unknown unknowns" in cloud-native microservices.
- **Task 3: GitOps Principles & ArgoCD Continuous Reconciliation:** Declarative configuration in [`03-gitops/`](monitoring-observability-gitops/03-gitops/) covering Git as the single source of truth, pull-based synchronization, drift detection, and automated self-healing.
- **Evidence:** `screenshots/51_monitoring_metrics_health.png` through `54_gitops_argocd_reconciliation.png`
- **Dedicated Documentation:** [`sessions/session-20-monitoring-observability-gitops/README.md`](sessions/session-20-monitoring-observability-gitops/README.md)
- **Root Report:** [MONITORING_OBSERVABILITY_GITOPS_SUBMISSION.md](MONITORING_OBSERVABILITY_GITOPS_SUBMISSION.md)

---

### Capstone: Production Cloud-Native SRE Operations & Incident Platform
- **Project Directory:** [`final-devops-project/`](final-devops-project/)
- **Application:** CloudPulse SRE Operations & Incident Platform running live at `http://localhost:3000`.
- **Integrated Pillars:**
  1. Automated DevSecOps Pipeline (SAST, SCA, Gitleaks, Trivy).
  2. Enterprise Helm Chart with Dynamic Autoscaling (HPA) and Triple-Tier Probes.
  3. Live Observability (Prometheus Metrics & Health Probes).
  4. GitOps Continuous Reconciliation & Zero-Downtime Rollouts.
- **Evidence:** `screenshots/55_final_devsecops_pipeline.png` through `58_final_gitops_troubleshooting.png`
- **Full Capstone Report:** [FINAL_DEVOPS_PROJECT_SUBMISSION.md](FINAL_DEVOPS_PROJECT_SUBMISSION.md)

---

### Prerequisite / Foundational: Git Homework Assignment
- **Task 1:** `git commit -a -m` vs `git commit -m` testing & comparison.
- **Task 2:** Git cherry-pick walkthrough from feature branch into `main`.
- **Evidence:** `screenshots/01_task1_commit_comparison.png` through `04_task2_cherry_pick_and_verification.png`
- **Report:** [GIT_HOMEWORK_SUBMISSION.md](GIT_HOMEWORK_SUBMISSION.md)

---

*Repository maintained and documented by Srividya Ponnaganti (Enrollment No: 24BCS10350)*
