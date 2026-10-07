# Kubernetes Volumes: Architecture, Types & Dynamic Provisioning

**Student Name:** Srividya Ponnaganti  
**Enrollment Number:** 24BCS10350  
**Course/Session:** Session 13 - Kubernetes Storage, HPA & Probes  

---

## 1. Overview of Kubernetes Storage Architecture

By default, container filesystems are ephemeral. When a container crashes or is deleted, all local data is lost. Kubernetes solves this with **Volumes**, which abstract storage backends and provide varying lifecycles, persistence guarantees, and access modes.

```mermaid
flowchart TD
    subgraph ClusterStorage ["Cluster Storage Layer"]
        SC[StorageClass<br/>Provisioner: k8s.io/minikube-hostpath]
        PV[PersistentVolume (PV)<br/>Capacity: 5Gi, Mode: RWO]
        SC -->|Dynamically Provisions| PV
    end

    subgraph UserNamespace ["Application Namespace"]
        PVC[PersistentVolumeClaim (PVC)<br/>Requests: 5Gi, Mode: RWO]
        Pod[Application Pod]
        VolumeMount["VolumeMount: /var/lib/data"]
        
        PVC -->|Binds to| PV
        Pod -->|References| PVC
        Pod --> VolumeMount
    end
```

---

## 2. Deep Dive: Kubernetes Volume Types

### 1. `emptyDir`
- **Definition:** An ephemeral storage volume created when a Pod is assigned to a Node. It exists for the lifetime of that Pod.
- **Persistence:** Data is lost when the Pod is deleted from the node, but survives container crashes within the same pod.
- **Use Cases:**
  - Scratch space (e.g. disk-based merge sort, temporary computation cache).
  - Multi-container communication (e.g., logging sidecar reading logs produced by an app container).
  - Temporary download buffer before uploading to S3.

#### Example YAML:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-emptydir-demo
spec:
  containers:
  - name: producer
    image: alpine
    command: ["/bin/sh", "-c", "echo 'Hello from producer' > /scratch/data.txt; sleep 3600"]
    volumeMounts:
    - name: scratch-volume
      mountPath: /scratch
  - name: consumer
    image: alpine
    command: ["/bin/sh", "-c", "sleep 2; cat /scratch/data.txt; sleep 3600"]
    volumeMounts:
    - name: scratch-volume
      mountPath: /scratch
  volumes:
  - name: scratch-volume
    emptyDir: {}
```

---

### 2. `hostPath`
- **Definition:** Mounts a file or directory from the host Node's filesystem directly into the Pod.
- **Persistence:** Persists as long as the node exists. If the pod is rescheduled to a different node, it accesses that node's local filesystem (data is node-bound).
- **Use Cases:**
  - System DaemonSets needing access to node logs (e.g., Fluentd reading `/var/log`).
  - Container runtime inspection (e.g., tools reading `/var/lib/docker`).
  - Node hardware monitoring (e.g., cAdvisor accessing `/sys`).

#### Example YAML:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-hostpath-demo
spec:
  containers:
  - name: log-reader
    image: alpine
    command: ["/bin/sh", "-c", "tail -f /node-logs/messages || sleep 3600"]
    volumeMounts:
    - name: host-log-volume
      mountPath: /node-logs
  volumes:
  - name: host-log-volume
    hostPath:
      path: /var/log
      type: Directory
```

---

### 3. `PersistentVolume` (PV)
- **Definition:** A piece of storage in the cluster provisioned by an administrator or dynamically provisioned using Storage Classes. It is a cluster-scoped resource with an independent lifecycle from any Pod.
- **Properties:**
  - Capacity (e.g., `10Gi`)
  - Access Modes (`ReadWriteOnce`, `ReadOnlyMany`, `ReadWriteMany`)
  - Reclaim Policy (`Retain`, `Delete`, `Recycle`)
  - Storage Backend (AWS EBS, GCP Persistent Disk, NFS, Ceph, iSCSI, CSI)

#### Example YAML (Static PV):
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: static-pv-5gb
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: manual
  hostPath:
    path: /mnt/data
```

---

### 4. `PersistentVolumeClaim` (PVC)
- **Definition:** A request for storage by a user/developer in a specific namespace. It specifies the desired size, access modes, and optionally a StorageClass.
- **Binding:** Kubernetes control plane (PersistentVolume Controller) matches PVCs to matching PVs (or triggers dynamic provisioning) and binds them 1-to-1.

#### Example YAML:
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-pvc-claim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: standard
```

---

### 5. `StorageClass` & Dynamic Provisioning
- **Definition:** A `StorageClass` provides a way for administrators to describe the "classes" of storage they offer (e.g., `fast-ssd`, `standard-hdd`, `backup-cold`).
- **Dynamic Provisioning:** Eliminates the need for cluster admins to pre-create manual PVs. When a developer creates a PVC requesting a StorageClass, the cloud CSI (Container Storage Interface) or provisioner automatically provisions the underlying storage volume and creates the corresponding PV on the fly.

#### Example StorageClass YAML:
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-storage
provisioner: k8s.io/minikube-hostpath # or ebs.csi.aws.com, pd.csi.storage.gke.io
reclaimPolicy: Delete
volumeBindingMode: Immediate
```

---

## 3. Comparison Matrix of Kubernetes Volume Types

| Feature | `emptyDir` | `hostPath` | `PersistentVolume` (PV) | `PersistentVolumeClaim` (PVC) |
| :--- | :--- | :--- | :--- | :--- |
| **Scope** | Pod-level (local) | Node-level (local) | Cluster-wide | Namespace-scoped |
| **Lifecycle** | Tied to Pod lifecycle | Tied to Node filesystem | Independent of Pods | Bound to matched PV |
| **Persistence** | Ephemeral | Node-persistent | Durable persistent | Durable persistent |
| **Multi-Node Portability** | No | No (pinned to node) | Yes (Cloud/NFS/SAN) | Yes (references PV) |
| **Primary Audience** | Container sharing | System/Node agents | Cluster Administrators | Application Developers |
| **Dynamic Creation** | Automatic on Pod start | Direct node path mount | Via StorageClass provisioner | Triggers PV creation |

---

## 4. Volume Access Modes Explained

1. **`ReadWriteOnce` (RWO):** Volume can be mounted as read-write by a single Node. (Standard for block storage like AWS EBS, GKE PD).
2. **`ReadOnlyMany` (ROX):** Volume can be mounted as read-only by many Nodes simultaneously. (Golden images, static datasets).
3. **`ReadWriteMany` (RWX):** Volume can be mounted as read-write by many Nodes concurrently. (Shared filesystems like NFS, AWS EFS, CephFS).
4. **`ReadWriteOncePod` (RWOP):** Volume can be mounted as read-write by a single Pod across the entire cluster (Kubernetes v1.22+).
