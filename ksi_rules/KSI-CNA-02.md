# KSI-CNA-02: Design systems to minimize the attack surface and minimize lateral movement if compromised

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-09-26 19:15

**What it validates:** Design systems to minimize the attack surface and minimize lateral movement if compromised

**Why it matters:** Validates comprehensive attack surface reduction through network segmentation, workload isolation, service minimization, and lateral movement prevention across traditional and modern cloud-native architectures

## Validation Method

1. `aws ec2 describe-subnets --output json`
   *Analyze subnet segmentation for attack surface isolation (public vs private)*

2. `aws ec2 describe-security-groups --output json`
   *Evaluate micro-segmentation and lateral movement prevention through security group rules*

3. `aws ec2 describe-instances --output json`
   *Assess compute workload exposure and placement for attack surface minimization*

4. `aws ec2 describe-network-acls --output json`
   *Check Network ACLs for subnet-level isolation and lateral movement barriers*

5. `aws elbv2 describe-load-balancers --output json`
   *Analyze load balancer exposure patterns (internal vs internet-facing)*

6. `aws lambda list-functions --output json`
   *Assess Lambda function isolation and VPC configuration for attack surface reduction*

7. `aws rds describe-db-instances --output json`
   *Check database placement and exposure (should be in private subnets)*

## Latest Results

PASS Excellent attack surface minimization and lateral movement prevention (85%): PASS Strong attack surface minimization: 6/8 private subnets (75%)
- PASS Good AZ segmentation: 8 subnets across 2 availability zones
- PASS Strong micro-segmentation: 14/15 custom security groups
- PASS Lateral movement barriers: 10/15 security groups with specific rules
- PASS Minimal compute exposure: 6/6 instances in private subnets
- PASS Database isolation: All 1 RDS instances private
- PASS Controlled service exposure: Single internet-facing load balancer with private backend services
- PASS Lambda isolation: 2/12 functions in VPC
- PASS Advanced segmentation barriers: 1/1 Network ACLs with custom isolation rules

---
*Generated 2025-09-26 19:15 UTC*