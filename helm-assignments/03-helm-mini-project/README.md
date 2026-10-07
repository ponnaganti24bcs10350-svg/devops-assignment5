# Session 15 Mini-Project: Enterprise Custom Helm Chart & Lifecycle Management

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**Course/Session:** Session 15 - Helm  

---

## 1. Project Overview & Chart Architecture

This mini-project demonstrates the design, linting, packaging, and lifecycle management of a production-ready custom Helm chart named **`webapp`**.

The chart standardizes the deployment of microservices with:
- **Dynamic ConfigMaps & Secrets:** Templated injection from `values.yaml`.
- **Health Probes:** Fully configurable Startup, Liveness, and Readiness probes.
- **Autoscaling (HPA):** Conditional HPA generation (`{{- if .Values.autoscaling.enabled }}`).
- **Resource Constraints:** Granular CPU/Memory requests and limits.
- **Service Abstraction:** Configurable `ClusterIP` / `NodePort` / `LoadBalancer` types.

```
webapp-chart/
├── Chart.yaml                  # Chart metadata and versioning
├── values.yaml                 # Default configuration values
└── templates/                  # Reusable Kubernetes YAML templates
    ├── _helpers.tpl            # Template helper macros and naming logic
    ├── configmap.yaml          # ConfigMap template
    ├── secret.yaml             # Secret template
    ├── deployment.yaml         # Workload deployment template
    ├── service.yaml            # Networking service template
    ├── hpa.yaml                # Autoscaler template
    └── NOTES.txt               # Post-installation CLI instructions
```

---

## 2. Validation & Testing Workflow

### Step 1: Lint the Chart for Syntax & Best Practices
```bash
helm lint ./helm-assignments/03-helm-mini-project/webapp-chart
```
**Output:**
```text
==> Linting ./helm-assignments/03-helm-mini-project/webapp-chart
1 chart(s) linted, 0 chart(s) failed
```

---

### Step 2: Render Templates Locally (Dry-Run / Template Debugging)
```bash
helm template test-run ./helm-assignments/03-helm-mini-project/webapp-chart --set replicaCount=3
```
*Validates that all Go template expressions resolve correctly without executing against the cluster.*

---

### Step 3: Install the Custom Chart
```bash
helm install prod-app ./helm-assignments/03-helm-mini-project/webapp-chart \
  --set service.type=NodePort \
  --set service.nodePort=32090 \
  --set replicaCount=2
```

---

### Step 4: Verify Live Resources
```bash
kubectl get all -l app.kubernetes.io/instance=prod-app
```
**Output:**
```text
NAME                                       READY   STATUS    RESTARTS   AGE
pod/prod-app-webapp-649f4cb4db-m9kx4       1/1     Running   0          20s
pod/prod-app-webapp-649f4cb4db-q2tz5       1/1     Running   0          20s

NAME                      TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/prod-app-webapp   NodePort   10.108.45.120   <none>        80:32090/TCP   20s

NAME                              READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/prod-app-webapp   2/2     2            2           20s
```

---

### Step 5: Test Application Response
```bash
curl http://$(minikube ip):32090
```
**Output:**
```html
<h1>📦 Helm Deployed App: prod-app-webapp</h1><p>Environment: production | Message: Welcome to Production Helm Managed Microservice!</p>
```
