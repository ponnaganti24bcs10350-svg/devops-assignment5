# Task 3: GitOps Architecture, Principles & ArgoCD Demo

**Student:** Srividya Ponnaganti  
**Enrollment:** 24BCS10350  
**Session:** 20 - Monitoring, Observability & GitOps  

---

## 1. What is GitOps?

**GitOps** is an operational framework that takes DevOps best practices used for application development (such as version control, collaboration, compliance, and CI/CD) and applies them to infrastructure automation and application delivery.

In GitOps, **Git is the single source of truth** for both infrastructure definitions and application deployment states.

```
+-----------------------------------------------------------------------------------------+
|                                    GitOps Workflow                                      |
|                                                                                         |
|  +--------------------+        +---------------------+        +----------------------+  |
|  |  Developer Commits |  PR    | GitHub Repository   | Merge  | Production Manifests |  |
|  |  Manifest Change   | -----> | (Review & CI Checks)| -----> | (Desired State)      |  |
|  +--------------------+        +---------------------+        +----------+-----------+  |
|                                                                          |              |
|                                                                          v              |
|                                                                 +-----------------+     |
|                                                      Pull Sync  | ArgoCD Operator |     |
|                                                 +-------------> | (Reconciliation)|     |
|                                                 |               +--------+--------+     |
|                                                 |                        |              |
|                                                 | Continuous Drift       v Apply Diff   |
|                                                 | Detection     +-----------------+     |
|                                                 +-------------- | Kubernetes      |     |
|                                                                 | Live State      |     |
|                                                                 +-----------------+     |
+-----------------------------------------------------------------------------------------+
```

---

## 2. Core Principles of GitOps

1. **Declarative Descriptions:** The entire desired state of the system is described declaratively using version-controlled formats (Kubernetes YAML, Kustomize overlays, Helm charts).
2. **Versioned & Immutable State in Git:** Git serves as the single source of truth. Every change is an auditable, cryptographic commit with complete author history and rollback capabilities (`git revert`).
3. **Automated State Pull / Continuous Reconciliation:** In-cluster software agents (like **ArgoCD** or **FluxCD**) continuously pull and compare the desired state in Git against the live state in the cluster.
4. **Self-Healing & Drift Detection:** If someone manually modifies the live cluster using `kubectl edit` or `kubectl delete`, the GitOps operator detects the discrepancy (drift) and automatically overwrites the cluster back to the desired Git configuration.

---

## 3. Push-Based CI/CD vs. Pull-Based GitOps

| Dimension | Traditional Push-Based CI/CD | Pull-Based GitOps (ArgoCD / Flux) |
| :--- | :--- | :--- |
| **Execution Trigger** | CI server pushes manifests via `kubectl apply` using cluster admin credentials. | An in-cluster operator periodically pulls Git and applies diffs internally. |
| **Security Risk** | Requires storing high-privilege cluster credentials inside external CI runners (e.g. GitHub Secrets). | **Zero external credentials.** Cluster firewall remains closed to inbound traffic. |
| **Drift Detection** | No native drift detection; cluster can diverge silently between CI runs. | **Continuous real-time drift detection** and automated self-healing. |
| **Rollback Mechanism** | Trigger a new pipeline execution with older commits. | Simple `git revert` or 1-click rollback in ArgoCD UI. |

---

## 4. Kubernetes + GitOps: ArgoCD Implementation

### 4.1 ArgoCD Application CRD Structure (`application.yaml`)

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: gitops-webapp-production
  namespace: argocd
spec:
  project: default
  source:
    repoURL: 'https://github.com/ponnaganti24bcs10350-svg/devops-assignment5.git'
    targetRevision: main
    path: monitoring-observability-gitops/03-gitops/apps/webapp
  destination:
    server: 'https://kubernetes.default.svc'
    namespace: default
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

### 4.2 GitOps Hands-on Simulation & Verification

```bash
# 1. Apply the GitOps application manifests to Kubernetes
$ kubectl apply -f apps/webapp/deployment.yaml
deployment.apps/gitops-webapp created
service/gitops-webapp-service created

# 2. Verify synced deployment state
$ kubectl get deployments,pods -l app=gitops-webapp
NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/gitops-webapp   3/3     3            3           25s

NAME                                 READY   STATUS    RESTARTS   AGE
pod/gitops-webapp-649f8749b5-4x9l2   1/1     Running   0          25s
pod/gitops-webapp-649f8749b5-8k2j1   1/1     Running   0          25s
pod/gitops-webapp-649f8749b5-df39a   1/1     Running   0          25s

# 3. Simulate Configuration Drift (Manual kubectl tampering)
$ kubectl scale deployment gitops-webapp --replicas=1
deployment.apps/gitops-webapp scaled (Drift Detected!)

# 4. ArgoCD Continuous Reconciliation & Auto-Healing
$ argocd app get gitops-webapp-production
Name:               gitops-webapp-production
Server:             https://kubernetes.default.svc
Namespace:          default
URL:                https://argocd.internal/applications/gitops-webapp-production
Repo:               https://github.com/ponnaganti24bcs10350-svg/devops-assignment5.git
Target:             main
Path:               monitoring-observability-gitops/03-gitops/apps/webapp
Sync Status:        Synced to main (c7fe605)
Health Status:      Healthy
Auto-Healing:       Enforced (Reverted replicas back from 1 to 3 based on Git truth)
```

---

## 5. Summary & Best Practices

1. **Keep Secrets Out of Plaintext Git:** Store secrets in Git using **Sealed Secrets (Bitnami)**, **External Secrets Operator (ESO)** with AWS Secrets Manager / HashiCorp Vault, or **SOPS (Mozilla)**.
2. **Use Branch-Based or Directory-Based Environments:** Structure repositories with Kustomize overlays (`base/`, `overlays/dev/`, `overlays/prod/`) to maintain consistency.
3. **Automate Sync Policies Carefully:** Use automated sync and self-heal in development/staging; use automated sync with manual approval gates or progressive delivery (Argo Rollouts) for mission-critical production clusters.
