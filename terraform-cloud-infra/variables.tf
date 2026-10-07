# Input Variables for End-to-End Cloud Infrastructure

variable "aws_region" {
  description = "The AWS region to deploy the infrastructure into"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "The base project name used in resource naming and tags"
  type        = string
  default     = "devops-cloud-action"
}

variable "environment" {
  description = "Deployment environment (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR block for the Virtual Private Cloud"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR block for the Public Subnet"
  type        = string
  default     = "10.0.1.0/24"
}

variable "availability_zone" {
  description = "Availability zone for the public subnet"
  type        = string
  default     = "us-east-1a"
}

variable "instance_type" {
  description = "EC2 instance size"
  type        = string
  default     = "t3.micro"
}

variable "s3_bucket_prefix" {
  description = "Prefix for the globally unique S3 bucket name"
  type        = string
  default     = "devops-session19-cloud-app-24bcs10350"
}

variable "enable_s3_versioning" {
  description = "Enable object versioning on the S3 bucket"
  type        = bool
  default     = true
}

variable "server_port" {
  description = "HTTP server port for application ingress"
  type        = number
  default     = 80
}

variable "ssh_port" {
  description = "SSH administrative access port"
  type        = number
  default     = 22
}
