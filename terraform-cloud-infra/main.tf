# Root Entry Coordinator for Cloud & Terraform in Action
# Session 19: End-to-End AWS Infrastructure Deployment
# Student: Srividya Ponnaganti (24BCS10350)

# Local values for computed metadata
locals {
  app_fqdn       = "http://${aws_instance.web_server.public_ip}:${var.server_port}"
  deployment_id  = "${var.project_name}-${var.environment}"
  common_tags    = {
    DeploymentId = local.deployment_id
    ManagedBy    = "Terraform"
    Owner        = "Srividya Ponnaganti"
    Enrollment   = "24BCS10350"
  }
}
