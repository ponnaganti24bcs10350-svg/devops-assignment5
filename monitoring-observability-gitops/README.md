# Session 20: Monitoring, Observability & GitOps

**Student:** Srividya Ponnaganti  
**Enrollment:** 24BCS10350  
**Repository:** [devops-assignment5](https://github.com/ponnaganti24bcs10350-svg/devops-assignment5)  

---

## Directory Index

```
monitoring-observability-gitops/
├── 01-monitoring/
│   ├── app/
│   │   ├── app.py                # Microservice exposing /metrics, /healthz, /api/data
│   │   ├── Dockerfile            # Container definition
│   │   └── requirements.txt      # Python dependencies
│   ├── k8s/
│   │   ├── deployment.yaml       # K8s deployment with Prometheus annotations
│   │   ├── service.yaml          # ClusterIP service
│   │   └── prometheus-alertmanager.yaml # Prometheus scrape config & alert rules
│   └── README.md                 # Monitoring systems guide & commands
├── 02-observability/
│   └── README.md                 # Three Pillars (Metrics, Logs, Traces) & OTel Architecture
└── 03-gitops/
    ├── apps/
    │   └── webapp/
    │       └── deployment.yaml   # Declarative application manifests
    ├── argocd/
    │   ├── application.yaml      # ArgoCD Application CRD (self-heal, auto-sync)
    │   └── appproject.yaml       # ArgoCD AppProject RBAC boundary
    └── README.md                 # GitOps workflow, continuous reconciliation & drift healing
```

---

## Tasks Summary

1. **[01. Monitoring Demo & Guide](file:///Users/srividya/devops-assign/monitoring-observability-gitops/01-monitoring/README.md):** Demonstrates real-time metric counters, gauges, Prometheus format, structured JSON logging, Alertmanager alert evaluation rules, CPU/Memory resource constraints, and `/healthz` liveness/readiness probes.
2. **[02. Observability Architecture](file:///Users/srividya/devops-assign/monitoring-observability-gitops/02-observability/README.md):** Deep-dive into the Three Pillars (Metrics, Logs, Traces), OpenTelemetry standard, context propagation across microservices, and Kubernetes observability stack (cAdvisor, KSM, Promtail, Service Mesh).
3. **[03. GitOps & ArgoCD Reconciliation](file:///Users/srividya/devops-assign/monitoring-observability-gitops/03-gitops/README.md):** Establishes Git as the single source of truth, pull-based vs push-based comparison, declarative configuration management, continuous reconciliation, and automated drift correction.
