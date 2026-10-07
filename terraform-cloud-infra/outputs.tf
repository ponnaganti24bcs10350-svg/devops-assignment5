# Output Values for End-to-End Cloud Infrastructure

output "vpc_id" {
  description = "The ID of the provisioned Virtual Private Cloud"
  value       = aws_vpc.main.id
}

output "public_subnet_id" {
  description = "The ID of the Public Subnet"
  value       = aws_subnet.public.id
}

output "internet_gateway_id" {
  description = "The ID of the Internet Gateway"
  value       = aws_internet_gateway.igw.id
}

output "security_group_id" {
  description = "The ID of the Web Application Security Group"
  value       = aws_security_group.web_sg.id
}

output "ec2_instance_id" {
  description = "The ID of the provisioned EC2 instance"
  value       = aws_instance.web_server.id
}

output "ec2_public_ip" {
  description = "The Public IPv4 address of the EC2 Web Server"
  value       = aws_instance.web_server.public_ip
}

output "ec2_public_dns" {
  description = "The Public DNS hostname of the EC2 Web Server"
  value       = aws_instance.web_server.public_dns
}

output "s3_bucket_id" {
  description = "The ID/Name of the S3 Object Storage Bucket"
  value       = aws_s3_bucket.app_storage.id
}

output "s3_bucket_arn" {
  description = "The Amazon Resource Name (ARN) of the S3 Storage Bucket"
  value       = aws_s3_bucket.app_storage.arn
}

output "iam_role_arn" {
  description = "The ARN of the IAM Role assumed by the EC2 instance"
  value       = aws_iam_role.ec2_s3_role.arn
}

output "application_url" {
  description = "Direct HTTP access URL to the deployed web application dashboard"
  value       = "http://${aws_instance.web_server.public_ip}"
}
