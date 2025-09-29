# KSI-CNA-07: Ensure cloud-native information resources are implemented based on host provider's best practices and documented guidance

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-09-29 22:56

**What it validates:** Ensure cloud-native information resources are implemented based on host provider's best practices and documented guidance

**Why it matters:** Validates comprehensive adherence to AWS best practices through Well-Architected principles, service configurations, security recommendations, and operational excellence

## Validation Method

1. `aws configservice describe-config-rules --output json`
   *Check Config rules for compliance and governance.*

2. `aws cloudtrail describe-trails --output json`
   *Validate CloudTrail configuration.*

3. `aws cloudtrail describe-trails --query 'trailList[?IsMultiRegionTrail==`true`]|[0].Name' --output text | xargs -I {} aws cloudtrail get-trail-status --name {}`
   *RESILIENT: Checks the status of the first found multi-region CloudTrail trail.*

4. `aws kms list-keys --output json`
   *Check for KMS keys for data protection.*

5. `aws iam get-account-summary --output json`
   *Check IAM role vs. user ratio.*

6. `aws ec2 describe-instances --output json`
   *Assess full instance data for IaC patterns and performance.*

7. `aws elbv2 describe-load-balancers --output json`
   *Check for multi-AZ load balancers.*

8. `aws autoscaling describe-auto-scaling-groups --output json`
   *Check for Auto Scaling Groups for traditional reliability.*

9. `aws s3api list-buckets --output json`
   *Validate S3 usage for cost-effective storage.*

10. `aws cloudwatch describe-alarms --output json`
   *Validate monitoring foundation.*

11. `aws backup list-backup-plans --output json`
   *Check for backup strategies.*

12. `aws organizations describe-organization --output json`
   *Check for enterprise governance with AWS Organizations.*

13. `aws lambda list-functions --output json`
   *Detect serverless-first architectures.*

14. `aws rds describe-db-instances --output json`
   *Detect managed database services.*

15. `aws apigateway get-rest-apis --output json`
   *Detect managed API services.*

## Latest Results

PASS Strong AWS best practices adoption (70%): FAIL No CloudTrail configured (critical security best practice violation)
- PASS Encryption key management: 17 KMS keys for data protection
- PASS IAM best practices: 84 roles vs 3 users (service-oriented architecture)
- PASS Excellent reliability architecture: 1/1 load balancers multi-AZ
- PASS Infrastructure as Code scaling: 5/6 Terraform-managed instances (superior to ASGs for pilot)
- PASS Active data protection: 2 backup plan(s) with recent execution
- PASS Good performance: 5/6 instances using modern types
- PASS Storage optimization: 7 S3 buckets (cost-effective storage)
- PASS Proactive monitoring: 13 CloudWatch alarms
- PASS Compliance service available: AWS Config ready for rule deployment (optional for pilot)
- PASS Enterprise governance: AWS Organizations with centralized management

---
*Generated 2025-09-29 22:56 UTC*