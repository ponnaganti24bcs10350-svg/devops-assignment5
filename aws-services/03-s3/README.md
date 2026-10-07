# AWS Simple Storage Service (S3) - Storage Guide

**Student:** Srividya Ponnaganti  
**Enrollment:** 24BCS10350  
**Domain:** Scalable Object Storage in the Cloud  

---

## 1. What is Amazon S3?

**Amazon Simple Storage Service (Amazon S3)** is an object storage service offering industry-leading scalability, data availability, security, and performance. S3 provides **99.999999999% (11 9s) of data durability** by automatically storing data redundantly across multiple Availability Zones within a region.

```
+-----------------------------------------------------------------------------------+
|                                  Amazon S3 Architecture                           |
|                                                                                   |
|  +-------------------------------- S3 Bucket ----------------------------------+  |
|  | Bucket: "devops-assignment-s3-demo-bucket-24bcs10350" (Region: us-east-1)   |  |
|  |                                                                             |  |
|  |   +-------------------------- S3 Object ------------------------------+     |  |
|  |   | Key: "images/profile.png"                                         |     |  |
|  |   | Value: Binary Data (0B to 5TB)                                    |     |  |
|  |   | Version ID: "v1.2.9834..."                                        |     |  |
|  |   | Metadata: { "Content-Type": "image/png", "author": "srividya" }   |     |  |
|  |   +-------------------------------------------------------------------+     |  |
|  |                                                                             |  |
|  |   +----------------------- Security & Controls -----------------------+     |  |
|  |   |  * Default Server-Side Encryption (SSE-S3 AES-256 / SSE-KMS)      |     |  |
|  |   |  * Bucket Policy (JSON Access Control)                            |     |  |
|  |   |  * Block Public Access (Enforced)                                 |     |  |
|  |   |  * Lifecycle Rules (Auto-transition to Glacier / Expiration)      |     |  |
|  |   +-------------------------------------------------------------------+     |  |
|  +-----------------------------------------------------------------------------+  |
+-----------------------------------------------------------------------------------+
```

---

## 2. Core Concepts: Buckets & Objects

### 2.1 Buckets
* A **Bucket** is a container for objects stored in Amazon S3.
* **Naming Rules:** Bucket names are **globally unique** across all AWS accounts worldwide (3-63 characters, lowercase letters, numbers, and hyphens only).
* Buckets reside in a specific AWS Region to optimize latency and satisfy compliance/data sovereignty requirements.

### 2.2 Objects
* An **Object** is a fundamental entity stored in S3 consisting of:
  * **Key:** The unique name that identifies the object within a bucket (e.g., `logs/2026/app.log`).
  * **Value:** The content/payload itself (size can range from 0 bytes up to **5 Terabytes**; single PUT uploads up to 5 GB, multipart upload for larger).
  * **Version ID:** A unique string generated when versioning is enabled.
  * **Metadata:** System metadata (date, size, ETag) and user-defined key-value pairs.
  * **Access Control Information:** Access policies and tags.

---

## 3. S3 Storage Classes

| Storage Class | Durability | Availability | Latency | Minimum Duration | Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **S3 Standard** | 99.999999999% | 99.99% | Milliseconds | None | Frequently accessed data, active web assets, dynamic content. |
| **S3 Intelligent-Tiering** | 99.999999999% | 99.9% | Milliseconds | None | Data with unpredictable or changing access patterns (auto-tiering). |
| **S3 Standard-IA** | 99.999999999% | 99.9% | Milliseconds | 30 days | Infrequently accessed data requiring millisecond retrieval (disaster recovery, backups). |
| **S3 One Zone-IA** | 99.999999999% | 99.5% | Milliseconds | 30 days | Recreatable non-critical backup data in a single AZ (cost saving). |
| **S3 Glacier Instant Retrieval** | 99.999999999% | 99.9% | Milliseconds | 90 days | Archival data accessed once a quarter requiring immediate retrieval. |
| **S3 Glacier Flexible Retrieval** | 99.999999999% | 99.9% | Minutes to Hours | 90 days | Regulatory archives, tape replacements with flexible retrieval windows. |
| **S3 Glacier Deep Archive** | 99.999999999% | 99.9% | 12 to 48 Hours | 180 days | Long-term digital preservation, multi-year compliance archives (lowest cost). |

---

## 4. Advanced S3 Capabilities

### 4.1 S3 Versioning
* Keeps multiple variants of an object in the same bucket.
* Protects against accidental deletes or overwrites:
  * A standard `DELETE` operation places a **Delete Marker** over the object rather than removing it permanently.
  * Previous versions can be restored at any time.

### 4.2 S3 Lifecycle Policies
* Defines automated rules to manage objects over time:
  1. **Transition Actions:** Automatically move objects from S3 Standard &rarr; S3 Standard-IA &rarr; S3 Glacier after specified days (e.g., transition to Glacier after 90 days).
  2. **Expiration Actions:** Automatically delete outdated objects or non-current versions after specified retention periods.

### 4.3 S3 Encryption
* **Server-Side Encryption (SSE):**
  * **SSE-S3:** Amazon manages keys using AES-256 (default since 2023).
  * **SSE-KMS:** Keys managed via AWS Key Management Service (provides audit trails and key rotation).
  * **SSE-C:** Customer-provided keys.
* **Client-Side Encryption:** Data encrypted by the client application prior to transmission to AWS S3.

### 4.4 S3 Bucket Policies
* Resource-based JSON policies attached directly to the bucket to grant or restrict access to users, roles, or entire AWS accounts.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EnforceTLSRequestsOnly",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::devops-assignment-s3-demo-bucket-24bcs10350",
        "arn:aws:s3:::devops-assignment-s3-demo-bucket-24bcs10350/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
```

---

## 5. Common Use Cases

1. **Static Website Hosting:** Hosting static SPAs (React, Vue, HTML/JS) distributed globally through Amazon CloudFront CDN.
2. **Cloud Data Lake:** Central repository for structured and unstructured data queried with Amazon Athena, AWS Glue, and EMR.
3. **Backup and Disaster Recovery:** Storing system snapshots, database dumps, and VM images with cross-region replication (CRR).
4. **DevOps Artifacts & Build Storage:** Storing compiled binaries, Docker build artifacts, and Terraform remote state backends.
