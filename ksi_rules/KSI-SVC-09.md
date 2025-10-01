# KSI-SVC-09: Use TLS 1.2 or higher versions of secure protocols

## Overview

**Category:** Service Configuration
**Status:** PASS
**Last Check:** 2025-10-01 22:14

**What it validates:** Use TLS 1.2 or higher versions of secure protocols

**Why it matters:** Validates comprehensive TLS 1.2+ enforcement from basic HTTPS to enterprise-grade cryptographic compliance and certificate management

## Validation Method

1. `aws acm list-certificates --output json`
   *Check ACM certificates for TLS 1.2+ support and validity*

2. `aws elbv2 describe-ssl-policies --output json`
   *Validate load balancer SSL policies for TLS 1.2+ enforcement*

3. `for arn in $(aws elbv2 describe-load-balancers --query 'LoadBalancers[].LoadBalancerArn' --output text); do aws elbv2 describe-listeners --load-balancer-arn $arn --output json; done`
   *Check load balancer listeners for TLS 1.2+ configurations*

4. `aws ec2 describe-vpc-endpoints --output json`
   *Validate VPC endpoints using TLS 1.2+ encrypted connections*

5. `aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,Engine,EngineVersion]' --output json`
   *Check RDS instances for TLS 1.2+ support in database engines*

6. `aws kms list-keys --output json`
   *Validate KMS keys for cryptographic compliance*

7. `aws cloudwatch describe-alarms --output json`
   *Check CloudWatch alarms for TLS and certificate monitoring*

## Latest Results

PASS Good communication integrity (60%): PASS Tls Certificate Management
- FAIL Continuous Certificate Monitoring
- PASS Inter Service Encryption
- PASS Integrity Validation Mechanisms
- FAIL Automated Certificate Lifecycle

---
*Generated 2025-10-01 22:14 UTC*