# KSI-PIY-01: Establish and maintain complete inventories of all information resources

## Overview

**Category:** Policy and Inventory
**Status:** PASS
**Last Check:** 2025-09-16 03:14

**What it validates:** Establish and maintain complete inventories of all information resources

**Why it matters:** Comprehensive AWS resource discovery through native APIs provides real-time automated inventory validation PLUS automated inventory management through Lambda-based daily scanning and auditable S3 storage

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

10. `LATEST_FILE=$(aws s3 ls s3://mksfr-sftp-bucket/inventory/ --recursive | grep 'inventory_.*\.csv' | sort -k1,2 | tail -n1 | awk '{print $4}'); if [ -n "$LATEST_FILE" ]; then aws s3 cp s3://mksfr-sftp-bucket/$LATEST_FILE /tmp/current_inventory.csv --only-show-errors && echo '{"inventory_download": "success", "file": "'$(basename $LATEST_FILE)'"}' || echo '{"inventory_download": "failed", "reason": "download_error"}'; else echo '{"inventory_download": "failed", "reason": "no_inventory_files"}'; fi`
   *Download most recent automated inventory CSV file from daily Lambda automation with proper fallback handling*

11. `aws config list-discovered-resources --resource-type AWS::S3::Bucket --query 'resourceIdentifiers[*].[resourceType,resourceId,resourceName]' --output json`
   *Config service comprehensive S3 bucket discovery for cross-validation with automated inventory*

12. `aws config list-discovered-resources --resource-type AWS::Lambda::Function --query 'resourceIdentifiers[*].[resourceType,resourceId,resourceName]' --output json`
   *Config service comprehensive Lambda function discovery for automated inventory validation*

13. `aws s3api list-objects-v2 --bucket mksfr-sftp-bucket --prefix inventory/ --query 'sort_by(Contents, &LastModified)[-1]' --output json`
   *Get metadata of most recent inventory file to validate daily automation freshness and file generation*

14. `aws events list-rules --name-prefix inventory --output json`
   *Verify EventBridge rules for daily inventory automation scheduling*

15. `aws logs filter-log-events --log-group-name '/aws/lambda/inventory-scanner' --start-time $(date -d '7 days ago' +%s)000 --filter-pattern 'SUCCESS' --max-items 5 --output json`
   *Validate recent successful inventory automation executions via Lambda logs*

## Latest Results

PASS Good comprehensive inventory from authoritative AWS sources with automation (54%): PASS Comprehensive compute inventory: 5 EC2 instances
- PASS Database inventory: 1 RDS instances
- PASS Serverless inventory: 8 Lambda functions
- PASS Storage inventory: 4 S3 buckets
- PASS Network inventory: 1 load balancers
- PASS DNS inventory: 1 Route53 hosted zones
- PASS Comprehensive IaC inventory: 10 CloudFormation stacks
- PASS Serverless inventory: 1 Lambda functions
- INFO S3 file metadata detected but not inventory format
- INFO No EventBridge automation rules found
- INFO No recent Lambda execution logs found

---
*Generated 2025-09-16 03:14 UTC*