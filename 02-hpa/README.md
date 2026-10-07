# Kubernetes Horizontal Pod Autoscaler (HPA) Hands-on

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**Course/Session:** Session 13 - Kubernetes Storage, HPA & Probes  

---

## 1. Overview of Horizontal Pod Autoscaling (HPA)

The **Horizontal Pod Autoscaler (HPA)** automatically scales the number of Pod replicas in a Deployment, ReplicaSet, or StatefulSet based on observed CPU utilization, memory consumption, or custom metrics collected by the Kubernetes **Metrics Server**.

### Scaling Algorithm Formula:
$$\text{Desired Replicas} = \left\lceil \text{Current Replicas} \times \left( \frac{\text{Current Metric Value}}{\text{Target Metric Value}} \right) \right\rceil$$

---

## 2. Step-by-Step Hands-on Workflow

### Step 1: Enable Metrics Server in Minikube
```bash
minikube addons enable metrics-server
kubectl get deployment metrics-server -n kube-system
```

### Step 2: Deploy Target Application & Service
Deploy the `php-apache` image with defined resource requests:
```bash
kubectl apply -f 02-hpa/app-deployment.yaml
kubectl get deployment php-apache
```

### Step 3: Configure HPA
Apply the HPA resource configuring auto-scaling from 1 to 5 replicas when average CPU exceeds 50%:
```bash
kubectl apply -f 02-hpa/hpa.yaml
kubectl get hpa php-apache
```

### Step 4: Generate Application Load
Deploy the `load-generator` Pod to flood the `php-apache` service with continuous HTTP queries:
```bash
kubectl apply -f 02-hpa/load-generator.yaml
```

### Step 5: Observe Live Scaling & Utilization
Monitor the metrics and Pod replicas:
```bash
# Check HPA status
kubectl get hpa php-apache --watch

# Check CPU consumption per Pod
kubectl top pods -l run=php-apache

# Describe HPA event details
kubectl describe hpa php-apache

# View scaled Pod instances
kubectl get pods -l run=php-apache
```

### Step 6: Scale-Down Verification
Stop the load generator and observe the HPA automatically scaling back down to 1 replica after the stabilization window:
```bash
kubectl delete pod load-generator
```

---

## 3. Useful Troubleshooting & Monitoring Commands

| Command | Purpose |
| :--- | :--- |
| `kubectl get hpa` | View current target metrics, min/max limits, and replica counts |
| `kubectl describe hpa php-apache` | View autoscaling conditions, events, and scaling reasons |
| `kubectl top pods` | Inspect real-time CPU (milli-cores) and memory (MiB) usage |
| `kubectl top nodes` | Inspect cluster-wide node resource consumption |
| `kubectl get events --sort-by=.metadata.creationTimestamp` | Track scale-up and scale-down controller events |
