# KSI-PIY-01: Establish and maintain complete inventories of all information resources

## Overview

**Category:** Policy and Inventory
**Status:** PASS
**Last Check:** 2025-09-16 04:08

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

8. `aws s3 ls s3://mksfr-sftp-bucket/inventory/`
   *Validate automated inventory file generation frequency and availability via daily Lambda scanning*

9. `aws lambda get-function --function-name aws_inventory --output json 2>/dev/null || aws lambda list-functions --query 'Functions[?contains(FunctionName, `inventory`) || contains(FunctionName, `scanner`)]' --output json`
   *Verify automated inventory scanning Lambda function configuration and automation capability*

10. `LATEST_FILE=$(aws s3 ls s3://mksfr-sftp-bucket/inventory/ --recursive | grep 'inventory_.*\.csv' | sort -k1,2 | tail -n1 | awk '{print $4}'); if [ -n "$LATEST_FILE" ]; then aws s3 cp s3://mksfr-sftp-bucket/$LATEST_FILE /tmp/current_inventory.csv --only-show-errors && echo '{"inventory_download": "success", "file": "'$(basename $LATEST_FILE)'"}' || echo '{"inventory_download": "failed", "reason": "download_error"}'; else echo '{"inventory_download": "failed", "reason": "no_inventory_files"}'; fi`
   *Download most recent automated inventory CSV file from daily Lambda automation with proper fallback handling*

11. `aws config describe-configuration-recorders --output json 2>/dev/null || echo '{"ConfigurationRecorders": []}'`
   *Check if Config service is enabled before attempting resource discovery*

12. `if aws config describe-configuration-recorders --output json 2>/dev/null | grep -q '"Name"'; then aws config list-discovered-resources --resource-type AWS::S3::Bucket --query 'resourceIdentifiers[*].[resourceType,resourceId,resourceName]' --output json; else echo '{"resourceIdentifiers": [], "note": "Config service not enabled"}'; fi`
   *Config service comprehensive S3 bucket discovery for cross-validation (if Config enabled)*

13. `if aws config describe-configuration-recorders --output json 2>/dev/null | grep -q '"Name"'; then aws config list-discovered-resources --resource-type AWS::Lambda::Function --query 'resourceIdentifiers[*].[resourceType,resourceId,resourceName]' --output json; else echo '{"resourceIdentifiers": [], "note": "Config service not enabled"}'; fi`
   *Config service comprehensive Lambda function discovery for automated inventory validation (if Config enabled)*

14. `aws s3api list-objects-v2 --bucket mksfr-sftp-bucket --prefix inventory/ --query 'sort_by(Contents[?ends_with(Key, `.csv`)], &LastModified)[-1]' --output json`
   *Get metadata of most recent inventory CSV file to validate daily automation freshness*

15. `aws events list-rules --output json`
   *List all EventBridge rules to identify automation scheduling (may use different naming patterns)*

16. `aws logs filter-log-events --log-group-name '/aws/lambda/aws_inventory' --start-time $(date -d '7 days ago' +%s)000 --filter-pattern 'SUCCESS' --max-items 5 --output json 2>/dev/null || echo '{"events": [], "note": "Log group not found or no recent events"}'`
   *Validate recent successful inventory automation executions via Lambda logs*

## Latest Results

PASS Enterprise-grade comprehensive automated inventory with validated daily automation (85%): PASS Compute Resources
- PASS Database Resources
- PASS Serverless Resources
- PASS Storage Resources
- PASS Network Resources
- PASS Dns Resources
- PASS Infrastructure Code
- PASS Automated Inventory Scanning
- PASS Inventory Data Storage
- PASS Inventory Freshness Tracking
- FAIL Comprehensive Inventory Coverage
- PASS Automation Scheduling
- FAIL Automation Execution Logs

---
*Generated 2025-09-16 04:08 UTC*