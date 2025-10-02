# KSI-CNA-02: Segment network and compute resources into security zones

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-10-02 03:01

**What it validates:** Segment network and compute resources into security zones

**Why it matters:** Validates comprehensive network segmentation from basic VPC subnets to enterprise-grade multi-tier architecture with strict isolation

## Validation Method

1. `aws ec2 describe-subnets --output json`
   *Check subnet configurations for network segmentation and security zones*

2. `aws ec2 describe-security-groups --output json`
   *Validate security group rules for zone-based access control*

3. `aws ec2 describe-instances --output json`
   *Check EC2 instance placements across security zones*

4. `aws ec2 describe-network-acls --output json`
   *Validate network ACLs for zone-level traffic control*

5. `aws elbv2 describe-load-balancers --output json`
   *Check load balancer configurations for zone-aware traffic distribution*

6. `aws lambda list-functions --output json`
   *Validate Lambda function network configurations and VPC integration*

7. `aws rds describe-db-instances --output json`
   *Check RDS instance placements in private subnets and security zones*

## Latest Results

PASS Strong attack surface minimization (85%): PASS Strong attack surface minimization: 6/8 private subnets (75%)
- PASS Good AZ segmentation: 8 subnets across 2 availability zones
- PASS Strong micro-segmentation: 14/15 custom security groups
- PASS Lateral movement barriers: 10/15 security groups with specific rules
- PASS Minimal compute exposure: 6/6 instances in private subnets
- PASS Database isolation: All 1 RDS instances private
- PASS Controlled service exposure: Single internet-facing load balancer with private backend services
- PASS Lambda isolation: 2/12 functions in VPC
- PASS Advanced segmentation barriers: 1/1 Network ACLs with custom isolation rules

---
*Generated 2025-10-02 03:01 UTC*