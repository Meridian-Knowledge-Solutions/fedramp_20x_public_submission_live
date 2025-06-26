# KSI-CMT-02: Execute changes through redeployment of version controlled immutable resources rather than direct modification wherever possible

## Overview

**Category:** Change Management
**Status:** FAIL
**Last Check:** 2025-06-26 02:53

**What it validates:** Execute changes through redeployment of version controlled immutable resources rather than direct modification wherever possible

**Why it matters:** Validates comprehensive immutable deployment capabilities from pilot to enterprise maturity levels through CloudFormation, Launch Templates, containers, serverless, and governance

## Validation Method

1. `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE UPDATE_ROLLBACK_COMPLETE --output json`
   *Check CloudFormation stacks for AWS-managed immutable infrastructure foundation*

2. `aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags,LaunchTime,ImageId]' --output json`
   *Analyze instance patterns for Terraform-managed immutable deployments (consistent tagging, recent launches)*

3. `aws lambda list-functions --max-items 50 --output json`
   *Check Lambda functions for immutable serverless deployment patterns*

4. `aws s3api list-buckets --query 'Buckets[?contains(Name, `terraform`) || contains(Name, `tfstate`)]' --output json`
   *Detect Terraform state management patterns (S3 backend indicates mature Infrastructure as Code)*

5. `aws ssm describe-parameters --output json`
   *Validate Systems Manager parameters for external configuration management and versioning*

6. `aws elbv2 describe-target-groups --max-items 50 --output json`
   *Check load balancer target groups for blue/green immutable deployment infrastructure*

7. `aws configservice describe-config-rules --output json`
   *Evaluate Config rules for immutable deployment compliance and governance (optional for Terraform-managed infrastructure)*

8. `aws organizations describe-organization --output json 2>/dev/null || echo '{"Organization": null}'`
   *Check for enterprise-wide immutable deployment governance through AWS Organizations*

## Latest Results

- Exception during evaluation: No module named 'dateutil'

---
*Generated 2025-06-26 02:53 UTC*