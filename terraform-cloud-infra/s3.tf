# S3 Storage Infrastructure

# 1. Base S3 Bucket Resource
resource "aws_s3_bucket" "app_storage" {
  bucket        = var.s3_bucket_prefix
  force_destroy = true

  tags = {
    Name = var.s3_bucket_prefix
    Tier = "ObjectStorage"
  }
}

# 2. S3 Bucket Versioning
resource "aws_s3_bucket_versioning" "storage_versioning" {
  bucket = aws_s3_bucket.app_storage.id

  versioning_configuration {
    status = var.enable_s3_versioning ? "Enabled" : "Suspended"
  }
}

# 3. S3 Server-Side Encryption (SSE-S3 AES256)
resource "aws_s3_bucket_server_side_encryption_configuration" "storage_encryption" {
  bucket = aws_s3_bucket.app_storage.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# 4. S3 Ownership Controls
resource "aws_s3_bucket_ownership_controls" "storage_ownership" {
  bucket = aws_s3_bucket.app_storage.id

  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}

# 5. S3 Block Public Access
resource "aws_s3_bucket_public_access_block" "storage_public_block" {
  bucket = aws_s3_bucket.app_storage.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# 6. Sample Initial Asset Object Upload
resource "aws_s3_object" "sample_config" {
  bucket  = aws_s3_bucket.app_storage.id
  key     = "config/app-manifest.json"
  content = jsonencode({
    app_name        = "Cloud Action Webapp"
    deployed_by     = "Terraform"
    author          = "Srividya Ponnaganti"
    enrollment      = "24BCS10350"
    session         = "Session 19"
    environment     = var.environment
    timestamp       = "2026-10-08T00:30:00Z"
  })
  content_type = "application/json"

  depends_on = [
    aws_s3_bucket_ownership_controls.storage_ownership,
    aws_s3_bucket_public_access_block.storage_public_block
  ]
}
