# Troubleshooting Common Kubernetes Issues: Complete Catalog & Playbook

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**Course/Session:** Session 14 - Kubernetes Troubleshooting  

---

## 1. CrashLoopBackOff

### Identification & Symptoms:
- **Status:** `CrashLoopBackOff` or `Error`.
- **Restarts:** Incrementing rapidly (e.g. `Restarts: 5`).
- **Meaning:** The container started, executed, and exited immediately with a non-zero error code. Kubelet restarts it with an exponential backoff delay (10s, 20s, 40s... up to 5 min).

### Investigation Steps:
```bash
kubectl get pods
kubectl logs <pod-name> --previous
kubectl describe pod <pod-name>
```

### Root Causes:
1. Application crashed due to missing required environment variable or configuration file.
2. Port binding conflict inside container.
3. Memory limit exceeded (`OOMKilled: true` with exit code 137).
4. Entrypoint script typo or command exiting immediately (e.g. bash script finished).

### Fix & Verification:
- Add missing configuration/secrets, fix application code, or ensure continuous background processes (`daemon off;` or long-running service).

---

## 2. ImagePullBackOff / ErrImagePull

### Identification & Symptoms:
- **Status:** `ImagePullBackOff` or `ErrImagePull`.
- **Meaning:** Kubelet failed to pull the specified container image from the container registry.

### Investigation Steps:
```bash
kubectl describe pod <pod-name>
# Inspect Events section at bottom
```
**Sample Event:**
```text
Failed to pull image "nginx:version-9999": rpc error: code = NotFound desc = failed to pull and unpack image: not found
```

### Root Causes:
1. Typo in image name or tag.
2. Private registry requiring `imagePullSecrets` which is missing or unauthorized.
3. Network timeout or registry rate limiting (e.g., Docker Hub 429).

### Fix & Verification:
- Correct the image repository/tag in YAML or attach valid `imagePullSecrets`.

---

## 3. Pending Pod State

### Identification & Symptoms:
- **Status:** `Pending`.
- **Meaning:** The Pod cannot be scheduled onto any worker node by the `kube-scheduler`.

### Investigation Steps:
```bash
kubectl describe pod <pod-name>
kubectl get nodes
```
**Sample Event:**
```text
0/1 nodes are available: 1 Insufficient cpu. preemption: 0/1 nodes are available: 1 No preemption victims found for incoming pod.
```

### Root Causes:
1. **Insufficient Resources:** Container `resources.requests.cpu` or `requests.memory` exceed total allocatable capacity on any node.
2. **Node Affinity / NodeSelector:** Target node labels do not match `spec.nodeSelector`.
3. **Taints and Tolerations:** Node has a taint (e.g., `node-role.kubernetes.io/master:NoSchedule`) without matching toleration.
4. **Unbound PVC:** Pod references a PVC that has not yet been bound to a PV.

### Fix & Verification:
- Adjust resource requests to realistic values, resolve node labels, or ensure PVCs are Bound.

---

## 4. ContainerCreating State

### Identification & Symptoms:
- **Status:** Stuck in `ContainerCreating` for minutes.

### Investigation Steps:
```bash
kubectl describe pod <pod-name>
```

### Root Causes:
1. Volume mount failure: Referenced Secret, ConfigMap, or PVC does not exist or cannot be attached.
2. CNI IP allocation bottleneck or exhausted IP pool.

### Fix & Verification:
- Create the referenced ConfigMap/Secret/PVC or check CNI node agent logs.

---

## 5. Service Connectivity Issues

### Identification & Symptoms:
- Client receives `Connection Refused`, `HTTP 503`, or timeout when contacting a Service.

### Investigation Steps:
```bash
kubectl get endpoints <service-name>
kubectl describe svc <service-name>
kubectl get pods --show-labels
```

### Root Causes:
1. **Selector Mismatch:** `spec.selector` on Service does not match Pod labels. Result: `Endpoints: <none>`.
2. **TargetPort Mismatch:** `spec.ports.targetPort` does not match the port exposed in the container (`containerPort`).

### Fix & Verification:
- Update Service selector and targetPort to match Pod labels and listening port.

---

## 6. DNS Resolution Issues

### Identification & Symptoms:
- `nslookup` returns `Server: 10.96.0.10 Can't find <name>: Non-existent domain`.

### Investigation Steps:
```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
kubectl logs -n kube-system -l k8s-app=kube-dns
kubectl exec -it <pod-name> -- cat /etc/resolv.conf
```

### Root Causes:
1. Querying incorrect FQDN across namespaces (must use `<service>.<namespace>.svc.cluster.local`).
2. CoreDNS pods in `CrashLoopBackOff` or blocked by NetworkPolicy.

---

## 7. Pod Networking Issues

### Identification & Symptoms:
- Pods on different nodes cannot communicate or ping each other.

### Investigation Steps:
```bash
kubectl get pods -o wide
kubectl get networkpolicies
```

### Root Causes:
1. CNI plugin daemonset (Calico, Flannel, Cilium) crashed or not running.
2. Misconfigured `NetworkPolicy` blocking Ingress/Egress traffic.

---

## 8. Configuration Issues (ConfigMap / Secret Key Missing)

### Identification & Symptoms:
- Pod fails to start with `CreateContainerConfigError`.

### Investigation Steps:
```bash
kubectl describe pod <pod-name>
```
**Sample Event:**
```text
Error: configmap "nonexistent-configmap" not found
```

### Root Causes:
- Typo in `configMapKeyRef.name` or `key`.

### Fix & Verification:
- Ensure the ConfigMap exists before creating the Pod, or set `optional: true`.
