# Output Values Definition

output "s3_bucket_id" {
  description = "The name/ID of the created S3 bucket"
  value       = aws_s3_bucket.demo_bucket.id
}

output "s3_bucket_arn" {
  description = "The Amazon Resource Name (ARN) of the created S3 bucket"
  value       = aws_s3_bucket.demo_bucket.arn
}

output "s3_bucket_region" {
  description = "The AWS Region where the S3 bucket is hosted"
  value       = aws_s3_bucket.demo_bucket.region
}

output "s3_bucket_domain_name" {
  description = "The bucket domain name"
  value       = aws_s3_bucket.demo_bucket.bucket_domain_name
}

output "s3_bucket_versioning_status" {
  description = "The versioning status of the S3 bucket"
  value       = aws_s3_bucket_versioning.demo_bucket_versioning.versioning_configuration[0].status
}
