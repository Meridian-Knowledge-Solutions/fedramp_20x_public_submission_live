# KSI-PIY-01: Establish and maintain complete inventories of all information resources

## Overview

**Category:** Policy and Inventory
**Status:** PASS
**Last Check:** 2025-09-16 00:12

**What it validates:** Establish and maintain complete inventories of all information resources

**Why it matters:** Comprehensive AWS resource discovery through native APIs provides real-time automated inventory validation

## Validation Method

1. `aws ec2 describe-instances --output json`
   *EC2 compute instance inventory with state and configuration details*

2. `aws rds describe-db-instances --output json`
   *RDS database instance inventory with configuration and backup settings*

3. `aws lambda list-functions --output json`
   *Lambda serverless function inventory with runtime and configuration details*

4. `aws s3api list-buckets --output json`
   *S3 storage bucket inventory for data storage resources*

5. `aws elbv2 describe-load-balancers --output json`
   *Load balancer inventory for traffic distribution resources*

6. `aws route53 list-hosted-zones --output json`
   *DNS zone inventory for domain and routing resources*

7. `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
   *Infrastructure as Code stack inventory for managed resource collections*

8. `aws s3 ls s3://mksfr-sftp-bucket/inventory/ --output json`
   *Validate automated inventory file generation frequency and availability via daily Lambda scanning*

9. `aws lambda get-function --function-name inventory-scanner --output json 2>/dev/null || aws lambda list-functions --query 'Functions[?contains(FunctionName, `inventory`) || contains(FunctionName, `scanner`)]' --output json`
   *Verify automated inventory scanning Lambda function configuration and automation capability*

10. `aws s3 cp s3://mksfr-sftp-bucket/inventory/inventory_$(date +%Y-%m-%d)T*Z.csv /tmp/current_inventory.csv --only-show-errors && echo '{"inventory_download": "success"}' || echo '{"inventory_download": "file_not_found"}'`
   *Download and validate current automated inventory CSV file from daily Lambda scan*

11. `aws config list-discovered-resources --resource-type AWS::S3::Bucket --query 'resourceIdentifiers[*].[resourceType,resourceId,resourceName]' --output json`
   *Config service comprehensive S3 bucket discovery for cross-validation with automated inventory*

12. `aws config list-discovered-resources --resource-type AWS::Lambda::Function --query 'resourceIdentifiers[*].[resourceType,resourceId,resourceName]' --output json`
   *Config service comprehensive Lambda function discovery for automated inventory validation*

## Latest Results

PASS Good comprehensive inventory from authoritative AWS sources with automation (64%): PASS Comprehensive compute inventory: 5 EC2 instances
- PASS Database inventory: 1 RDS instances
- PASS Serverless inventory: 8 Lambda functions
- PASS Storage inventory: 4 S3 buckets
- PASS Network inventory: 1 load balancers
- PASS DNS inventory: 1 Route53 hosted zones
- PASS Comprehensive IaC inventory: 10 CloudFormation stacks
- PASS Serverless inventory: 1 Lambda functions
- INFO Inventory file not found for current date - may be generated at different time

---
*Generated 2025-09-16 00:12 UTC*