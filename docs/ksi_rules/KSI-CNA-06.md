# KSI-CNA-06: Design for high availability and recovery

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-06-24 00:57

**What it validates:** Design for high availability and recovery

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

WARNING Moderate HA design (61%) - expand redundancy: PASS Good network HA: 8 subnets across 2 AZs
- PASS Balanced AZ distribution: Even subnet spread across zones
- FAIL No database HA: 1 RDS instances single-AZ
- PASS Excellent application HA: All 1 load balancers multi-AZ
- WARNING No Auto Scaling Groups found - missing compute HA
- PASS Centralized backup strategy: 1 AWS Backup plans
- WARNING No EBS snapshots found
- PASS Storage redundancy: 2 S3 buckets (built-in HA)
- PASS DNS redundancy: 1 Route 53 hosted zones

---
*Generated 2025-06-24 00:57 UTC*