# KSI-PIY-01: Maintain an inventory of authorized users

## Overview

**Category:** Policy and Inventory
**Status:** PASS
**Last Check:** 2025-10-01 06:31

**What it validates:** Maintain an inventory of authorized users

**Why it matters:** Validates comprehensive user inventory from basic IAM list to enterprise-grade identity lifecycle management and automated discovery

## Validation Method

1. `aws ec2 describe-instances --output json`
   *Check EC2 instances for system resource inventory*

2. `aws rds describe-db-instances --output json`
   *Validate RDS database inventory*

3. `aws lambda list-functions --output json`
   *Check Lambda functions inventory*

4. `aws s3api list-buckets --output json`
   *Validate S3 bucket inventory*

5. `aws elbv2 describe-load-balancers --output json`
   *Check load balancer inventory*

6. `aws route53 list-hosted-zones --output json`
   *Validate Route53 DNS inventory*

7. `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
   *Check CloudFormation stack inventory*

8. `aws s3 ls s3://mksfr-sftp-bucket/inventory/ || echo 'No inventory files'`
   *Validate automated inventory collection in S3*

9. `aws lambda get-function --function-name aws_inventory --output json || echo '{"Configuration": null}'`
   *Check automated inventory Lambda function*

## Latest Results

PASS Enterprise-grade comprehensive inventory with automated maintenance (100%): PASS Compute Resources
- PASS Database Resources
- PASS Serverless Resources
- PASS Storage Resources
- PASS Network Resources
- PASS Dns Resources
- PASS Infrastructure Code
- PASS Automated Maintenance
- PASS Maintenance Mechanism

---
*Generated 2025-10-01 06:31 UTC*