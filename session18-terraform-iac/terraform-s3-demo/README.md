# Session 18 - Task 1: Terraform S3 Demo

**Student:** Srividya Ponnaganti  
**Enrollment:** 24BCS10350  
**Project:** Infrastructure as Code (IaC) with Terraform & AWS S3  

---

## 1. Project Overview

This project demonstrates creating and managing an **Amazon S3 Bucket** using **Terraform (Infrastructure as Code)**. The infrastructure configuration follows AWS and HashiCorp best practices including default server-side encryption (AES-256), bucket versioning, bucket ownership controls, and public access blocking.

### Directory Structure
```
terraform-s3-demo/
├── main.tf           # S3 bucket, versioning, encryption, and public access block resources
├── variables.tf      # Input variable declarations with types and defaults
├── outputs.tf        # Output values (Bucket ID, ARN, Region, Domain Name)
├── provider.tf       # Terraform AWS provider declaration and version constraints
├── terraform.tfvars  # Environment-specific variable assignments
└── README.md         # Complete workflow documentation and commands
```

---

## 2. Infrastructure as Code Configuration Files

### `provider.tf`
Configures the HashiCorp AWS provider with required version constraints and default tags applied globally across all created resources.
```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      Project     = "DevOps-Terraform-Demo"
      ManagedBy   = "Terraform"
      Owner       = "Srividya Ponnaganti"
      Enrollment  = "24BCS10350"
      Environment = var.environment
    }
  }
}
```

### `variables.tf`
Defines parameterized inputs for AWS region, bucket naming, environment tagging, and feature flags.
```hcl
variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "bucket_name" {
  type    = string
  default = "devops-assignment-s3-demo-bucket-24bcs10350"
}

variable "environment" {
  type    = string
  default = "dev"
}

variable "enable_versioning" {
  type    = bool
  default = true
}

variable "enable_encryption" {
  type    = bool
  default = true
}
```

### `main.tf`
Defines the core AWS S3 resources:
1. `aws_s3_bucket`: Core bucket resource with `force_destroy = true`.
2. `aws_s3_bucket_versioning`: Enables object revision tracking.
3. `aws_s3_bucket_server_side_encryption_configuration`: Enforces AES256 server-side encryption.
4. `aws_s3_bucket_ownership_controls`: Enforces `BucketOwnerEnforced`.
5. `aws_s3_bucket_public_access_block`: Blocks public ACLs and bucket policies to prevent accidental data leaks.

### `outputs.tf`
Exposes the resulting infrastructure metadata:
```hcl
output "s3_bucket_id" {
  value = aws_s3_bucket.demo_bucket.id
}

output "s3_bucket_arn" {
  value = aws_s3_bucket.demo_bucket.arn
}

output "s3_bucket_domain_name" {
  value = aws_s3_bucket.demo_bucket.bucket_domain_name
}
```

---

## 3. Terraform Lifecycle & Execution Workflow

### Step 1: `terraform init`
Initializes the working directory, downloads the AWS provider plugin into `.terraform/`, and creates the lock file `.terraform.lock.hcl`.

```bash
$ terraform init

Initializing the backend...
Initializing provider plugins...
- Finding hashicorp/aws versions matching "~> 5.0"...
- Installing hashicorp/aws v5.42.0...
- Installed hashicorp/aws v5.42.0 (signed by HashiCorp)

Terraform has been successfully initialized!
```

---

### Step 2: `terraform fmt`
Formats the HCL code according to canonical style conventions.

```bash
$ terraform fmt
# Formats all .tf files in the directory
```

---

### Step 3: `terraform validate`
Validates the syntax, arguments, and internal consistency of the configuration files.

```bash
$ terraform validate
Success! The configuration is valid.
```

---

### Step 4: `terraform plan`
Creates an execution plan, reading current cloud state and computing the diff required to reach desired state.

```bash
$ terraform plan

Terraform used the selected providers to generate the following execution plan:

  # aws_s3_bucket.demo_bucket will be created
  + resource "aws_s3_bucket" "demo_bucket" {
      + arn                         = (known after apply)
      + bucket                      = "devops-assignment-s3-demo-bucket-24bcs10350"
      + bucket_domain_name          = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + region                      = (known after apply)
      + tags                        = {
          + "Assignment"  = "DevOps-Session-18"
          + "Environment" = "dev"
          + "Name"        = "devops-assignment-s3-demo-bucket-24bcs10350"
          + "Task"        = "Session-18-Terraform-S3"
          + "Tier"        = "Storage"
        }
    }

  # aws_s3_bucket_ownership_controls.demo_bucket_ownership will be created
  + resource "aws_s3_bucket_ownership_controls" "demo_bucket_ownership" { ... }

  # aws_s3_bucket_public_access_block.demo_bucket_public_access_block will be created
  + resource "aws_s3_bucket_public_access_block" "demo_bucket_public_access_block" { ... }

  # aws_s3_bucket_server_side_encryption_configuration.demo_bucket_encryption[0] will be created
  + resource "aws_s3_bucket_server_side_encryption_configuration" "demo_bucket_encryption" { ... }

  # aws_s3_bucket_versioning.demo_bucket_versioning will be created
  + resource "aws_s3_bucket_versioning" "demo_bucket_versioning" { ... }

Plan: 5 to add, 0 to change, 0 to destroy.
```

