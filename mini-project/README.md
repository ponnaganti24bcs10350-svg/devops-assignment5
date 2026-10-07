# Session 13 Mini-Project: Resilient & Auto-Scaling Multi-Tier Application

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**Course/Session:** Session 13 - Kubernetes Storage, HPA & Probes  

---

## 1. Project Overview & Architecture

This mini-project demonstrates an enterprise-ready, multi-tier architecture deployed on Kubernetes, integrating:
1. **Durable Storage Layer:** Stateful MySQL database backed by dynamic **PersistentVolumeClaim (PVC)** on `standard` StorageClass.
2. **Resilience & Health Probes:** Web application configured with **Startup Probes**, **Readiness Probes**, and **Liveness Probes**.
3. **Dynamic Scalability:** **Horizontal Pod Autoscaler (HPA)** configured for auto-scaling from 2 to 6 replicas.
4. **Decoupled Configuration:** ConfigMaps for environment variables and Secrets for database credentials.

```mermaid
flowchart TD
    Client[Client Traffic / Ingress] --> WebService[web-app-service (NodePort 32080)]
    
    subgraph WebTier ["Web / API Application Tier (Auto-Scaling)"]
        HPA[Horizontal Pod Autoscaler<br/>Target: 50% CPU | Min: 2, Max: 6]
        HPA -.-> WebPods
        WebPods["web-app Pods (2 - 6 Replicas)<br/>• Startup Probe (/healthz)<br/>• Readiness Probe (/healthz)<br/>• Liveness Probe (/healthz)"]
        WebCM["ConfigMap: web-app-config"] --> WebPods
    end
    
    WebService --> WebPods
    WebPods --> DBService[mysql-service (ClusterIP: 3306)]
    
    subgraph DBTier ["Stateful Database Tier (Persistent Storage)"]
        DBService --> DBPod["mysql-db Pod<br/>• Readiness Probe (mysqladmin ping)<br/>• Liveness Probe (mysqladmin ping)"]
        DBSecret["Secret: db-secret"] --> DBPod
        DBPVC["PersistentVolumeClaim (1Gi RWO)"] --> DBPod
        PV["PersistentVolume (standard StorageClass)"] -.-> DBPVC
    end
```

---

## 2. Manifests Breakdown

- [`01-storage-db.yaml`](file:///Users/srividya/devops-assign/mini-project/01-storage-db.yaml): Database Secret, PersistentVolumeClaim, MySQL Deployment with exec health probes, and ClusterIP service.
- [`02-app-probes.yaml`](file:///Users/srividya/devops-assign/mini-project/02-app-probes.yaml): Web ConfigMap, Deployment with Startup/Readiness/Liveness HTTP probes and resource requests/limits, NodePort Service.
- [`03-app-hpa.yaml`](file:///Users/srividya/devops-assign/mini-project/03-app-hpa.yaml): Horizontal Pod Autoscaler targeting 50% average CPU utilization.

---

## 3. Health Probes In-Depth

| Probe Type | Purpose | Configuration in Mini-Project | Action on Failure |
| :--- | :--- | :--- | :--- |
| **Startup Probe** | Protects applications with long bootstrap/init times from premature kills. | `httpGet: /healthz`, `failureThreshold: 10`, `periodSeconds: 3` | Disables other probes until success; kills pod if threshold exceeded. |
| **Readiness Probe** | Determines if the container is ready to accept incoming user traffic. | `httpGet: /healthz`, `periodSeconds: 5`, `failureThreshold: 3` | Removes Pod IP from Service Endpoints / Load Balancer without restarting it. |
| **Liveness Probe** | Detects deadlocks, internal crashes, or frozen threads. | `httpGet: /healthz`, `periodSeconds: 10`, `failureThreshold: 3` | Kubelet restarts the container according to `restartPolicy`. |

---

## 4. Deployment & Verification Steps

### Step 1: Deploy Database Tier with Persistent Storage
```bash
kubectl apply -f mini-project/01-storage-db.yaml
kubectl get pvc db-data-pvc
kubectl get pods -l app=miniproject-db
```

### Step 2: Deploy Web Application Tier with Probes
```bash
kubectl apply -f mini-project/02-app-probes.yaml
kubectl get pods -l app=miniproject-web
kubectl describe pod -l app=miniproject-web | grep -E "Startup|Readiness|Liveness"
```

### Step 3: Deploy Autoscaler (HPA)
```bash
kubectl apply -f mini-project/03-app-hpa.yaml
kubectl get hpa web-app-hpa
```

### Step 4: Verify Connectivity & Service Response
```bash
curl http://$(minikube ip):32080
```
**Output:**
```html
<h1>🚀 Session 13 Mini-Project: Scalable Web Application with Probes & PVC</h1>
```
