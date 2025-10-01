# KSI-SVC-02: Use encryption in transit with TLS 1.2 or higher

## Overview

**Category:** Service Configuration
**Status:** PASS
**Last Check:** 2025-10-01 22:14

**What it validates:** Use encryption in transit with TLS 1.2 or higher

**Why it matters:** Validates comprehensive encryption in transit from basic TLS to enterprise-grade certificate management and cryptographic compliance

## Validation Method

1. `for arn in $(aws elbv2 describe-load-balancers --query 'LoadBalancers[].LoadBalancerArn' --output text); do aws elbv2 describe-listeners --load-balancer-arn $arn --output json; done`
   *Check load balancer listeners for TLS 1.2+ enforcement*

2. `aws ec2 describe-vpc-endpoints --output json`
   *Validate VPC endpoints using encrypted connections*

3. `aws cloudfront list-distributions --output json`
   *Check CloudFront distributions for TLS 1.2+ minimum protocol*

4. `aws apigateway get-rest-apis --output json`
   *Validate API Gateway TLS configurations*

5. `aws rds describe-db-instances --output json`
   *Check RDS instances for SSL/TLS enforcement*

6. `aws elasticache describe-cache-clusters --output json`
   *Validate ElastiCache encryption in transit*

7. `aws acm list-certificates --output json`
   *Check ACM certificates for TLS 1.2+ support and validity*

8. `aws organizations describe-organization --output json`
   *Validate organization-wide encryption in transit policies*

## Latest Results

PASS Network traffic encryption established across multiple services (56%): PASS Private service communication: 7 VPC endpoints configured.
- PASS API encryption capability: 2 API Gateway endpoints (HTTPS by default).
- PASS Database encryption capability: 1 RDS instances (1 encrypted).
- PASS Automated certificate management: 1/2 active ACM certificates (50%).
- PASS Enterprise-wide encryption governance: AWS Organizations enables centralized policies.
- PASS Advanced organization features: SCPs for encryption policy enforcement enabled.

---
*Generated 2025-10-01 22:14 UTC*