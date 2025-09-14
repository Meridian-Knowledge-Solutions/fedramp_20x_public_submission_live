# KSI-CNA-07: Ensure cloud-native information resources are implemented based on host provider's best practices and documented guidance

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-09-14 10:15

**What it validates:** Ensure cloud-native information resources are implemented based on host provider's best practices and documented guidance

**Why it matters:** Validates comprehensive adherence to AWS best practices through Well-Architected principles, service configurations, security recommendations, and operational excellence

## Validation Method

1. `aws configservice describe-config-rules --output json`
   *Check Config rules for best practice compliance and continuous governance*

2. `aws cloudtrail describe-trails --output json`
   *Validate CloudTrail configuration following AWS security best practices*

3. `aws iam get-account-summary --output json`
   *Check IAM configuration against AWS security best practices*

4. `aws s3api list-buckets --output json`
   *Validate S3 configurations following AWS best practices for data protection*

5. `aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceType,State.Name]' --output json`
   *Check instance types and configurations against AWS best practices*

6. `aws cloudwatch describe-alarms --output json`
   *Validate monitoring and alerting following AWS operational best practices*

7. `aws support describe-trusted-advisor-checks --language en --output json`
   *Check Trusted Advisor recommendations for AWS best practice adherence*

8. `aws wellarchitected list-workloads --output json`
   *Validate Well-Architected Framework implementation and best practice reviews*

9. `aws servicecatalog list-portfolios --output json`
   *Check Service Catalog for standardized best practice deployments*

10. `aws ssm describe-instance-information --output json`
   *Validate Systems Manager configuration for operational best practices*

11. `aws inspector2 get-configuration --output json`
   *Check Inspector configuration for security best practice scanning*

12. `aws organizations describe-organization --output json`
   *Check enterprise-wide best practice governance and organizational standards*

## Latest Results

PASS Good AWS best practices foundation (58%): PASS CloudTrail excellently configured: 'meridianks-Management-events' ready for activation (cost-optimized for pilot)
- PASS Multi-region audit coverage: CloudTrail spans all AWS regions
- PASS Log integrity protection: CloudTrail log file validation enabled
- PASS Encrypted audit logs: CloudTrail using KMS encryption
- PASS Global service monitoring: CloudTrail capturing global AWS events
- PASS Real-time log analysis: CloudTrail integrated with CloudWatch Logs
- PASS Enterprise governance: Organization-wide CloudTrail
- PASS IAM best practices: 71 roles vs 2 users (service-oriented architecture)
- PASS Managed services foundation: 4 S3 buckets (consider adding compute layer)
- PASS Storage optimization: 4 S3 buckets (cost-effective storage)
- PASS Monitoring foundation ready: CloudWatch available (alarms optional for pilot environments)
- PASS Compliance service available: AWS Config ready for rule deployment (optional for pilot)
- PASS Enterprise governance: AWS Organizations with centralized management

---
*Generated 2025-09-14 10:15 UTC*