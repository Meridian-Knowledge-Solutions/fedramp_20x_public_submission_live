# KSI-CNA-04: Clearly define and deploy security controls as code to enforce the principle of least functionality

## Overview

**Category:** Cloud Native Architecture
**Status:** FAIL
**Last Check:** 2025-10-01 18:40

**What it validates:** Clearly define and deploy security controls as code to enforce the principle of least functionality

**Why it matters:** Validates Infrastructure as Code security controls from basic CloudFormation to enterprise-grade policy-driven deployment with automated compliance

## Validation Method

1. `aws ec2 describe-instances --filters 'Name=instance-state-name,Values=running' --output json`
   *Check running instances for least functionality and minimal services*

2. `aws ec2 describe-launch-templates --query 'LaunchTemplates[].{Name:LaunchTemplateName,Id:LaunchTemplateId}' --output json`
   *Validate launch templates for codified security configurations*

3. `aws autoscaling describe-auto-scaling-groups --query 'AutoScalingGroups[].{Name:AutoScalingGroupName,LaunchTemplate:LaunchTemplate}' --output json`
   *Check auto-scaling groups using infrastructure as code templates*

4. `aws lambda list-functions --query 'Functions[].FunctionName' --output json`
   *Validate Lambda functions deployed with least privilege configurations*

5. `aws s3api list-buckets --query 'Buckets[?contains(Name, `terraform`) || contains(Name, `cloudformation`)].Name' --output json`
   *Check for IaC state storage and deployment automation*

6. `aws dynamodb list-tables --query 'TableNames[?contains(@, `terraform`) || contains(@, `state`)]' --output json`
   *Validate DynamoDB tables used for IaC state locking*

7. `aws ec2 describe-security-groups --query 'SecurityGroups[?length(IpPermissions) <= `3`].{GroupName:GroupName,Rules:length(IpPermissions)}' --output json`
   *Check security groups following least functionality principle*

8. `aws iam list-entities-for-policy --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess --output json`
   *Validate read-only policy attachments for principle of least privilege*

## Latest Results

- FAIL CRITICAL least privilege violation detected: CRITICAL: Unapproved AdministratorAccess policy attached to role(s): aws-controltower-ReadOnlyExecutionRole, aws-controltower-ConfigRecorderRole, AWSReservedSSO_ReadOnlyAccess_c4a62adfd2671015.

---
*Generated 2025-10-01 18:40 UTC*