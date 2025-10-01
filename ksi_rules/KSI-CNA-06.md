# KSI-CNA-06: Design systems for high availability and rapid recovery

## Overview

**Category:** Cloud Native Architecture
**Status:** FAIL
**Last Check:** 2025-10-01 03:22

**What it validates:** Design systems for high availability and rapid recovery

**Why it matters:** Validates comprehensive high availability through multi-AZ deployments, redundant infrastructure, automated failover, backup strategies, and disaster recovery capabilities across all service layers

## Validation Method

1. `aws ec2 describe-subnets --output json`
   *Analyze subnet distribution across availability zones for network-level HA*

2. `aws ec2 describe-availability-zones --output json`
   *Check available AZs in region for HA planning and validation*

3. `aws rds describe-db-instances --output json`
   *Validate RDS Multi-AZ deployments and database high availability*

4. `aws elbv2 describe-load-balancers --output json`
   *Check load balancers for application-layer HA and traffic distribution*

5. `aws autoscaling describe-auto-scaling-groups --output json`
   *Validate Auto Scaling Groups for compute resilience and multi-AZ distribution*

6. `aws backup list-backup-plans --output json`
   *Check backup plans for data protection and recovery capabilities*

7. `aws ec2 describe-snapshots --owner-ids self --output json`
   *Validate EBS snapshot strategy for storage recovery*

8. `aws s3api list-buckets --output json`
   *Check S3 buckets for storage redundancy and cross-region replication*

9. `aws route53 list-hosted-zones --output json`
   *Validate DNS redundancy and health check capabilities*

## Latest Results

- Exception during evaluation: name 'compliance_percentage' is not defined

---
*Generated 2025-10-01 03:22 UTC*