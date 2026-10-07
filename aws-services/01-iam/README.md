# AWS Identity and Access Management (IAM) - Governance Guide

**Student:** Srividya Ponnaganti  
**Enrollment:** 24BCS10350  
**Domain:** AWS Cloud Security & Identity Governance  

---

## 1. What is AWS IAM?

**AWS Identity and Access Management (IAM)** is a web service that helps you securely control access to AWS resources. IAM is the core authentication (**AuthN**) and authorization (**AuthZ**) plane of Amazon Web Services. It is a **global service** (not region-specific) and is provided at no additional charge.

```
+-----------------------------------------------------------------------------------+
|                                  AWS IAM Plane                                    |
|                                                                                   |
|  +--------------------+    +--------------------+    +-------------------------+  |
|  |     IAM Users      |    |     IAM Groups     |    |        IAM Roles        |  |
|  |  (Human / Machine) |    | (Collection of U)  |    | (Temporary Credentials) |  |
|  +---------+----------+    +---------+----------+    +------------+------------+  |
|            |                         |                            |               |
|            +-------------------------+----------------------------+               |
|                                      |                                            |
|                                      v                                            |
|                          +-----------------------+                                |
|                          |     IAM Policies      |                                |
|                          |    (JSON Documents)   |                                |
|                          +-----------+-----------+                                |
|                                      |                                            |
|                                      v                                            |
|               +---------------------------------------------+                     |
|               |  AWS Resources (EC2, S3, RDS, DynamoDB...)  |                     |
|               +---------------------------------------------+                     |
+-----------------------------------------------------------------------------------+
```

---

## 2. Core IAM Entities & Concepts

### 2.1 IAM Users
* An **IAM User** is an entity representing a person or application that interacts with AWS resources.
* Consists of a name, credentials (password for AWS Management Console, or Access Key ID & Secret Access Key for AWS CLI/SDKs).
* Initially has **zero permissions** by default (implicit deny).

### 2.2 IAM Groups
* An **IAM Group** is a collection of IAM users.
* Used to attach permissions to multiple users at once (e.g., `Developers`, `Admins`, `Auditors`).
* Groups cannot be nested; a group cannot contain another group.

### 2.3 IAM Roles
* An **IAM Role** is an IAM identity with specific permission policies that can be assumed by anyone who needs it.
* Does not have permanent credentials (passwords or long-term access keys).
* AWS Security Token Service (**AWS STS**) provides temporary, short-lived security credentials (typically valid for 15 minutes to 12 hours).
* Commonly assumed by:
  1. **AWS Services** (e.g., an EC2 instance assuming an IAM Role to access an S3 bucket).
  2. **Cross-Account Access** (delegating access across different AWS accounts).
  3. **Federated Users** (Single Sign-On via SAML 2.0 / OpenID Connect with Okta, Google, Azure AD).

### 2.4 IAM Policies
* An **IAM Policy** is a JSON document that defines permissions.
* AWS evaluates policies using an explicit algorithm:
  `Explicit Deny > Explicit Allow > Default Deny (Implicit)`

#### Structure of a JSON IAM Policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3ReadSpecificBucket",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::production-app-data",
        "arn:aws:s3:::production-app-data/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "true"
        }
      }
    }
  ]
}
```

* **Version:** The policy language version (`2012-10-17` is standard).
* **Statement:** Array of individual permission statements containing:
  * **Sid:** Optional statement identifier.
  * **Effect:** Either `"Allow"` or `"Deny"`.
  * **Action:** List of specific API actions (e.g., `ec2:DescribeInstances`, `s3:PutObject`).
  * **Resource:** Amazon Resource Names (ARNs) to which the action applies.
  * **Condition:** Optional criteria under which the policy is in effect (e.g., IP range, MFA status, SSL/TLS enforcement).

---

## 3. Permissions & The Principle of Least Privilege

### Principle of Least Privilege (PoLP)
* The security standard of granting users and applications **only the minimal permissions necessary** to perform their required job duties, and no more.
* Prevents accidental deletion, privilege escalation, and lateral movement in the event of compromised credentials.

### Policy Types:
1. **Identity-Based Policies:** Attached directly to Users, Groups, or Roles.
2. **Resource-Based Policies:** Attached directly to resources (e.g., S3 Bucket Policies, KMS Key Policies).
3. **Service Control Policies (SCPs):** Organizational boundaries applied across AWS Organizations.
4. **Permission Boundaries:** Advanced feature that sets the maximum allowable permissions an identity-based policy can grant.

---

## 4. IAM Best Practices

1. **Lock Away Root User Credentials:** Use the AWS root user only for initial setup and emergency account-level changes. Enable hardware/virtual MFA immediately.
2. **Never Hardcode Credentials:** Use IAM Roles and Instance Profiles for applications running on EC2, ECS, or Lambda instead of storing AWS access keys.
3. **Enforce Multi-Factor Authentication (MFA):** Mandatory for all human console users.
4. **Rotate Access Keys Regularly:** Enforce 90-day rotation schedules for long-term programmatic credentials.
5. **Use IAM Access Analyzer:** Continuously analyze policies to identify unintended public or cross-account access.
6. **Use AWS Organizations & SCPs:** Enforce organizational guardrails across multiple AWS accounts.

---

## 5. Common Use Cases

| Scenario | Recommended IAM Solution |
| :--- | :--- |
| EC2 instance needs to read/write to S3 | Attach an **IAM Instance Profile (Role)** with S3 permissions directly to the EC2 instance. |
| Corporate employees need AWS Console access | Use **AWS IAM Identity Center (SSO)** with SAML 2.0 federation. |
| CI/CD Pipeline (GitHub Actions) deploys to AWS | Use **OIDC (OpenID Connect)** federation to assume an IAM Role temporarily without storing long-lived AWS secret keys in GitHub. |
| Read-only audit access for compliance team | Create a `SecurityAuditors` IAM Group with the AWS-managed policy `SecurityAudit`. |
