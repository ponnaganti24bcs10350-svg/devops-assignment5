# Input Variables Definition

variable "aws_region" {
  description = "The AWS region to deploy resources into"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "Name of the S3 bucket (must be globally unique)"
  type        = string
  default     = "devops-assignment-s3-demo-bucket-24bcs10350"
}

variable "environment" {
  description = "Deployment environment name"
  type        = string
  default     = "dev"
}

variable "enable_versioning" {
  description = "Flag to enable object versioning on the S3 bucket"
  type        = bool
  default     = true
}

variable "enable_encryption" {
  description = "Flag to enable server-side encryption by default"
  type        = bool
  default     = true
}

variable "custom_tags" {
  description = "Additional tags for the S3 bucket"
  type        = map(string)
  default = {
    Task = "Session-18-Terraform-S3"
    Tier = "Storage"
  }
}
