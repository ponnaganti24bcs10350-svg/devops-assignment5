# AWS Elastic Compute Cloud (EC2) - Compute Guide

**Student:** Srividya Ponnaganti  
**Enrollment:** 24BCS10350  
**Domain:** AWS Cloud Compute Infrastructure  

---

## 1. What is Amazon EC2?

**Amazon Elastic Compute Cloud (Amazon EC2)** provides scalable, on-demand virtual compute capacity in the AWS Cloud. It eliminates the need to invest in physical hardware upfront, allowing you to build and run applications faster with pay-as-you-go pricing.

```
+-----------------------------------------------------------------------------------+
|                                  Amazon EC2 Architecture                          |
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  | AWS VPC (Virtual Private Cloud)                                              |  |
|  |                                                                             |  |
|  |   +----------------------- EC2 Instance -----------------------+            |  |
|  |   |                                                            |            |  |
|  |   |  +-------------------+              +-------------------+  |            |  |
|  |   |  |     AMI Boot      |              |  Instance Type    |  |            |  |
|  |   |  | (Ubuntu/RHEL/AL2) |              | (t3.micro, c6g...) |  |            |  |
|  |   |  +---------+---------+              +---------+---------+  |            |  |
|  |   |            |                                  |            |            |  |
|  |   |            +-----------------+----------------+            |            |  |
|  |   |                              |                             |            |  |
|  |   |                              v                             |            |  |
|  |   |     +------------------------------------------------+     |            |  |
|  |   |     | Attached EBS Volume (Root /dev/xvda, gp3)      |     |            |  |
|  |   |     +------------------------------------------------+     |            |  |
|  |   |                              |                             |            |  |
|  |   |     +------------------------------------------------+     |            |  |
|  |   |     | Virtual Firewall: Security Group (In/Outbound) |     |            |  |
|  |   |     +------------------------------------------------+     |            |  |
|  |   +------------------------------------------------------------+            |  |
|  +-----------------------------------------------------------------------------+  |
+-----------------------------------------------------------------------------------+
```

---

## 2. Core EC2 Building Blocks

### 2.1 Amazon Machine Image (AMI)
* An **AMI** is a pre-configured template that contains the software configuration (operating system, application server, and applications) required to launch your instance.
* **Types of AMIs:**
  1. **AWS Quick Start / Community AMIs:** Pre-built OS images (Amazon Linux 2023, Ubuntu 22.04 LTS, Red Hat Enterprise Linux, Windows Server).
  2. **AWS Marketplace AMIs:** Commercial appliances (Cisco CSR, WordPress by Bitnami, Datadog agents).
  3. **Custom AMIs (Golden Images):** User-created AMIs hardened with corporate security policies, dependencies, and configurations.

### 2.2 EC2 Instance Types
AWS classifies instance families based on compute, memory, and storage optimization:

| Family | Classification | Example Types | Ideal Workloads |
| :--- | :--- | :--- | :--- |
| **T / M** | General Purpose | `t3.micro`, `t4g.small`, `m6i.large` | Web servers, small databases, dev/test environments. |
| **C** | Compute Optimized | `c6i.xlarge`, `c7g.2xlarge` | High-performance batch processing, media transcoding, scientific modeling. |
| **R / X** | Memory Optimized | `r6i.xlarge`, `r7g.4xlarge` | In-memory caches (Redis/Memcached), large relational databases, big data analytics. |
| **I / D** | Storage Optimized | `i3.large`, `d2.xlarge` | Data warehousing, NoSQL distributed file systems (Cassandra, Kafka). |
| **G / P** | Accelerated Computing | `g5.xlarge`, `p4d.24xlarge` | Machine Learning training, LLM inference, 3D rendering. |

### 2.3 Key Pairs
* Amazon EC2 uses **public-key cryptography** to encrypt and decrypt login credentials.
* **Linux Instances:** AWS injects the public key into `~/.ssh/authorized_keys`. You connect securely via SSH using your private key (`.pem` or `.ppk` file):
  ```bash
  ssh -i my-key.pem ec2-user@<public-ip>
  ```
* **Windows Instances:** The private key is used to decrypt the administrator password.

### 2.4 Security Groups
* Acts as a **stateful virtual firewall** for your EC2 instances to control incoming and outgoing network traffic.
* **Key Properties:**
  * **Stateful:** If you send an outbound request, the incoming response is automatically allowed regardless of inbound rules.
  * **Default Deny:** All inbound traffic is blocked by default until explicit Allow rules are added.
  * You cannot create **Deny** rules in Security Groups (use Network ACLs for that).

### 2.5 Amazon Elastic Block Store (EBS)
* Provides raw, persistent block-level storage volumes for use with EC2 instances.
* **Volume Types:**
  * **gp3 / gp2 (General Purpose SSD):** Baseline for boot volumes and general workloads with independent IOPS and throughput scaling.
  * **io2 / io1 (Provisioned IOPS SSD):** High-performance, latency-sensitive database workloads.
  * **st1 (Throughput Optimized HDD):** Big data, log processing, data warehousing.
  * **sc1 (Cold HDD):** Infrequently accessed data, lowest cost.
* **Snapshots:** Point-in-time backups of EBS volumes stored incrementally in Amazon S3.

### 2.6 Public vs. Private vs. Elastic IP

| IP Type | Persistence | Publicly Reachable? | Description |
| :--- | :--- | :--- | :--- |
| **Private IP** | Persistent for instance life | No (VPC internal only) | Assigned automatically to every instance in a subnet. |
| **Public IP** | Lost on Stop / Start | Yes (Internet reachable) | Dynamic IP assigned automatically from AWS public pool. |
| **Elastic IP (EIP)** | Static (fixed until released) | Yes (Internet reachable) | Static public IPv4 address that can be rapidly re-associated to other instances. |

---

## 3. EC2 Instance Lifecycle

```
             +------------+
             |  Pending   |
             +-----+------+
                   |
                   v
             +------------+       Stop
       +---->|  Running   |----------------->+
       |     +-----+------+                  |
       |           |                         v
 Start |           | Reboot            +------------+
       |           v                   |  Stopping  |
       |     +------------+            +-----+------+
       +-----|  Rebooting |                  |
             +------------+                  v
                                       +------------+
                                       |  Stopped   |
                                       +-----+------+
                                             |
                               Terminate     v
                                       +---------------+
                                       | Shutting-down |
                                       +-------+-------+
                                               |
                                               v
                                       +---------------+
                                       |  Terminated   |
                                       +---------------+
```

1. **Pending:** AWS prepares the host hardware, network interface, and AMI initialization.
2. **Running:** The instance is up and operational; billing begins.
3. **Stopping / Stopped:** The instance is shut down (RAM cleared, private IP retained, EBS volumes persist).
4. **Shutting-down / Terminated:** The instance is permanently deleted; associated EBS root volumes are deleted (if `DeleteOnTermination` is true).

---

## 4. Common Use Cases

1. **Web and Application Hosting:** Running Nginx, Apache, Node.js, Spring Boot, or Django microservices behind an Application Load Balancer.
2. **Self-Managed Databases:** Running PostgreSQL, MongoDB, or Cassandra clusters with Provisioned IOPS (io2) EBS storage.
3. **Batch Computing & Worker Queues:** Consuming jobs from Amazon SQS using Auto Scaling Groups of Spot EC2 instances for cost optimization.
4. **DevSecOps Runners:** Hosting dedicated, self-hosted GitHub Actions or Jenkins CI/CD runners.
