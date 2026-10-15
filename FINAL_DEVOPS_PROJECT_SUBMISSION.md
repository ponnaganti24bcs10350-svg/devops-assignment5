# Session 21: Final DevOps Capstone Project & Troubleshooting

**Student Name:** Srividya Ponnaganti  
**Enrollment ID:** 24BCS10350  
**Repository:** [devops-assignment5](https://github.com/ponnaganti24bcs10350-svg/devops-assignment5)  
**Date:** October 8, 2026  

---

## Executive Summary

This submission represents the **Final Capstone DevOps Project (Session 21)**, bringing together all core disciplines of enterprise Cloud Engineering, DevSecOps, Container Orchestration, Infrastructure as Code, Observability, and GitOps into an end-to-end production platform.

```
Application -> Git -> GitHub -> CI Pipeline -> Build & Test -> Security Scanning -> Docker Image -> Container Registry -> Kubernetes -> Helm -> Monitoring -> GitOps
```

---

## Deliverables Structure & Directory Tree

```
devops-assign/final-devops-project/
├── application/
│   ├── src/server.js           # Production Express API with /metrics, /healthz, structured logs
│   ├── tests/server.test.js    # Jest integration test suite (100% pass)
│   └── package.json            # Node.js dependencies
├── docker/
│   ├── Dockerfile              # Multi-stage hardened build (Node 20 Alpine, non-root UID)
│   └── .dockerignore           # Optimized build exclusions
├── kubernetes/
│   └── app-manifests.yaml      # Deployment, Service, ConfigMap, Secret, Ingress, HPA, Probes, Storage, NetPol
├── helm/
│   ├── Chart.yaml              # Chart metadata
│   ├── values.yaml             # Dynamic parameters
│   └── templates/              # Deployment, Service, Ingress, HPA templates
├── terraform/
│   ├── provider.tf             # AWS Provider (~> 5.0)
│   ├── variables.tf            # Parameter definitions
│   ├── main.tf                 # VPC, Subnet, IGW, Route Table, S3 Bucket
│   └── outputs.tf              # Infrastructure outputs
├── .github/workflows/
│   └── final-pipeline.yml      # CI/CD & DevSecOps Workflow (SAST, SCA, Secrets, Trivy, Helm Lint)
├── security/
│   └── .gitleaks.toml          # Secret scanning configuration
├── monitoring/
│   └── prometheus-rules.yaml   # PrometheusRule alert definitions
├── gitops/
│   └── argocd-final-app.yaml   # ArgoCD Application CRD (self-heal, continuous reconciliation)
└── README.md                   # Complete architectural guide and RCA documentation
```

---

## 1. Cloud Infrastructure as Code (Terraform)

- **VPC & Subnets ([main.tf](file:///Users/srividya/devops-assign/final-devops-project/terraform/main.tf)):** Custom VPC with CIDR `10.100.0.0/16`, public subnet `10.100.1.0/24`, and Internet Gateway route tables.
- **S3 State & Artifacts:** S3 bucket configured with `force_destroy = true`, SSE-S3 AES-256 encryption, and strict `aws_s3_bucket_public_access_block`.

---

## 2. DevSecOps CI/CD Pipeline ([final-pipeline.yml](file:///Users/srividya/devops-assign/final-devops-project/.github/workflows/final-pipeline.yml))

```
1. Build & Unit Tests (Jest) -> 2. Secret Scan (Gitleaks) -> 3. SAST (Semgrep) -> 4. SCA (npm audit) -> 5. Multi-Stage Docker Build -> 6. Trivy Image Scan -> 7. Security Gate -> 8. Helm Lint & GitOps Sync
```

### DevSecOps Evidence:
![Final DevSecOps Pipeline](/Users/srividya/devops-assign/screenshots/55_final_devsecops_pipeline.png)

---

## 3. Kubernetes & Helm Deployment

- **Helm Chart ([helm/](file:///Users/srividya/devops-assign/final-devops-project/helm/)):** Enterprise Helm packaging with configurable replica count, resource requests/limits, Startup/Liveness/Readiness probes, Horizontal Pod Autoscaling (HPA: min 2, max 10 at 70% CPU target), and NGINX Ingress routing (`devops-final.local`).

### Kubernetes & Helm Evidence:
![Kubernetes Helm & HPA](/Users/srividya/devops-assign/screenshots/56_final_k8s_helm_hpa.png)

---

## 4. Monitoring & Observability

- **Metrics:** Exposes `/metrics` in Prometheus format collecting HTTP request counts, durations, process CPU %, and memory RSS.
- **Health:** `/healthz` liveness probe and `/ready` readiness probe.
- **Structured Logs:** High-cardinality JSON logs emitted to stdout and indexed by log shippers.

### Observability Evidence:
![Monitoring & Observability](/Users/srividya/devops-assign/screenshots/57_final_monitoring_observability.png)

---

## 5. GitOps Continuous Delivery & Troubleshooting Case Studies

### GitOps Workflow:
- **ArgoCD Controller ([argocd-final-app.yaml](file:///Users/srividya/devops-assign/final-devops-project/gitops/argocd-final-app.yaml)):** Continuous synchronization against Git repository with automatic pruning and self-healing.

### Troubleshooting Scenarios (Root Cause Analysis):
1. **Incident 1 (`CrashLoopBackOff`):** Probe path mismatch between `/health` and `/healthz`. Resolved by updating probe path in `values.yaml`.
2. **Incident 2 (`HTTP 503 Bad Gateway`):** Service selector mismatch with deployment label (`app: final-devops-app`). Resolved selector in `service.yaml`.
3. **Incident 3 (Manual Cluster Drift):** Replicas dropped from 3 to 1 manually via kubectl. ArgoCD `selfHeal` detected drift and restored desired state in 15 seconds.

### GitOps & Troubleshooting Evidence:
![GitOps & Troubleshooting RCA](/Users/srividya/devops-assign/screenshots/58_final_gitops_troubleshooting.png)

---

## Conclusion

The Final DevOps Capstone Project brings together the entire syllabus into an enterprise-ready, self-healing, automated, and secure cloud delivery platform.
