# Session 18: Terraform & Infrastructure as Code Submission Report

**Student Name:** Srividya Ponnaganti  
**Enrollment ID:** 24BCS10350  
**Repository:** [devops-assignment5](https://github.com/ponnaganti24bcs10350-svg/devops-assignment5)  
**Date:** October 8, 2026  

---

## Executive Summary

This submission covers the comprehensive implementation and documentation for **Session 18: Terraform & Infrastructure as Code**, comprising:
1. **Task 1: Terraform AWS S3 Demo Project:** Complete modular Terraform infrastructure setup (`provider.tf`, `variables.tf`, `terraform.tfvars`, `main.tf`, `outputs.tf`, `README.md`) demonstrating the full Terraform lifecycle (`init`, `fmt`, `validate`, `plan`, `apply`, `show`, `output`, `destroy`).
2. **Task 2: AWS Core Services Research & Architecture Guides:** Five standalone research guides covering **IAM (Governance)**, **EC2 (Compute)**, **S3 (Storage)**, **VPC (Networking)**, and **DynamoDB & RDS (Databases)**.

---

## Deliverables Architecture & Directory Tree

```
devops-assign/
├── terraform-s3-demo/
│   ├── provider.tf             # AWS provider configuration and version constraints
│   ├── variables.tf            # Input variable declarations
│   ├── terraform.tfvars        # Parameter values definition
│   ├── main.tf                 # S3 bucket, versioning, encryption, and ACL blocks
│   ├── outputs.tf              # Output metadata attributes
│   └── README.md               # Detailed workflow guide
├── aws-services/
│   ├── 01-iam/
│   │   └── README.md           # IAM Governance, Users, Roles, Policies, Least Privilege
│   ├── 02-ec2/
│   │   └── README.md           # EC2 Compute, AMIs, Instance Types, SGs, EBS, Lifecycle
│   ├── 03-s3/
│   │   └── README.md           # S3 Object Storage, Classes, Versioning, Lifecycles, Encryption
│   ├── 04-vpc/
│   │   └── README.md           # VPC Networking, CIDRs, Subnets, Gateways, NACLs vs SGs
│   └── 05-dynamodb-rds/
│       └── README.md           # DynamoDB NoSQL vs RDS Relational Multi-AZ & Read Replicas
└── screenshots/
    ├── 43_terraform_init_plan.png
    ├── 44_terraform_apply_outputs.png
    ├── 45_terraform_destroy.png
    └── 46_aws_services_architecture.png
```

---

## Task 1: Terraform S3 Demo Implementation

### 1. File Structure & Configuration

- **[provider.tf](file:///Users/srividya/devops-assign/terraform-s3-demo/provider.tf):** Declares `hashicorp/aws` (~> 5.0) and assigns standard organizational default tags.
- **[variables.tf](file:///Users/srividya/devops-assign/terraform-s3-demo/variables.tf):** Defines variable types and defaults for `aws_region`, `bucket_name`, `environment`, `enable_versioning`, and `enable_encryption`.
- **[terraform.tfvars](file:///Users/srividya/devops-assign/terraform-s3-demo/terraform.tfvars):** Supplies concrete values for deployment.
- **[main.tf](file:///Users/srividya/devops-assign/terraform-s3-demo/main.tf):** Implements:
  - `aws_s3_bucket`: Root bucket resource with `force_destroy = true`.
  - `aws_s3_bucket_versioning`: Reversible object revision control.
  - `aws_s3_bucket_server_side_encryption_configuration`: AES-256 encryption at rest.
  - `aws_s3_bucket_ownership_controls`: Object ownership enforcement (`BucketOwnerEnforced`).
  - `aws_s3_bucket_public_access_block`: Blocks public ACLs and bucket policies.
- **[outputs.tf](file:///Users/srividya/devops-assign/terraform-s3-demo/outputs.tf):** Exposes bucket ID, ARN, domain name, and region.
- **[README.md](file:///Users/srividya/devops-assign/terraform-s3-demo/README.md):** Project manual.

### 2. Complete Terraform Lifecycle Execution

| Step | Command | Purpose & Result |
| :--- | :--- | :--- |
| **1. Init** | `terraform init` | Downloads AWS provider plugin and configures backend. |
| **2. Format** | `terraform fmt` | Formats all `.tf` files to canonical HashiCorp HCL style. |
| **3. Validate** | `terraform validate` | Validates syntax, arguments, and internal consistency. |
| **4. Plan** | `terraform plan` | Computes diff; plans creation of 5 resources. |
| **5. Apply** | `terraform apply -auto-approve` | Provisions infrastructure in AWS and writes state. |
| **6. Show** | `terraform show` | Reads and inspects state file (`terraform.tfstate`). |
| **7. Output** | `terraform output` | Queries outputs (ID, ARN, Domain Name, Region). |
| **8. Destroy** | `terraform destroy -auto-approve` | Destroys all 5 resources safely. |

### Evidence Screenshots:

#### 1. Initialization, Validation & Plan
![Terraform Init Plan](/Users/srividya/devops-assign/screenshots/43_terraform_init_plan.png)

#### 2. Apply & Output Verification
![Terraform Apply Outputs](/Users/srividya/devops-assign/screenshots/44_terraform_apply_outputs.png)

#### 3. State Inspection & Clean Destruction
![Terraform Destroy](/Users/srividya/devops-assign/screenshots/45_terraform_destroy.png)

---

## Task 2: AWS Services Research Guides

### 1. [01. IAM - Governance Guide](file:///Users/srividya/devops-assign/aws-services/01-iam/README.md)
* **What is IAM:** Global identity, authentication, and authorization control plane.
* **IAM Entities:** Users, Groups, Roles (STS temporary credentials), Policies (JSON documents).
* **Evaluation Logic:** Explicit Deny > Explicit Allow > Implicit Default Deny.
* **Least Privilege Principle:** Minimal necessary permissions to avoid lateral movement.
* **Best Practices:** Root account MFA, avoid hardcoded credentials, use instance profiles, enforce 90-day access key rotation, SCPs.

### 2. [02. EC2 - Compute Guide](file:///Users/srividya/devops-assign/aws-services/02-ec2/README.md)
* **What is EC2:** Resizable, on-demand compute capacity in the cloud.
* **Core Components:** AMIs, Instance Types (General Purpose, Compute, Memory, Storage, Accelerated), Key Pairs (SSH asymmetric keys), Security Groups (stateful virtual firewalls), EBS Volumes (gp3, io2, st1, sc1).
* **IP Addressing:** Private IP (internal VPC), Public IP (ephemeral), Elastic IP (persistent static IPv4).
* **Instance Lifecycle:** Pending &rarr; Running &rarr; Stopping &rarr; Stopped &rarr; Shutting-down &rarr; Terminated.

### 3. [03. S3 - Storage Guide](file:///Users/srividya/devops-assign/aws-services/03-s3/README.md)
* **What is S3:** Highly durable (11 9s) global object storage service.
* **Buckets & Objects:** Globally unique namespace, objects up to 5 TB with key, value, metadata, version ID.
* **Storage Classes:** Standard, Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier Instant/Flexible/Deep Archive.
* **Lifecycle Rules & Encryption:** Automated transitions, expiration, and SSE-S3 / SSE-KMS encryption.

### 4. [04. VPC - Networking Guide](file:///Users/srividya/devops-assign/aws-services/04-vpc/README.md)
* **What is VPC:** Logically isolated virtual network with custom CIDR ranges (e.g., `10.0.0.0/16`).
* **Subnets & Routing:** Public subnets (route to Internet Gateway) vs. Private subnets (route to NAT Gateway).
* **Security Layers:** Security Groups (stateful instance-level firewall) vs. Network ACLs (stateless subnet-level firewall).

### 5. [05. DynamoDB & RDS - Database Services Guide](file:///Users/srividya/devops-assign/aws-services/05-dynamodb-rds/README.md)
* **DynamoDB:** Fully managed serverless NoSQL key-value & document store with single-digit millisecond latency, Partition Keys, Sort Keys, GSIs/LSIs.
* **Amazon RDS:** Managed relational database supporting Aurora, PostgreSQL, MySQL, MariaDB, Oracle, SQL Server with Multi-AZ synchronous standby replication, Read Replicas, and automated backups.

### AWS Services Research Overview:
![AWS Services Architecture](/Users/srividya/devops-assign/screenshots/46_aws_services_architecture.png)

---

## Conclusion & Submission Verification

All requirements for Session 18 have been thoroughly completed, tested, formatted, and documented according to DevOps and cloud engineering standards.
