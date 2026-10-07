# AWS Database Services: DynamoDB & RDS Guide

**Student:** Srividya Ponnaganti  
**Enrollment:** 24BCS10350  
**Domain:** Managed Relational & NoSQL Database Architectures  

---

## 1. Overview of AWS Database Paradigms

Modern cloud architectures leverage both **NoSQL** (Non-relational, distributed, schema-less) and **RDBMS** (Relational, ACID-compliant, structured) database engines depending on the access patterns and data models required by microservices.

```
+-----------------------------------------------------------------------------------------+
|                                AWS Managed Database Fleet                               |
|                                                                                         |
|  +--------------------- Amazon DynamoDB ---------------------+   +--- Amazon RDS -----+  |
|  | * Fully Managed Serverless NoSQL                          |   | * Managed RDBMS    |  |
|  | * Key-Value & Document Store                              |   | * PostgreSQL/MySQL |  |
|  | * Single-digit millisecond latency at any scale           |   | * Multi-AZ Standby |  |
|  | * Partition Key + Sort Key index model                    |   | * Read Replicas    |  |
|  +-----------------------------------------------------------+   +--------------------+  |
+-----------------------------------------------------------------------------------------+
```

---

## 2. Amazon DynamoDB (NoSQL Service)

### 2.1 What is DynamoDB?
**Amazon DynamoDB** is a fully managed, serverless, key-value and document database designed to deliver single-digit millisecond performance at any scale. It has built-in security, continuous backups, automated multi-region replication, and data encryption at rest.

### 2.2 Core Data Model

```
+------------------------------------------------------------------------------------------+
| Table: "UserProfiles"                                                                    |
|                                                                                          |
| +------------------------- PRIMARY KEY -------------------------+                        |
| | Partition Key (PK)       | Sort Key (SK)                      | Attributes (Dynamic)   |
| +--------------------------+------------------------------------+------------------------+
| | "USER#101"               | "METADATA#PROFILE"                 | name="Srividya",       |
| |                          |                                    | role="DevOps Engineer" |
| +--------------------------+------------------------------------+------------------------+
| | "USER#101"               | "ORDER#2026-10-08T00:30"           | amount=150.00,         |
| |                          |                                    | status="PAID"          |
| +--------------------------+------------------------------------+------------------------+
| | "USER#202"               | "METADATA#PROFILE"                 | name="Alex",           |
| |                          |                                    | email="alex@corp.com"  |
| +--------------------------+------------------------------------+------------------------+
+------------------------------------------------------------------------------------------+
```

* **Table:** A collection of data items (similar to a table in SQL or a collection in MongoDB).
* **Item:** A collection of attributes that is uniquely identifiable among all other items (similar to a row/record).
* **Attribute:** A fundamental data element (similar to a column or field). DynamoDB is schema-less; items in the same table can have entirely different attributes except for the primary key.

### 2.3 Primary Keys & Indexing
1. **Simple Primary Key (Partition Key only):**
   * DynamoDB uses the partition key's hash value to distribute data items across physical storage partitions.
2. **Composite Primary Key (Partition Key + Sort Key):**
   * Items with the same partition key are stored together in sorted order by the sort key (enables range queries like `begins_with`, `between`, `>`, `<`).
3. **Secondary Indexes:**
   * **Global Secondary Index (GSI):** An index with a partition key and sort key that can be different from those on the base table.
   * **Local Secondary Index (LSI):** An index that has the same partition key as the base table, but a different sort key.

### 2.4 DynamoDB Use Cases
* High-volume e-commerce shopping carts.
* Gaming leaderboards and real-time state sync.
* User session stores and authentication tokens.
* IoT sensor data ingestion and real-time telemetry.

---

## 3. Amazon Relational Database Service (RDS)

### 3.1 What is Amazon RDS?
**Amazon Relational Database Service (Amazon RDS)** makes it easy to set up, operate, and scale a relational database in the AWS Cloud. It automates time-consuming administrative tasks such as hardware provisioning, database setup, patching, and backups.

### 3.2 Supported Database Engines
* **Amazon Aurora:** Cloud-native MySQL and PostgreSQL compatible enterprise database with 5x throughput of standard MySQL.
* **PostgreSQL:** Open-source object-relational database.
* **MySQL:** Popular open-source relational database.
* **MariaDB:** Community-developed fork of MySQL.
* **Oracle Database:** Enterprise Oracle editions.
* **Microsoft SQL Server:** Enterprise MS-SQL editions.

### 3.3 High Availability & Scaling Architecture

```
                                  [ Write & Read Traffic ]
                                             |
                                             v
                               +---------------------------+
                               |  Primary DB Instance      | (AZ-1a: Active)
                               |  (PostgreSQL / MySQL)     |
                               +-------------+-------------+
                                             |
                     +-----------------------+-----------------------+
                     | Synchronous                                   | Asynchronous
                     | Physical Replication                          | Replication
                     v                                               v
       +---------------------------+                   +---------------------------+
       | Multi-AZ Standby Replica  | (AZ-1b: Standby)  | Read Replica              | (AZ-1c: Read Only)
       | (Automatic Failover)      |                   | (Offloads Read Traffic)   |
       +---------------------------+                   +---------------------------+
```

1. **Multi-AZ Deployments (High Availability / Disaster Recovery):**
   * Automatically provisions and maintains a synchronous standby replica in a different Availability Zone.
   * In the event of infrastructure failure or maintenance, RDS performs an automatic failover to the standby without changing the database endpoint URL.
2. **Read Replicas (Horizontal Read Scaling):**
   * Asynchronously replicates updates from the primary DB instance to up to 15 read replicas.
   * Offloads heavy BI reporting, analytical queries, and read-heavy application traffic.
3. **Automated Backups & Snapshots:**
   * Backups are taken automatically during user-defined windows with point-in-time recovery (PITR) down to the second within a 1-35 day retention period.

### 3.4 RDS Security
* Deployed within private VPC subnets with no direct public internet exposure.
* In-transit encryption with mandatory SSL/TLS certificates.
* Encryption at rest using **AWS KMS (AES-256)** for DB instances, automated backups, and snapshots.

### 3.5 RDS Use Cases
* Financial transaction systems requiring strict **ACID compliance**.
* Complex relational business applications (ERP, CRM, inventory catalogs).
* Legacy application migrations requiring standard SQL dialects.

---

## 4. Architectural Comparison: DynamoDB vs. RDS

| Dimension | Amazon DynamoDB | Amazon RDS |
| :--- | :--- | :--- |
| **Data Model** | NoSQL (Key-Value & Document) | Relational (SQL Tables, Joins, Foreign Keys) |
| **Scaling Model** | Automatic horizontal partitioning (Infinite) | Vertical scaling (compute/storage) + Read Replicas |
| **Query Pattern** | Primary key lookups, GSIs, key-value filters | Complex multi-table JOINs, aggregations, SQL queries |
| **Management** | 100% Serverless (On-Demand / Provisioned) | Managed DB Instances (Serverless option in Aurora) |
| **Transaction Guarantee** | ACID support via `TransactWriteItems` | Full ACID relational compliance out of the box |
| **High Availability** | Built-in multi-AZ redundancy | Multi-AZ standby replica deployment |
