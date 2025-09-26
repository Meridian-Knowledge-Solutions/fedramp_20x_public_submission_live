# KSI-CNA-04: Use immutable infrastructure with strictly defined functionality and privileges by default.

## Overview

**Category:** Cloud Native Architecture
**Status:** PASS
**Last Check:** 2025-09-26 17:55

**What it validates:** Use immutable infrastructure with strictly defined functionality and privileges by default.

**Why it matters:** Validates immutable infrastructure patterns (IaC, serverless, Auto Scaling) and performs a context-aware, least-privilege analysis for network and IAM configurations to reduce false positives.

## Validation Method

1. `aws ec2 describe-instances --filters 'Name=instance-state-name,Values=running,pending' --query 'Reservations[].Instances[].[InstanceId, Tags, LaunchTime, ImageId]' --output json`
   *Query running instances for IaC tags, naming, and age to assess immutability.*

2. `aws ec2 describe-launch-templates --query 'LaunchTemplates[].LaunchTemplateName' --output json`
   *Validate use of launch templates for standardized, repeatable deployments.*

3. `aws autoscaling describe-auto-scaling-groups --query 'AutoScalingGroups[].AutoScalingGroupName' --output json`
   *Check Auto Scaling Groups for immutable replacement and scaling patterns.*

4. `aws lambda list-functions --query 'Functions[].FunctionName' --output json`
   *Check for serverless functions, which are treated as inherently immutable resources.*

5. `aws s3api list-buckets --query 'Buckets[?contains(Name, `terraform`) || contains(Name, `tfstate`)].[Name]' --output json`
   *Identify S3 buckets used for Terraform state management as direct evidence of IaC.*

6. `aws dynamodb list-tables --query 'TableNames[?contains(@, `terraform-lock`)]' --output json`
   *Identify DynamoDB tables used for Terraform state locking, reinforcing IaC evidence.*

7. `aws ec2 describe-security-groups --query 'SecurityGroups[?length(IpPermissions[?contains(IpRanges[].CidrIp, `0.0.0.0/0`)]) > `0`].[GroupId, GroupName, IpPermissions]' --output json`
   *Check for Security Groups with overly permissive ingress rules from the internet (0.0.0.0/0).*

8. `aws iam list-entities-for-policy --policy-arn arn:aws:iam::aws:policy/AdministratorAccess --query '{PolicyRoles: PolicyRoles}' --output json`
   *Check for any IAM roles using AdministratorAccess for intelligent, exception-based analysis.*

## Latest Results

WARNING Minimal evidence of immutable infrastructure or potential gaps in least privilege (42%): PASS Serverless adoption: 12 Lambda function(s) found (inherently immutable).
- INFO No launch templates found.
- INFO No Auto Scaling Groups found.
- PASS Immutable replacement pattern: High percentage of recent instances.
- PASS IAM Check: AdministratorAccess policy is appropriately restricted.
- INFO IAM Info: Found 3 protected AWS service role(s) with intended AdminAccess.
- PASS Network Check: No sensitive ports found exposed to the internet.
- WARNING IAM Awareness: Human-facing admin role 'AWSReservedSSO_AdministratorAccess_500b4ab3fed23646' is present. Verify assignment and necessity.

---
*Generated 2025-09-26 17:55 UTC*