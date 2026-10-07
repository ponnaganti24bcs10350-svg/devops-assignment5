# Main Terraform Infrastructure Definition - AWS S3 Bucket

# 1. Base S3 Bucket Resource
resource "aws_s3_bucket" "demo_bucket" {
  bucket        = var.bucket_name
  force_destroy = true

  tags = merge(
    var.custom_tags,
    {
      Name        = var.bucket_name
      Environment = var.environment
    }
  )
}

# 2. S3 Bucket Versioning Configuration
resource "aws_s3_bucket_versioning" "demo_bucket_versioning" {
  bucket = aws_s3_bucket.demo_bucket.id

  versioning_configuration {
    status = var.enable_versioning ? "Enabled" : "Suspended"
  }
}

# 3. S3 Bucket Server-Side Encryption (SSE-S3 AES-256)
resource "aws_s3_bucket_server_side_encryption_configuration" "demo_bucket_encryption" {
  count  = var.enable_encryption ? 1 : 0
  bucket = aws_s3_bucket.demo_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# 4. S3 Bucket Ownership Controls
resource "aws_s3_bucket_ownership_controls" "demo_bucket_ownership" {
  bucket = aws_s3_bucket.demo_bucket.id

  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}

# 5. S3 Bucket Public Access Block (Security Best Practice)
resource "aws_s3_bucket_public_access_block" "demo_bucket_public_access_block" {
  bucket = aws_s3_bucket.demo_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
