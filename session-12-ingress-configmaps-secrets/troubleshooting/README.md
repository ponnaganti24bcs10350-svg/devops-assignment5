# Kubernetes Troubleshooting Guide: Ingress & Service Misconfiguration

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**Course/Session:** Session 12 - Kubernetes Ingress, ConfigMaps & Secrets  

---

## 1. Problem Scenario

An engineering team deployed a microservice `order-service-app` exposed via an Ingress resource (`orders.local/orders`).
However, clients attempting to reach `http://orders.local/orders` receive **`HTTP 503 Service Temporarily Unavailable`**.

Manifests used:
- Broken State: [`broken-ingress-service.yaml`](file:///Users/srividya/devops-assign/troubleshooting/broken-ingress-service.yaml)
- Resolved State: [`fixed-ingress-service.yaml`](file:///Users/srividya/devops-assign/troubleshooting/fixed-ingress-service.yaml)

---

## 2. Step-by-Step Diagnostic Workflow

### Step 1: Identify the Symptom
```bash
curl -i -H "Host: orders.local" http://192.168.49.2/orders
```
**Output Before Fix:**
```http
HTTP/1.1 503 Service Temporarily Unavailable
Date: Wed, 07 Oct 2026 18:25:00 GMT
Content-Type: text/html
Content-Length: 190
Connection: keep-alive

<html>
<head><title>503 Service Temporarily Unavailable</title></head>
<body>
<center><h1>503 Service Temporarily Unavailable</h1></center>
<hr><center>nginx</center>
</body>
</html>
```

---

### Step 2: Inspect the Ingress Resource
```bash
kubectl describe ingress order-ingress
```
**Observation:**
```text
Rules:
  Host          Path  Backends
  ----          ----  --------
  orders.local  
                /orders   order-service:80 (<error: endpoints not found>)
```
*The Ingress shows `<error: endpoints not found>` for backend `order-service:80`.*

---

### Step 3: Inspect Service Endpoints
```bash
kubectl get endpoints order-service
kubectl describe svc order-service
```
**Observation:**
```text
Name:              order-service
Namespace:         default
Labels:            <none>
Selector:          app=orders
Type:              ClusterIP
IP:                10.105.120.45
Port:              <unset>  80/TCP
TargetPort:        9090/TCP
Endpoints:         <none>
```
*The Service has `Endpoints: <none>`, meaning no Pods match the selector.*

---

### Step 4: Compare Pod Labels with Service Selector (Root Cause Discovery)
```bash
kubectl get pods --show-labels -l app=order-service
```
**Observation:**
- **Pod Label:** `app=order-service`
- **Service Selector:** `app=orders` (Mismatch!)
- **Container Port:** `containerPort: 80`
- **Service TargetPort:** `targetPort: 9090` (Mismatch!)

---

## 3. Root Cause Analysis (RCA)

1. **Root Cause 1 (Selector Mismatch):** The Service `spec.selector` had `app: orders`, whereas the Deployment Pod template had `app: order-service`. Because no Pods matched `app: orders`, Kubernetes created an empty EndpointSlice (`<none>`).
2. **Root Cause 2 (TargetPort Mismatch):** The Service `spec.ports.targetPort` was set to `9090`, while the NGINX container listens on port `80`.

---

## 4. Fix Applied

Updated the manifest in [`fixed-ingress-service.yaml`](file:///Users/srividya/devops-assign/troubleshooting/fixed-ingress-service.yaml):
```diff
 apiVersion: v1
 kind: Service
 metadata:
   name: order-service
 spec:
   type: ClusterIP
   selector:
-    app: orders
+    app: order-service
   ports:
   - port: 80
-    targetPort: 9090
+    targetPort: 80
```

Apply the fix:
```bash
kubectl apply -f troubleshooting/fixed-ingress-service.yaml
```

---

## 5. Verification After Fix

### Step 1: Check Service Endpoints
```bash
kubectl get endpoints order-service
```
**Output:**
```text
NAME            ENDPOINTS                       AGE
order-service   10.244.0.52:80,10.244.0.53:80   45s
```

### Step 2: Test End-to-End Ingress Request
```bash
curl -i -H "Host: orders.local" http://192.168.49.2/orders
```
**Output:**
```http
HTTP/1.1 200 OK
Date: Wed, 07 Oct 2026 18:27:00 GMT
Content-Type: text/html
Content-Length: 53
Connection: keep-alive

<h1>🛍️ Order Service API Online (HTTP 200)</h1>
```

---

## 6. Summary Comparison: Before vs After

| Metric / Check | Before Fix (Broken) | After Fix (Resolved) |
| :--- | :--- | :--- |
| **Service Endpoints** | `<none>` | `10.244.0.52:80, 10.244.0.53:80` |
| **Ingress Backend State** | `<error: endpoints not found>` | `order-service:80 (10.244.0.52:80, 10.244.0.53:80)` |
| **HTTP Status Code** | `503 Service Temporarily Unavailable` | `200 OK` |
| **Response Payload** | Nginx 503 error page | `<h1>🛍️ Order Service API Online (HTTP 200)</h1>` |
