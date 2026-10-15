variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "environment" {
  type    = string
  default = "production"
}

variable "vpc_cidr" {
  type    = string
  default = "10.100.0.0/16"
}

variable "public_subnet_cidr" {
  type    = string
  default = "10.100.1.0/24"
}

variable "cluster_name" {
  type    = string
  default = "final-devops-eks-cluster"
}
