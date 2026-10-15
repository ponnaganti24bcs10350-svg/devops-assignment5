output "vpc_id" {
  value = aws_vpc.final_vpc.id
}

output "subnet_id" {
  value = aws_subnet.final_subnet.id
}

output "s3_bucket_arn" {
  value = aws_s3_bucket.artifacts.arn
}
