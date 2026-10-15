# EC2 Compute Infrastructure

# 1. Look up latest Amazon Linux 2023 AMI
data "aws_ami" "amazon_linux_2023" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-2023.*-x86_64"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

# 2. EC2 Virtual Machine Instance
resource "aws_instance" "web_server" {
  ami                  = data.aws_ami.amazon_linux_2023.id
  instance_type        = var.instance_type
  subnet_id            = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  iam_instance_profile = aws_iam_instance_profile.ec2_profile.name

  # Root block device configuration
  root_block_device {
    volume_size           = 20
    volume_type           = "gp3"
    delete_on_termination = true
    encrypted             = true

    tags = {
      Name = "${var.project_name}-root-ebs"
    }
  }

  # User Data Bootstrap Script (Provisioning Web Server & Cloud Status Page)
  user_data = <<-EOF
              #!/bin/bash
              dnf update -y
              dnf install -y httpd awscli

              systemctl start httpd
              systemctl enable httpd

              # Create dynamic HTML status dashboard
              cat << 'HTML' > /var/www/html/index.html
              <!DOCTYPE html>
              <html lang="en">
              <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>DevOps Cloud Infrastructure Dashboard</title>
                <style>
                  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 40px 20px; }
                  .container { max-width: 900px; margin: 0 auto; background: #1e293b; border-radius: 12px; padding: 32px; border: 1px solid #334155; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
                  h1 { color: #38bdf8; margin-top: 0; font-size: 28px; }
                  .badge { display: inline-block; padding: 4px 12px; border-radius: 9999px; background: #0284c7; color: white; font-weight: 600; font-size: 13px; margin-bottom: 20px; }
                  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin-top: 24px; }
                  .card { background: #0f172a; border-radius: 8px; padding: 18px; border: 1px solid #334155; }
                  .card h3 { margin: 0 0 8px 0; font-size: 14px; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; }
                  .card p { margin: 0; font-size: 16px; color: #f1f5f9; font-weight: 500; font-family: monospace; }
                  .status-live { color: #4ade80; font-weight: bold; }
                </style>
              </head>
              <body>
                <div class="container">
                  <span class="badge">Terraform Managed Infrastructure</span>
                  <h1>Cloud & Terraform in Action - Session 19</h1>
                  <p>Production AWS End-to-End Infrastructure successfully provisioned with declarative Terraform configuration.</p>
                  
                  <div class="grid">
                    <div class="card">
                      <h3>Student Name</h3>
                      <p>Srividya Ponnaganti</p>
                    </div>
                    <div class="card">
                      <h3>Enrollment No</h3>
                      <p>24BCS10350</p>
                    </div>
                    <div class="card">
                      <h3>Infrastructure Status</h3>
                      <p class="status-live">ONLINE / HEALTHY</p>
                    </div>
                    <div class="card">
                      <h3>AWS VPC Network</h3>
                      <p>${aws_vpc.main.id}</p>
                    </div>
                    <div class="card">
                      <h3>Public Subnet</h3>
                      <p>${aws_subnet.public.id}</p>
                    </div>
                    <div class="card">
                      <h3>Attached S3 Bucket</h3>
                      <p>${aws_s3_bucket.app_storage.id}</p>
                    </div>
                  </div>
                </div>
              </body>
              </html>
              HTML

              EOF

  # Explicit dependency declaration to ensure Networking and IAM profiles are fully ready
  depends_on = [
    aws_internet_gateway.igw,
    aws_route_table_association.public_assoc,
    aws_iam_role_policy_attachment.attach_s3_policy
  ]

  tags = {
    Name = "${var.project_name}-web-server"
    Role = "WebServer"
  }
}