---

### Step 5: `terraform apply`
Applies the changes to create the real infrastructure in AWS and writes the state to `terraform.tfstate`.

```bash
$ terraform apply -auto-approve

aws_s3_bucket.demo_bucket: Creating...
aws_s3_bucket.demo_bucket: Creation complete after 2s [id=devops-assignment-s3-demo-bucket-24bcs10350]
aws_s3_bucket_ownership_controls.demo_bucket_ownership: Creating...
aws_s3_bucket_public_access_block.demo_bucket_public_access_block: Creating...
aws_s3_bucket_server_side_encryption_configuration.demo_bucket_encryption[0]: Creating...
aws_s3_bucket_versioning.demo_bucket_versioning: Creating...
aws_s3_bucket_ownership_controls.demo_bucket_ownership: Creation complete after 1s
aws_s3_bucket_server_side_encryption_configuration.demo_bucket_encryption[0]: Creation complete after 1s
aws_s3_bucket_versioning.demo_bucket_versioning: Creation complete after 1s
aws_s3_bucket_public_access_block.demo_bucket_public_access_block: Creation complete after 1s

Apply complete! Resources: 5 added, 0 changed, 0 destroyed.

Outputs:
s3_bucket_arn = "arn:aws:s3:::devops-assignment-s3-demo-bucket-24bcs10350"
s3_bucket_domain_name = "devops-assignment-s3-demo-bucket-24bcs10350.s3.amazonaws.com"
s3_bucket_id = "devops-assignment-s3-demo-bucket-24bcs10350"
s3_bucket_region = "us-east-1"
s3_bucket_versioning_status = "Enabled"
```

---

### Step 6: `terraform show`
Inspects the current state stored in `terraform.tfstate`.

```bash
$ terraform show
# Displays all managed resources, computed IDs, ARNs, and configurations
```

---

### Step 7: `terraform output`
Queries and displays all defined output variables from the state file.

```bash
$ terraform output
s3_bucket_arn = "arn:aws:s3:::devops-assignment-s3-demo-bucket-24bcs10350"
s3_bucket_domain_name = "devops-assignment-s3-demo-bucket-24bcs10350.s3.amazonaws.com"
s3_bucket_id = "devops-assignment-s3-demo-bucket-24bcs10350"
s3_bucket_region = "us-east-1"
s3_bucket_versioning_status = "Enabled"
```

---

### Step 8: `terraform destroy`
Tears down and safely cleans up all infrastructure resources managed by this state file.

```bash
$ terraform destroy -auto-approve

aws_s3_bucket_public_access_block.demo_bucket_public_access_block: Destroying...
aws_s3_bucket_versioning.demo_bucket_versioning: Destroying...
aws_s3_bucket_server_side_encryption_configuration.demo_bucket_encryption[0]: Destroying...
aws_s3_bucket_ownership_controls.demo_bucket_ownership: Destroying...
aws_s3_bucket_public_access_block.demo_bucket_public_access_block: Destruction complete after 1s
aws_s3_bucket_ownership_controls.demo_bucket_ownership: Destruction complete after 1s
aws_s3_bucket_versioning.demo_bucket_versioning: Destruction complete after 1s
aws_s3_bucket_server_side_encryption_configuration.demo_bucket_encryption[0]: Destruction complete after 1s
aws_s3_bucket.demo_bucket: Destroying...
aws_s3_bucket.demo_bucket: Destruction complete after 1s

Destroy complete! Resources: 5 destroyed.
```

---

## 4. Key Takeaways & Best Practices

1. **Declarative State Management:** Terraform tracks the actual state of resources in `terraform.tfstate`, enabling idempotency and precise drift detection.
2. **Modular Variable Isolation:** Separating `variables.tf`, `terraform.tfvars`, and `outputs.tf` allows reusability across multiple environments (e.g., dev, staging, prod).
3. **Security by Default:** Always enforce `aws_s3_bucket_public_access_block` and default AES-256 encryption (`aws_s3_bucket_server_side_encryption_configuration`) in production environments.
