# Session 14 Mini-Project: Multi-Fault Kubernetes Troubleshooting Lab

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**Course/Session:** Session 14 - Kubernetes Troubleshooting  

---

## 1. Problem Statement

A critical production payment gateway microservice `payment-service-deployment` was deployed using [`broken-payment-app.yaml`](file:///Users/srividya/devops-assign/k8s-troubleshooting/03-mini-project/broken-payment-app.yaml).
Upon deployment:
1. Pods were failing to start (`ImagePullBackOff` and `CreateContainerConfigError`).
2. The internal Service `payment-service` had 0 endpoints (`<none>`), causing 100% transaction failure.

---

## 2. Step-by-Step Investigation & RCA

### Step 1: Check Pod Status
```bash
kubectl get pods -l app=payment-service
```
**Output:**
```text
NAME                                         READY   STATUS             RESTARTS   AGE
payment-service-deployment-78f9bd746-9k2lw   0/1     ImagePullBackOff   0          25s
payment-service-deployment-78f9bd746-lm8sz   0/1     ImagePullBackOff   0          25s
```

---

### Step 2: Describe Pod for Events
```bash
kubectl describe pod -l app=payment-service
```
**Identified Faults:**
- **Fault 1:** `Failed to pull image "nginx:v999-broken-tag": rpc error: code = NotFound`
- **Fault 2:** `Error: configmap "missing-payment-config" not found`

---

### Step 3: Inspect Service & Endpoints
```bash
kubectl describe svc payment-service
kubectl get endpoints payment-service
```
**Identified Faults:**
- **Fault 3:** `Selector: app=payment-wrong-selector` does not match Pod label `app=payment-service`. Result: `Endpoints: <none>`.
- **Fault 4:** `TargetPort: 8443` does not match container's listening port `80`.

---

## 3. Root Cause Analysis (RCA) Matrix

| Component | Error / Symptom | Root Cause | Fix Required |
| :--- | :--- | :--- | :--- |
| **Image** | `ImagePullBackOff` | `image: nginx:v999-broken-tag` non-existent | Update image to `nginx:alpine` |
| **Config** | `CreateContainerConfigError` | ConfigMap `missing-payment-config` missing | Create `payment-config` ConfigMap with `mode: production-live` |
| **Service Selector** | `Endpoints: <none>` | Selector set to `app=payment-wrong-selector` | Change selector to `app: payment-service` |
| **Service Port** | Port unreachable | `targetPort: 8443` vs containerPort `80` | Change targetPort to `80` |

---

## 4. Applied Solution

Applied the corrected configuration in [`fixed-payment-app.yaml`](file:///Users/srividya/devops-assign/k8s-troubleshooting/03-mini-project/fixed-payment-app.yaml):
```bash
kubectl apply -f k8s-troubleshooting/03-mini-project/fixed-payment-app.yaml
```

---

## 5. Verification & Before / After Comparison

### Status Comparison Table:

| Metric | Before Fix (Broken) | After Fix (Resolved) |
| :--- | :--- | :--- |
| **Pod Status** | `ImagePullBackOff` / `CreateContainerConfigError` | `2/2 Running (Ready)` |
| **ConfigMap** | Missing (`nonexistent`) | `payment-config` Bound |
| **Service Endpoints** | `<none>` | `10.244.0.58:80, 10.244.0.59:80` |
| **HTTP Response** | Failed / Connection Refused | `HTTP 200 OK: 💳 Payment Microservice Gateway: Healthy` |

### Post-Fix Verification Commands:
```bash
# Check Pods
kubectl get pods -l app=payment-service

# Check Endpoints
kubectl get endpoints payment-service

# Verify HTTP traffic via cluster curl
kubectl run curl-test --image=curlimages/curl:latest --restart=Never -- curl -s http://payment-service
```
**Output:**
```html
<h1>💳 Payment Microservice Gateway: Healthy & Processing (HTTP 200)</h1>
```
