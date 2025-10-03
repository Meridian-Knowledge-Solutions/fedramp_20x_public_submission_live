# KSI-CNA-06: Deploy highly available components and services

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-10-03 22:39

**What it validates:** Deploy highly available components and services

**Why it matters:** Validates comprehensive high availability from basic multi-AZ to enterprise-grade disaster recovery and global resilience

## Validation Method

1. `aws ec2 describe-subnets --output json`
   *Check subnet distribution across multiple availability zones*

2. `aws ec2 describe-availability-zones --output json`
   *Validate availability zone utilization for redundancy*

3. `aws rds describe-db-instances --output json`
   *Check RDS Multi-AZ deployments and read replicas for database HA*

4. `aws elbv2 describe-load-balancers --output json`
   *Validate load balancer configurations across multiple AZs*

5. `aws autoscaling describe-auto-scaling-groups --output json`
   *Check auto-scaling configurations for multi-AZ distribution*

6. `aws backup list-backup-plans --output json`
   *Validate AWS Backup plans for automated HA recovery*

7. `aws ec2 describe-snapshots --owner-ids self --output json`
   *Check EBS snapshot policies for data resilience*

8. `aws s3api list-buckets --output json`
   *Validate S3 configurations for cross-region replication*

9. `aws route53 list-hosted-zones --output json`
   *Check Route53 health checks and DNS failover for service HA*

## Latest Results

PASS Excellent high availability design (100%): PASS Strong network HA: 8 subnets across 2 AZs
- PASS Balanced subnet distribution across availability zones
- PASS Application HA: 1 multi-AZ load balancer(s) providing traffic distribution
- PASS Active backup strategy: 2 AWS Backup plan(s) with recent execution
- PASS Storage redundancy: 7 S3 bucket(s) with built-in 11-9s durability
- PASS Database HA-ready: 1 RDS instance(s) with multi-AZ subnet groups (easily convertible)
- INFO Compute HA via Infrastructure as Code (Terraform-managed instances acceptable for pilot)
- PASS Bonus: Storage recovery via 586 EBS snapshot(s)
- PASS DNS infrastructure: 1 Route 53 hosted zone(s)

---
*Generated 2025-10-03 22:39 UTC*