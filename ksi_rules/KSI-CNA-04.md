# KSI-CNA-04: Use immutable infrastructure with strictly defined functionality and privileges by default

## Overview

**Category:** Cloud Native Architecture
**Status:** FAIL
**Last Check:** 2025-09-24 03:26

**What it validates:** Use immutable infrastructure with strictly defined functionality and privileges by default

**Why it matters:** Validates immutable infrastructure patterns, IaC, serverless adoption, and least-privilege configurations for network and IAM.

## Validation Method

1. `aws ec2 describe-instances --filters 'Name=instance-state-name,Values=running,pending' --query 'Reservations[].Instances[].[InstanceId, Tags, LaunchTime, ImageId]' --output json`
   *Query running instances for IaC tags, naming, and age.*

2. `aws ec2 describe-launch-templates --query 'LaunchTemplates[].LaunchTemplateName' --output json`
   *Validate use of launch templates for standardized deployments.*

3. `aws autoscaling describe-auto-scaling-groups --query 'AutoScalingGroups[].AutoScalingGroupName' --output json`
   *Check Auto Scaling Groups for immutable replacement patterns.*

4. `aws lambda list-functions --query 'Functions[].FunctionName' --output json`
   *Check for serverless functions as immutable resources.*

5. `aws s3api list-buckets --query 'Buckets[?contains(Name, `terraform`) || contains(Name, `tfstate`)].[Name]' --output json`
   *Identify S3 buckets used for Terraform state management.*

6. `aws dynamodb list-tables --query 'TableNames[?contains(@, `terraform-lock`)]' --output json`
   *Identify DynamoDB tables used for Terraform state locking.*

7. `aws ec2 describe-security-groups --query 'SecurityGroups[?length(IpPermissions[?contains(IpRanges[].CidrIp, `0.0.0.0/0`)]) > `0`].[GroupId, GroupName, IpPermissions]' --output json`
   *NEW: Check for Security Groups with overly permissive ingress rules from the internet.*

8. `aws iam list-entities-for-policy --policy-arn arn:aws:iam::aws:policy/AdministratorAccess --query 'PolicyRoles[].RoleName' --output json`
   *NEW: Check for any IAM roles using the AWS-managed AdministratorAccess policy.*

## Latest Results

FAIL CRITICAL least privilege violation detected: CRITICAL: The AdministratorAccess policy is attached to role(s): githubactions_role, OrganizationAccountAccessRole, AWSControlTowerExecution, stacksets-exec-d5e511141f10f5aa9846491550c31da6, SSM-CR-Execution-Role, aws-controltower-AdministratorExecutionRole, AWSReservedSSO_AdministratorAccess_500b4ab3fed23646, CodePipelineServiceRoles, CodeBuildServiceRoles.
- CRITICAL: Security Group(s) expose sensitive ports to 0.0.0.0/0: launch-wizard-2 (Port: 22), launch-wizard-1 (Port: 22).

---
*Generated 2025-09-24 03:26 UTC*