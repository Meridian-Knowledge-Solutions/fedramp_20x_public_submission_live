# KSI-CNA-02: Design systems to minimize the attack surface and minimize lateral movement if compromised

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-07-19 08:57

**What it validates:** Design systems to minimize the attack surface and minimize lateral movement if compromised

**Why it matters:** Validates attack surface reduction through network micro-segmentation, minimal services, least privilege principles, and security-first architectural design

## Validation Method

1. `aws ec2 describe-security-groups --output json`
   *Check security groups for micro-segmentation and least privilege network access*

2. `aws ec2 describe-instances --output json`
   *Validate instance configurations for minimal attack surface*

3. `aws ecs describe-services --output json`
   *Check containerized services for attack surface minimization*

4. `aws lambda list-functions --output json`
   *Validate serverless functions for minimal attack surface (function-as-a-service isolation)*

5. `aws ec2 describe-network-interfaces --output json`
   *Analyze network interfaces for micro-segmentation and controlled communications*

6. `aws iam list-roles --output json`
   *Check IAM roles for least privilege and attack surface reduction*

7. `aws ssm describe-instance-information --output json`
   *Validate managed instances for centralized security posture and reduced attack surface*

## Latest Results

WARNING Basic segmentation (20%) - significant improvement recommended: FAIL No subnet information available
- PASS Strong micro-segmentation: 11/12 custom security groups
- PASS Lateral movement barriers: 9/12 security groups with specific rules
- INFO 4 EC2 instances found (placement analysis limited)
- PASS Lambda isolation: 1/4 functions in VPC

---
*Generated 2025-07-19 08:57 UTC*