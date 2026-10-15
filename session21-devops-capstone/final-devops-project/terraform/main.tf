# VPC Network
resource "aws_vpc" "final_vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "${var.environment}-final-vpc"
  }
}

resource "aws_subnet" "final_subnet" {
  vpc_id                  = aws_vpc.final_vpc.id
  cidr_block              = var.public_subnet_cidr
  availability_zone       = "${var.aws_region}a"
  map_public_ip_on_launch = true

  tags = {
    Name = "${var.environment}-final-subnet"
  }
}

resource "aws_internet_gateway" "final_igw" {
  vpc_id = aws_vpc.final_vpc.id

  tags = {
    Name = "${var.environment}-final-igw"
  }
}

resource "aws_route_table" "final_rt" {
  vpc_id = aws_vpc.final_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.final_igw.id
  }
}

resource "aws_route_table_association" "final_rta" {
  subnet_id      = aws_subnet.final_subnet.id
  route_table_id = aws_route_table.final_rt.id
}

# S3 State & Artifacts Bucket
resource "aws_s3_bucket" "artifacts" {
  bucket        = "devops-final-project-artifacts-24bcs10350"
  force_destroy = true
}

resource "aws_s3_bucket_versioning" "artifacts_versioning" {
  bucket = aws_s3_bucket.artifacts.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "artifacts_sse" {
  bucket = aws_s3_bucket.artifacts.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "artifacts_pab" {
  bucket                  = aws_s3_bucket.artifacts.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
