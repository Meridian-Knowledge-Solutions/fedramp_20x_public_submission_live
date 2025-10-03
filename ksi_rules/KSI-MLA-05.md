# KSI-MLA-05: Use change management tools to enforce, track and report configuration changes

## Overview

**Category:** Monitoring, Logging, and Auditing
**Status:** PASS
**Last Check:** 2025-10-03 02:59

**What it validates:** Use change management tools to enforce, track and report configuration changes

**Why it matters:** Validates comprehensive change tracking from basic CloudTrail to enterprise-grade automated governance and compliance reporting

## Validation Method

1. `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
   *Check CloudFormation stacks for infrastructure change management*

2. `aws cloudformation describe-stacks --output json`
   *Validate stack details for change tracking and history*

3. `aws ssm describe-parameters --max-results 50 --output json`
   *Check SSM parameters for configuration change management*

4. `aws codebuild list-projects --output json`
   *Validate CodeBuild for automated change deployment pipelines*

5. `aws codepipeline list-pipelines --output json`
   *Check CodePipeline for change management automation*

6. `aws cloudtrail lookup-events --lookup-attributes AttributeKey=ResourceType,AttributeValue=AWS::CloudFormation::Stack --max-items 20 --output json`
   *Validate CloudTrail audit logs for configuration changes*

7. `aws resourcegroupstaggingapi get-resources --resource-type-filters cloudformation --output json`
   *Check resource tagging for change management governance*

8. `aws organizations describe-organization --output json`
   *Validate organization-wide change management policies*

9. `aws servicecatalog search-products --output json`
   *Check Service Catalog for standardized change templates*

## Latest Results

PASS Enterprise-grade Infrastructure as Code evaluation and testing (100%): PASS Enterprise IaC governance: 5 Control Tower baseline stacks
- PASS Multi-account orchestration: 1 execution role stacks
- PASS Automated configuration deployment: 6 Quick Setup stacks
- PASS Infrastructure as Code deployment: 12/12 successful CloudFormation stacks
- PASS Centralized configuration management: 7 SSM parameters (4 encrypted)
- PASS Configuration governance: 1 compliance parameters
- PASS Enterprise compliance governance: Control Tower manages Config rules centrally
- PASS Infrastructure drift monitoring: 12 stacks tracked
- PASS Secure IAM deployment: 12 stacks with proper capabilities
- PASS Automated IaC testing: 3 CodeBuild projects
- PASS Deployment audit trail: 11 tracked CloudFormation events
- PASS Resource governance: 6 tagged CloudFormation resources
- PASS Enterprise multi-account governance: AWS Organizations with ALL features enabled
- PASS Organizational infrastructure: Centralized account management

---
*Generated 2025-10-03 02:59 UTC*