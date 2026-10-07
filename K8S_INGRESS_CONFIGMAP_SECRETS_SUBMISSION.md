# Session 12: Kubernetes Ingress, ConfigMaps & Secrets Submission

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**Course:** DevOps Engineering / Kubernetes  
**Repository:** [devops-assignment5](https://github.com/ponnaganti24bcs10350-svg/devops-assignment5)  

---

## Executive Summary
This submission documents the practical implementation and architectural concepts for **Session 12: Kubernetes Ingress, ConfigMaps & Secrets**. It includes hands-on demonstrations of decoupled application configuration using **ConfigMaps**, sensitive data injection via **Secrets**, Layer 7 HTTP/HTTPS routing via **Ingress & Ingress Controller**, in-depth architectural comparisons, and an end-to-end **Troubleshooting Case Study** for resolving broken Ingress backends.

---

## Table of Contents
1. [Task 1: Kubernetes ConfigMap Demo](#task-1-kubernetes-configmap-demo)
2. [Task 2: Kubernetes Secret Demo & Git Security Analysis](#task-2-kubernetes-secret-demo--git-security-analysis)
3. [Task 3: Kubernetes Ingress Routing Demo](#task-3-kubernetes-ingress-routing-demo)
4. [Task 4: Ingress vs Ingress Controller In-Depth](#task-4-ingress-vs-ingress-controller-in-depth)
5. [Task 5: Hands-on Troubleshooting & RCA](#task-5-hands-on-troubleshooting--rca)
6. [Evidence & Screenshots Index](#evidence--screenshots-index)
7. [Deliverables Summary](#deliverables-summary)

---

## Task 1: Kubernetes ConfigMap Demo

ConfigMaps allow externalizing configuration artifacts from container image builds to promote portability across environments (Development, Staging, Production).

### 1. Manifests
- **ConfigMap Manifest:** [`k8s-configmaps-secrets/01-configmap/app-configmap.yaml`](file:///Users/srividya/devops-assign/k8s-configmaps-secrets/01-configmap/app-configmap.yaml)
  - Key-value pairs: `APP_ENV`, `DATABASE_HOST`, `DATABASE_PORT`, `MAX_CONNECTIONS`
  - Multi-line file configuration: `app.properties`
- **Pod Consumer Manifest:** [`k8s-configmaps-secrets/01-configmap/pod-configmap.yaml`](file:///Users/srividya/devops-assign/k8s-configmaps-secrets/01-configmap/pod-configmap.yaml)
  - Direct environment variable binding via `configMapKeyRef`
  - Bulk environment variable loading via `envFrom.configMapRef`
  - Configuration file volume mounting at `/etc/config/app.properties`

### 2. Commands & Verification
```bash
# Apply ConfigMap and Pod
kubectl apply -f k8s-configmaps-secrets/01-configmap/app-configmap.yaml
kubectl apply -f k8s-configmaps-secrets/01-configmap/pod-configmap.yaml

# Inspect ConfigMap
kubectl get configmap app-config -o yaml

# Verify Environment Variables inside Pod
kubectl exec pod-configmap-demo -- env | grep -E "APP_|DB_|MAX_CONNECTIONS"

# Verify Mounted Configuration File inside Pod
kubectl exec pod-configmap-demo -- cat /etc/config/app.properties
```

### 3. Output Evidence
```text
APP_ENVIRONMENT=production
DB_HOST=postgres-db.internal
MAX_CONNECTIONS=100
APP_ENV=production

server.port=8080
logging.level.root=INFO
feature.dark_mode=true
```

![ConfigMap Demo Verification](screenshots/20_k8s_configmap.png)

---

## Task 2: Kubernetes Secret Demo & Git Security Analysis

Kubernetes Secrets let you store and manage sensitive information, such as passwords, OAuth tokens, and ssh keys.

### 1. Manifests
- **Secret Manifest:** [`k8s-configmaps-secrets/02-secret/app-secret.yaml`](file:///Users/srividya/devops-assign/k8s-configmaps-secrets/02-secret/app-secret.yaml)
  - StringData fields: `DB_PASSWORD`, `API_KEY`, `JWT_SECRET`, `secret.key` (RSA key)
- **Pod Consumer Manifest:** [`k8s-configmaps-secrets/02-secret/pod-secret.yaml`](file:///Users/srividya/devops-assign/k8s-configmaps-secrets/02-secret/pod-secret.yaml)
  - Injected via `secretKeyRef` and `envFrom.secretRef`
  - Mounted volume at `/etc/secrets/secret.key`

### 2. Commands & Verification
```bash
# Apply Secret and Consumer Pod
kubectl apply -f k8s-configmaps-secrets/02-secret/app-secret.yaml
kubectl apply -f k8s-configmaps-secrets/02-secret/pod-secret.yaml

# Inspect Raw Secret (Stored as Base64)
kubectl get secret app-secret -o yaml

# Verify Decoded Values inside Pod Environment
kubectl exec pod-secret-demo -- env | grep -E "DATABASE_PASSWORD|API_KEY|JWT_SECRET|DB_PASSWORD"

# Verify Mounted Secret File
kubectl exec pod-secret-demo -- cat /etc/secrets/secret.key
```

### 3. Output Evidence
```text
DATABASE_PASSWORD=SuperSecretPassword123!
API_KEY=ak_live_998877665544332211
DB_PASSWORD=SuperSecretPassword123!
JWT_SECRET=my-ultra-secure-jwt-signing-key

-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA0Y3wZ...EXAMPLE_KEY_DATA...
-----END RSA PRIVATE KEY-----
```

![Secret Demo Verification](screenshots/21_k8s_secret.png)

### 4. Why Secrets Should NOT Be Committed to Git
1. **Base64 is Encoding, Not Encryption:** Kubernetes Secrets in raw YAML are only Base64-encoded strings (`echo -n "..." | base64 -d`), which can be instantly decoded by anyone with repository access.
2. **Git History Permanence:** Once a secret is committed into a Git repository, it remains in the Git commit history even if deleted in a subsequent commit. Extracting it requires rewriting history with tools like `git-filter-repo` or BFG Repo-Cleaner.
3. **Audit Trail & Access Control:** Version control systems are shared across developers, CI/CD pipelines, and backup servers. Storing secrets in Git violates the Principle of Least Privilege.
4. **Production Best Practices:**
   - **Sealed Secrets:** Encrypt secrets using asymmetric keys (public key stored in Git, private key stored inside Kubernetes).
   - **External Secrets Operator (ESO):** Dynamically fetch secrets from HashiCorp Vault, AWS Secrets Manager, GCP Secret Manager, or Azure Key Vault.
   - **Git Pre-commit Hooks:** Use tools like `git-secrets`, `trufflehog`, or `gitleaks` to prevent accidental credential commits.

---

## Task 3: Kubernetes Ingress Routing Demo

Ingress manages external HTTP/HTTPS access to services within the cluster, providing Layer 7 path and host-based routing.

### 1. Ingress Setup & Manifests
- **Backend Deployments & Services:** [`k8s-ingress/app-deployments-services.yaml`](file:///Users/srividya/devops-assign/k8s-ingress/app-deployments-services.yaml)
  - `apple-app` Deployment + `apple-service` ClusterIP (Port 80)
  - `banana-app` Deployment + `banana-service` ClusterIP (Port 80)
- **Ingress Resource:** [`k8s-ingress/ingress.yaml`](file:///Users/srividya/devops-assign/k8s-ingress/ingress.yaml)
  - Host: `myapp.local`
  - Path `/apple` -> `apple-service:80`
  - Path `/banana` -> `banana-service:80`

### 2. Commands & Verification
```bash
# Enable Ingress Controller on Minikube
minikube addons enable ingress

# Deploy applications and Ingress rules
kubectl apply -f k8s-ingress/app-deployments-services.yaml
kubectl apply -f k8s-ingress/ingress.yaml

# Verify Ingress Object
kubectl get ingress demo-ingress

# Test Layer 7 Path Routing
minikube ssh "curl -s -H 'Host: myapp.local' http://localhost/apple"
minikube ssh "curl -s -H 'Host: myapp.local' http://localhost/banana"
```

### 3. Output Evidence
```text
<h1>🍎 Welcome to Apple App Backend (Route: /apple)</h1>
<h1>🍌 Welcome to Banana App Backend (Route: /banana)</h1>
```

![Ingress Demo Verification](screenshots/22_k8s_ingress.png)

---

## Task 4: Ingress vs Ingress Controller In-Depth

Detailed guide created in [`ingress-vs-controller/README.md`](file:///Users/srividya/devops-assign/ingress-vs-controller/README.md).

### Summary Comparison:

| Feature | Kubernetes Ingress | Ingress Controller |
| :--- | :--- | :--- |
| **Definition** | Declarative API resource specifying routing rules and hosts. | Reverse proxy daemon that monitors the API and enforces routing rules. |
| **Nature** | Configuration object (stored as YAML/JSON in `etcd`). | Running software process (e.g., NGINX, Envoy, Traefik, HAProxy). |
| **Core Availability** | Native Kubernetes API (`networking.k8s.io/v1`). | **Not installed by default**; must be deployed as an addon or Helm chart. |
| **Responsibility** | Defines *what* routes should exist. | Executes *how* packets are accepted, decrypted, load-balanced, and forwarded. |
| **Real-world Analogy** | A **boarding pass** listing departure and destination gates. | The **airplane & ground crew** physically routing the passengers. |

---

## Task 5: Hands-on Troubleshooting & RCA

Dedicated scenario documented in [`troubleshooting/README.md`](file:///Users/srividya/devops-assign/troubleshooting/README.md).

### 1. Problem Description
Clients accessing `http://orders.local/orders` encountered `HTTP 503 Service Temporarily Unavailable` / `404 Not Found`.

### 2. Troubleshooting Workflow
1. **Symptom Check:** `minikube ssh "curl -i -H 'Host: orders.local' http://localhost/orders"` returned `503 Service Unavailable`.
2. **Ingress Diagnosis:** `kubectl describe ingress order-ingress` showed backend `order-service:80 (<error: endpoints not found>)`.
3. **Service Diagnosis:** `kubectl describe svc order-service` reported `Endpoints: <none>`.
4. **Root Cause Analysis:**
   - **Bug 1:** Service selector was set to `app=orders` while Pod label was `app=order-service`.
   - **Bug 2:** Service `targetPort` was set to `9090` while container listened on `80`.

### 3. Resolution
Applied corrected manifest [`troubleshooting/fixed-ingress-service.yaml`](file:///Users/srividya/devops-assign/troubleshooting/fixed-ingress-service.yaml):
- Updated selector to `app: order-service`.
- Updated targetPort to `80`.

### 4. Verification Output
```bash
$ kubectl get endpoints order-service
NAME            ENDPOINTS                       AGE
order-service   10.244.0.51:80,10.244.0.52:80   25s

$ minikube ssh "curl -s -H 'Host: orders.local' http://localhost/orders"
<h1>🛍️ Order Service API Online (HTTP 200)</h1>
```

![Troubleshooting Verification](screenshots/23_k8s_troubleshooting.png)

---

## Evidence & Screenshots Index

| File | Description | Task |
| :--- | :--- | :--- |
| [`20_k8s_configmap.png`](screenshots/20_k8s_configmap.png) | ConfigMap injection (environment variables & mounted volume properties) | Task 1 |
| [`21_k8s_secret.png`](screenshots/21_k8s_secret.png) | Secret injection (env variables & mounted RSA private key file) | Task 2 |
| [`22_k8s_ingress.png`](screenshots/22_k8s_ingress.png) | Ingress controller routing `/apple` and `/banana` backends | Task 3 |
| [`23_k8s_troubleshooting.png`](screenshots/23_k8s_troubleshooting.png) | Step-by-step diagnostic RCA and resolution of broken Ingress endpoints | Task 5 |

---

## Deliverables Summary

- [x] ConfigMap YAML in [`k8s-configmaps-secrets/01-configmap/`](file:///Users/srividya/devops-assign/k8s-configmaps-secrets/01-configmap)
- [x] Secret YAML in [`k8s-configmaps-secrets/02-secret/`](file:///Users/srividya/devops-assign/k8s-configmaps-secrets/02-secret)
- [x] Ingress YAML in [`k8s-ingress/`](file:///Users/srividya/devops-assign/k8s-ingress)
- [x] Ingress vs Ingress Controller Guide in [`ingress-vs-controller/README.md`](file:///Users/srividya/devops-assign/ingress-vs-controller/README.md)
- [x] Troubleshooting Guide and Manifests in [`troubleshooting/`](file:///Users/srividya/devops-assign/troubleshooting)
- [x] High-resolution verification screenshots in [`screenshots/`](file:///Users/srividya/devops-assign/screenshots)
