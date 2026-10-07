# Task 1: Monitoring Systems Guide & Demo

**Student:** Srividya Ponnaganti  
**Enrollment:** 24BCS10350  
**Session:** 20 - Monitoring, Observability & GitOps  

---

## 1. What is Monitoring?

**Monitoring** is the automated process of collecting, aggregating, analyzing, and visualizing quantitative data about systems to determine whether they are functioning within acceptable operational thresholds.

```
+-----------------------------------------------------------------------------------+
|                                  Monitoring Pipeline                              |
|                                                                                   |
|  +---------------------+      +---------------------+      +-------------------+  |
|  |     Data Sources    |      |  Collection/Storage |      |  Visualization &  |  |
|  | (Pods, Nodes, Apps) | ---> | (Prometheus / TSDB) | ---> |     Alerting      |  |
|  +---------------------+      +---------------------+      +---------+---------+  |
|                                                                      |            |
|                                                                      v            |
|                                                            +-------------------+  |
|                                                            |  Grafana Dash /   |  |
|                                                            | Alertmanager (Ops)|  |
|                                                            +-------------------+  |
+-----------------------------------------------------------------------------------+
```

---

## 2. Core Monitoring Disciplines

### 2.1 Metrics
* Numerical values measured over time (Time-Series Data: timestamp + metric name + labels + numeric float value).
* **Metric Types:**
  1. **Counter:** A cumulative metric that only increases or resets to zero upon restart (e.g. `http_requests_total`).
  2. **Gauge:** A metric that can arbitrarily go up and down (e.g. `process_cpu_utilization_percent`, `memory_bytes`).
  3. **Histogram:** Samples observations into configurable buckets and counts occurrences (e.g. `http_request_duration_seconds_bucket`).
  4. **Summary:** Calculates configurable percentiles over a sliding time window.

### 2.2 Structured Logs
* High-cardinality discrete event records emitted during execution.
* Emitted as structured JSON containing timestamp, service name, HTTP verb, status code, latency, and client metadata:
```json
{
  "timestamp": "2026-10-08T00:45:10Z",
  "service": "observability-demo-api",
  "environment": "production",
  "method": "GET",
  "path": "/api/data",
  "status_code": 200,
  "duration_ms": 52.4,
  "client_ip": "10.244.0.1",
  "trace_id": "trace-1791398000-1420"
}
```

### 2.3 Alerts
* Rules defined over metric expressions. When a condition evaluates to `true` for a specified duration (e.g., `for: 2m`), Alertmanager routes notifications (Email, Slack, PagerDuty, Webhooks).
* **Severity Levels:** `info`, `warning`, `critical`, `page`.

### 2.4 CPU & Memory Utilization
* **CPU Utilization:** Measured in cores / millicores (`m`). If a container exceeds its `limits.cpu`, the Linux CFS (Completely Fair Scheduler) **throttles** CPU cycles, degrading response times without crashing.
* **Memory Utilization:** Measured in bytes / megabytes (`Mi`). If a container exceeds its `limits.memory`, the Linux kernel triggers the **OOM (Out-of-Memory) Killer**, terminating the pod (`Exit Code 137 / OOMKilled`).

### 2.5 Application Health & Probes
* Specialized HTTP/TCP endpoints:
  * `/healthz` (Liveness): Validates if the application runtime is alive. If failing, kubelet restarts the container.
  * `/ready` (Readiness): Validates if the application is ready to receive network traffic (e.g. DB connection established). If failing, the Service removes the Pod from endpoint routing.

---

## 3. Hands-On Verification & Commands

```bash
# 1. Deploy the demo application to Kubernetes
$ kubectl apply -f k8s/deployment.yaml
deployment.apps/observability-demo-app created
service/observability-demo-service created

# 2. Verify Pod health and probe status
$ kubectl get pods -l app=observability-demo -o wide
NAME                                     READY   STATUS    RESTARTS   AGE   IP           NODE
observability-demo-app-7984fb86b8-8k2p   1/1     Running   0          30s   10.244.0.15  minikube
observability-demo-app-7984fb86b8-9z4x   1/1     Running   0          30s   10.244.0.16  minikube

# 3. Test Health Endpoint
$ curl -s http://10.244.0.15:8080/healthz
{
  "status": "HEALTHY",
  "app": "observability-demo-api",
  "version": "v1.0.0",
  "uptime_seconds": 32.4,
  "student": "Srividya Ponnaganti (24BCS10350)"
}

# 4. Scrape Prometheus Metrics
$ curl -s http://10.244.0.15:8080/metrics
# HELP http_requests_total Total number of HTTP requests received.
# TYPE http_requests_total counter
http_requests_total{service="observability-demo",handler="all"} 14
# HELP process_cpu_utilization_percent Current CPU utilization percentage.
# TYPE process_cpu_utilization_percent gauge
process_cpu_utilization_percent{service="observability-demo"} 1.4
# HELP app_health_status Application health flag.
# TYPE app_health_status gauge
app_health_status{service="observability-demo"} 1

# 5. Apply Prometheus Scrape & Alerting Rules
$ kubectl apply -f k8s/prometheus-alertmanager.yaml
configmap/prometheus-config created
```
