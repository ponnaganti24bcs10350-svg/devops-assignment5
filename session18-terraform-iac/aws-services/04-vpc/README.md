# AWS Virtual Private Cloud (VPC) - Networking Guide

**Student:** Srividya Ponnaganti  
**Enrollment:** 24BCS10350  
**Domain:** Cloud Network Architecture & Isolation  

---

## 1. What is an AWS VPC?

**Amazon Virtual Private Cloud (Amazon VPC)** allows you to provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. You have complete control over your virtual networking environment, including selection of your IP address range, creation of subnets, and configuration of route tables and network gateways.

```
+-----------------------------------------------------------------------------------------+
|                               AWS Region: us-east-1                                     |
|                                                                                         |
|  +--------------------------- VPC: 10.0.0.0/16 (DevOps-VPC) -------------------------+  |
|  |                                                                                   |  |
|  |   +--------------------- Public Subnet (10.0.1.0/24 - AZ-1a) -----------------+   |  |
|  |   | Route: 0.0.0.0/0 -> Internet Gateway (igw-xxxx)                           |   |  |
|  |   | [ ALB / Bastion Host ] ------> [ NAT Gateway (eip-xxxx) ]                 |   |  |
|  |   +---------------------------------------------------------------------------+   |  |
|  |                                                        |                          |  |
|  |                                                        v Outbound Internet Only   |  |
|  |   +--------------------- Private Subnet (10.0.2.0/24 - AZ-1b) ----------------+   |  |
|  |   | Route: 0.0.0.0/0 -> NAT Gateway (nat-xxxx)                                |   |  |
|  |   | [ EC2 Backend App Pods / Microservices ]                                  |   |  |
|  |   +---------------------------------------------------------------------------+   |  |
|  |                                                                                   |  |
|  |   +--------------------- Database Subnet (10.0.3.0/24 - AZ-1c) ---------------+   |  |
|  |   | Route: Local VPC Only (10.0.0.0/16) (Isolated)                            |   |  |
|  |   | [ Amazon RDS Multi-AZ / Aurora Cluster ]                                  |   |  |
|  |   +---------------------------------------------------------------------------+   |  |
|  +-----------------------------------------------------------------------------------+  |
|                                         |                                               |
|                                         v                                               |
|                            [ Internet Gateway (IGW) ]                                   |
|                                         |                                               |
|                                         v                                               |
|                                     (Internet)                                          |
+-----------------------------------------------------------------------------------------+
```

---

## 2. Core VPC Networking Components

### 2.1 CIDR Block (Classless Inter-Domain Routing)
* Defines the private IPv4 range for your VPC (e.g., `10.0.0.0/16` gives 65,536 addresses).
* **AWS Subnet Reserved IPs:** In any subnet CIDR block (e.g., `10.0.1.0/24`), AWS reserves **5 IP addresses**:
  1. `10.0.1.0`: Network address.
  2. `10.0.1.1`: VPC router address.
  3. `10.0.1.2`: Reserved for DNS.
  4. `10.0.1.3`: Reserved by AWS for future use.
  5. `10.0.1.255`: Network broadcast address.
  *(A `/24` subnet has 256 - 5 = 251 usable IPs).*

### 2.2 Subnets
* A range of IP addresses within your VPC bounded to a single **Availability Zone (AZ)**.
* Spanning subnets across multiple AZs provides **High Availability (HA)** and disaster resilience.

### 2.3 Route Tables
* A set of rules (routes) that determine where network traffic from your subnet or gateway is directed.
* Every VPC has a default **Main Route Table** with a local route:
  `Destination: 10.0.0.0/16 -> Target: local`

### 2.4 Internet Gateway (IGW)
* A horizontally scaled, redundant, and highly available VPC component that enables communication between your VPC and the Internet.
* Performs **Network Address Translation (1:1 NAT)** for instances with public IPv4 addresses.

### 2.5 NAT Gateway (Network Address Translation)
* A managed AWS service that enables instances in a **private subnet** to connect to the internet or other AWS services, but prevents the internet from initiating a connection with those instances.
* Must be deployed in a **public subnet** with an allocated **Elastic IP (EIP)**.

---

## 3. Public vs. Private Subnets

| Characteristic | Public Subnet | Private Subnet |
| :--- | :--- | :--- |
| **Internet Access** | Direct two-way (Inbound & Outbound) via Internet Gateway. | Outbound-only via NAT Gateway; No direct inbound from internet. |
| **Route Table Target** | `0.0.0.0/0 -> igw-xxxx` | `0.0.0.0/0 -> nat-xxxx` |
| **Public IP Assignment** | Auto-assign public IPv4 enabled. | Private IPv4 only. |
| **Typical Workloads** | Public Load Balancers (ALB/NLB), Bastion / Jump hosts. | Backend APIs, Application servers, Microservices, DB clusters. |

---

## 4. Security Layers: Security Groups vs. Network ACLs

```
[ Internet ]
     |
     v
+-------------------------------------------------------+
| Subnet Boundary: Network ACL (NACL)                   |  <-- Stateless (Inbound & Outbound Rules evaluated)
+-------------------------------------------------------+
     |
     v
+-------------------------------------------------------+
| Instance Boundary: Security Group                     |  <-- Stateful (Return traffic automatically allowed)
+-------------------------------------------------------+
     |
     v
[ EC2 Instance / Container ]
```

### Detailed Comparison:

| Feature | Security Group (SG) | Network ACL (NACL) |
| :--- | :--- | :--- |
| **Operating Level** | Instance / Network Interface (ENI) level | Subnet level |
| **State Tracking** | **Stateful:** Return traffic is automatically allowed. | **Stateless:** Outbound return traffic must be explicitly allowed. |
| **Rule Types** | **Allow rules only** (No Deny rules possible). | **Allow AND Deny rules** supported. |
| **Rule Evaluation** | All rules are evaluated simultaneously before permitting traffic. | Rules evaluated in numerical order (lowest numbered rule first). |
| **Default Configuration** | All inbound denied; All outbound allowed. | Default NACL allows all inbound/outbound; Custom NACL denies all. |

---

## 5. Standard Multi-Tier VPC Architecture Blueprint

1. **Tier 1 (Public Subnet):** Internet-facing Application Load Balancer (ALB) across 2+ AZs.
2. **Tier 2 (Private Subnet):** EC2 Auto Scaling Group or EKS worker nodes hosting containerized backend applications.
3. **Tier 3 (Database Subnet):** Isolated Amazon RDS Aurora database deployed in Multi-AZ without internet access.
