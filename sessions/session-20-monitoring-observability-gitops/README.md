# Session 20: Monitoring, Observability & GitOps - Submission Report

**Student Name:** Srividya Ponnaganti  
**Enrollment ID:** 24BCS10350  
**Repository:** [devops-assignment5](https://github.com/ponnaganti24bcs10350-svg/devops-assignment5)  
**Date:** October 8, 2026  

---

## Executive Summary

This submission provides a complete implementation, architectural analysis, and practical demonstration for **Session 20: Monitoring, Observability & GitOps**, covering:
1. **Task 1: Monitoring Systems & Live Metrics Demo:** Microservice exposing Prometheus `/metrics`, `/healthz` liveness probes, CPU/Memory telemetry, structured JSON logs, and Alertmanager alert rules.
2. **Task 2: Observability Architecture (The Three Pillars):** Comprehensive guide on **Metrics**, **Logs**, and **Distributed Tracing (OpenTelemetry / Jaeger)**, explaining how observability solves "unknown unknowns" in cloud-native microservices.
3. **Task 3: GitOps Principles & ArgoCD Continuous Reconciliation:** Git as the single source of truth, declarative configuration, pull-based synchronization, drift detection, and automated self-healing.

---

## Project Structure & Deliverables Tree

```
devops-assign/monitoring-observability-gitops/
├── 01-monitoring/
│   ├── app/
│   │   ├── app.py                # Python API exposing Prometheus /metrics and /healthz
│   │   ├── Dockerfile            # Container definition
│   │   └── requirements.txt      # psutil dependencies
│   ├── k8s/
│   │   ├── deployment.yaml       # K8s Deployment with Prometheus scrape annotations
│   │   ├── service.yaml          # ClusterIP service definition
│   │   └── prometheus-alertmanager.yaml # Prometheus & Alertmanager scrape & alert rules
│   └── README.md                 # Complete monitoring guide & commands
├── 02-observability/
│   └── README.md                 # Three Pillars (Metrics, Logs, Traces) & OTel Architecture
├── 03-gitops/
│   ├── apps/
│   │   └── webapp/
│   │       └── deployment.yaml   # Declarative application manifests
│   ├── argocd/
│   │   ├── application.yaml      # ArgoCD Application CRD (self-heal, auto-sync)
│   │   └── appproject.yaml       # ArgoCD AppProject RBAC boundary
│   └── README.md                 # GitOps workflow, continuous reconciliation & drift healing
└── README.md                     # Master Session 20 Index
```

---

## Task 1: Monitoring Demo & Metrics Implementation

- **Application Code:** [app.py](file:///Users/srividya/devops-assign/monitoring-observability-gitops/01-monitoring/app/app.py)
  - Exposes `/metrics` in Prometheus text exposition format (Counters, Gauges for CPU % and Memory RSS).
  - Exposes `/healthz` returning HTTP 200 OK JSON status and uptime.
  - Emits high-cardinality structured JSON logs containing `trace_id`, latency, and HTTP status codes.
- **Alert Rules ([prometheus-alertmanager.yaml](file:///Users/srividya/devops-assign/monitoring-observability-gitops/01-monitoring/k8s/prometheus-alertmanager.yaml)):**
  - `HighCPUUtilization`: Triggers warning when CPU > 80% for 2m.
  - `HighMemoryUtilization`: Triggers critical alert when Memory > 85% for 3m.
  - `ApplicationDown`: Triggers page alert when health endpoint fails or metric target is absent.

### Evidence Screenshots:

#### 1. Metrics Scrape & Health Checks
![Monitoring Metrics & Health](/Users/srividya/devops-assign/screenshots/51_monitoring_metrics_health.png)

#### 2. Prometheus Alert Evaluation & Structured Logs
![Alert Rules & Logs](/Users/srividya/devops-assign/screenshots/52_monitoring_prometheus_alerts.png)

---

## Task 2: Observability Architecture & The Three Pillars

Detailed guide in [02-observability/README.md](file:///Users/srividya/devops-assign/monitoring-observability-gitops/02-observability/README.md):

```
+-----------------------------------------------------------------------------------------+
|                                The Three Pillars of Observability                       |
|                                                                                         |
|       +-------------------+     +--------------------+     +---------------------+      |
|       |      METRICS      |     |        LOGS        |     |       TRACES        |      |
|       | (Aggregatable TS) |     | (Contextual Event) |     |  (Request Journey)  |      |
|       +---------+---------+     +---------+----------+     +----------+----------+      |
|                 |                         |                           |                 |
|                 v                         v                           v                 |
|          "What is broken        "What happened at        "Where did latency occur       |
|          and when?"              that exact moment?"      in the microservice chain?"   |
|                 |                         |                           |                 |
|                 +-------------------------+---------------------------+                 |
|                                           |                                             |
|                                           v                                             |
|                             [ OpenTelemetry Standard / API ]                            |
|                                           |                                             |
|                                           v                                             |
|                     [ Unified Grafana / Jaeger / Loki Platform ]                        |
+-----------------------------------------------------------------------------------------+
```

1. **Metrics:** Real-time numerical time-series values aggregated for alerting and SLA/SLO dashboards.
2. **Logs:** Rich structured JSON records capturing individual system events with injected trace context.
3. **Traces:** End-to-end distributed transaction request journeys propagated across microservices using W3C `traceparent` context headers.
4. **Kubernetes Observability Agents:** cAdvisor (container CPU/Memory), kube-state-metrics (cluster object states), FluentBit/Promtail (log forwarding), and Istio Service Mesh (traffic tracing).

#### Observability Architecture Inspection:
![Three Pillars of Observability](/Users/srividya/devops-assign/screenshots/53_observability_pillars_otel.png)

---

## Task 3: GitOps & Continuous Reconciliation

Detailed guide in [03-gitops/README.md](file:///Users/srividya/devops-assign/monitoring-observability-gitops/03-gitops/README.md):

- **Git as Single Source of Truth:** All infrastructure and application states reside in version-controlled Git repositories.
- **Pull-Based Synchronization:** ArgoCD operator polls Git repository and continuously compares desired state against Kubernetes cluster state.
- **Drift Detection & Automated Self-Healing:** When manual modifications are made (`kubectl scale --replicas=1`), ArgoCD immediately detects the divergence and reconciles the cluster back to the Git baseline (3 replicas).

#### GitOps Continuous Reconciliation & Drift Healing:
![GitOps ArgoCD Reconciliation](/Users/srividya/devops-assign/screenshots/54_gitops_argocd_reconciliation.png)

---

## Conclusion & Submission Verification

All tasks for Session 20 have been completed with clean code, declarative manifests, comprehensive documentation, and visual evidence.
