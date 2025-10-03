# KSI-CMT-02: Use self-service templates and image repositories for provisioning

## Overview

**Category:** Change Management
**Status:** PASS
**Last Check:** 2025-10-03 19:13

**What it validates:** Use self-service templates and image repositories for provisioning

**Why it matters:** Validates comprehensive self-service provisioning from basic AMIs to enterprise-grade service catalogs and automated deployment templates

## Validation Method

1. `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
   *Check CloudFormation stacks for infrastructure templates*

2. `aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,ImageId,LaunchTime]' --output json`
   *Validate EC2 instances using standardized AMIs*

3. `aws ec2 describe-launch-templates --output json`
   *Check launch templates for self-service provisioning*

4. `aws autoscaling describe-auto-scaling-groups --output json`
   *Validate auto-scaling using standardized templates*

5. `aws lambda list-functions --output json`
   *Check Lambda functions for serverless self-service deployment*

6. `aws deploy list-applications --output json`
   *Validate CodeDeploy applications for automated deployment*

7. `aws ecr describe-repositories --output json`
   *Check ECR repositories for container image templates*

8. `aws servicecatalog search-products --output json`
   *Validate Service Catalog for self-service product templates*

9. `aws organizations describe-organization --output json`
   *Check organization-wide standardized provisioning policies*

## Latest Results

PASS Production-ready immutable deployment with Terraform Infrastructure as Code (75%): PASS Immutable infrastructure foundation: 12/12 successful CloudFormation deployments (100%)
- PASS External Terraform Infrastructure as Code: 9 managed files documented
- PASS Immutable deployment method: Terraform Infrastructure as Code
- PASS Automated immutable deployment: GitHub Actions CI/CD integration
- PASS Infrastructure as Code validation: Automated deployment pipeline
- PASS Serverless-first immutable architecture: No EC2 instances by design
- PASS External Terraform management: Infrastructure as Code via external automation
- PASS Version-controlled immutable deployments: Infrastructure changes via Git
- PASS Serverless-first immutable architecture: 12 Lambda functions (no EC2 instances expected)
- 🎯 External Infrastructure as Code excellence: Advanced immutable deployment automation
- PASS Immutable serverless functions: 12 Lambda functions (inherently immutable)
- PASS Infrastructure as Code configuration: Terraform-managed configuration patterns detected
- INFO No load balancer target groups for blue/green deployment patterns
- PASS Configuration drift detection: CloudFormation enables immutable infrastructure drift monitoring
- INFO No Config rules for immutable deployment compliance monitoring
- PASS Enterprise-wide immutable deployment governance: AWS Organizations enables centralized deployment policies
- PASS Advanced organization features: SCPs for immutable deployment policy enforcement enabled

---
*Generated 2025-10-03 19:13 UTC*