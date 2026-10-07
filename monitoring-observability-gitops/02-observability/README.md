# Task 2: Observability Architecture & The Three Pillars

**Student:** Srividya Ponnaganti  
**Enrollment:** 24BCS10350  
**Session:** 20 - Monitoring, Observability & GitOps  

---

## 1. What is Observability?

**Observability** is a measure of how well internal states of a distributed software system can be inferred from knowledge of its external outputs.

While **Monitoring** asks *"Is the system working?"* (alerting on known failure modes / *known unknowns*), **Observability** asks *"Why is the system behaving this way?"* (diagnosing unpredictable failures / *unknown unknowns* in distributed microservice topologies).

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

---

## 2. The Three Pillars of Observability

### 2.1 Pillar 1: Metrics (Aggregatable Time-Series Data)
* **Definition:** Numerically quantified measurements collected at uniform time intervals.
* **Characteristics:** Extremely lightweight, highly compressable, ideal for real-time alerting, trend detection, and SLA/SLO dashboards.
* **Standard Representation:**
  `http_request_duration_seconds{method="POST", path="/checkout", status="500"} 0.842`

### 2.2 Pillar 2: Logs (Contextual Event Streams)
* **Definition:** Immutable, timestamped, textual records of discrete events occurring within an application.
* **Characteristics:** High detail and high cardinality; rich debugging context containing stack traces, database query strings, and error payloads.
* **Best Practice:** Use structured JSON logging with injected `trace_id` and `span_id` to correlate logs directly with distributed traces.

### 2.3 Pillar 3: Distributed Tracing (End-to-End Request Journeys)
* **Definition:** Records the lifecycle of a request as it propagates through distributed microservices, network boundaries, and database queries.
* **Core Concepts:**
  * **Trace:** Represents an entire end-to-end user request path (e.g. `Client -> API Gateway -> Auth Service -> Payment Service -> Database`).
  * **Span:** A single unit of contiguous work within a trace (containing operation name, start/end timestamps, tags, and events).
  * **Context Propagation:** Injecting HTTP headers (such as W3C `traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01`) across network boundaries to correlate all downstream spans.

---

## 3. Why Observability is Essential for Cloud-Native DevOps

1. **Debugging "Unknown Unknowns":** In ephemeral, auto-scaling Kubernetes clusters with hundreds of interacting microservices, traditional single-server troubleshooting breaks down. Observability allows engineers to isolate needle-in-a-haystack anomalies without deploying new debug code.
2. **Accelerated Mean Time to Resolution (MTTR):** Correlating metrics spikes with correlated logs and distributed traces reduces incident investigation time from hours to seconds.
3. **Capacity & Performance Engineering:** Pinpoint distributed bottlenecks (e.g. N+1 database query problem, connection pool exhaustion) across microservice boundaries.

---

## 4. Industry Standard Tooling Matrix

| Pillar / Layer | Open-Source Tool | Cloud-Native / Enterprise | Purpose |
| :--- | :--- | :--- | :--- |
| **Telemetry Standard** | **OpenTelemetry (OTel)** | OpenTelemetry Collector | Vendor-neutral API, SDKs, and data transport specification. |
| **Metrics Storage** | **Prometheus / VictoriaMetrics** | Amazon Managed Prometheus, Datadog | High-throughput time-series database and PromQL query engine. |
| **Log Aggregation** | **Loki / Promtail / Fluentd** | Elasticsearch, Datadog Logs | Log ingestion, indexing, and LogQL querying. |
| **Distributed Tracing** | **Jaeger / Zipkin** | AWS X-Ray, Dynatrace | Trace visualization, latency flame graphs, and dependency graphs. |
| **Unified Visualization**| **Grafana** | Grafana Cloud, Datadog | Single pane of glass correlating metrics, logs, and trace spans. |

---

## 5. Kubernetes Observability Stack Architecture

```
[ Kubernetes Node ]
 ├── [ Kubelet ] ------------> [ cAdvisor ] (Exposes CPU, Memory, Disk, Network container metrics)
 ├── [ DaemonSet ] ----------> [ FluentBit / Promtail ] (Tails /var/log/pods/*.log -> Loki)
 ├── [ Cluster Component ] --> [ kube-state-metrics ] (Exposes Pod statuses, Deployment counts, PVC capacity)
 └── [ Service Mesh ] -------> [ Istio / Envoy Proxy ] (Injects W3C Trace headers & generates access logs)
```

1. **cAdvisor (Container Advisor):** Built directly into Kubelet; collects container resource usage (CPU throttling, working set memory, network bytes).
2. **kube-state-metrics (KSM):** Listens to the Kubernetes API server and generates metrics about the state of objects (e.g. `kube_deployment_status_replicas_unavailable`).
3. **FluentBit / Promtail DaemonSet:** Collects stdout/stderr logs from all node containers and forwards them to a centralized log store.
4. **Service Mesh / Ingress Proxies:** Automatically captures distributed tracing headers at the ingress boundary and tracks inter-service latencies.
