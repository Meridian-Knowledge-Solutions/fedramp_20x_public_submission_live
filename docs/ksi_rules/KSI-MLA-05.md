# KSI-MLA-05: Perform Infrastructure as Code and configuration evaluation and testing

## Overview

**Category:** Monitoring, Logging, and Auditing
**Status:** PASS
**Last Check:** 2025-06-23 08:29

**What it validates:** Perform Infrastructure as Code and configuration evaluation and testing

**Why it matters:** Validates comprehensive Infrastructure as Code security evaluation from basic CloudFormation deployment to enterprise-grade multi-account governance, automated testing, and configuration compliance management

## Validation Method

1. `aws config describe-config-rules --output json`
   *Check Config rules for Infrastructure as Code evaluation and configuration compliance monitoring*

2. `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
   *Validate CloudFormation stacks for Infrastructure as Code configuration testing and deployment*

3. `aws cloudformation describe-stacks --output json`
   *Analyze detailed stack configuration for drift detection and infrastructure validation*

4. `aws ssm describe-parameters --max-results 50 --output json`
   *Check Systems Manager Parameter Store for centralized configuration management*

5. `aws codebuild list-projects --output json`
   *Validate automated Infrastructure as Code testing through build projects and validation pipelines*

6. `aws codepipeline list-pipelines --output json`
   *Check for automated Infrastructure as Code deployment pipelines and change validation*

7. `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=CreateStack --start-time 2025-05-01 --output json`
   *Analyze deployment audit trail for Infrastructure as Code change tracking and compliance*

8. `aws resourcegroupstaggingapi get-resources --resource-type-filters cloudformation --output json`
   *Check resource inventory and tag-based governance for Infrastructure as Code assets*

9. `aws organizations describe-organization --output json`
   *Validate enterprise-level multi-account governance for Infrastructure as Code standardization*

10. `aws servicecatalog search-products --output json`
   *Check standardized Infrastructure as Code templates and governance through Service Catalog*

## Latest Results

PASS Enterprise-grade Infrastructure as Code evaluation and testing: PASS Infrastructure as Code deployment: 8/8 successful CloudFormation stacks
- PASS Parameterized configuration management: 5 SSM parameters
- WARNING No Config rules for infrastructure evaluation
- PASS Infrastructure drift detection: 8 stacks monitored
- INFO No automated testing projects (consider for production)
- INFO No automated deployment pipelines (consider for production)
- PASS Deployment audit trail: 2 tracked deployment events
- PASS Resource governance: 2 managed CloudFormation resources
- PASS Enterprise multi-account governance: AWS Organizations enabled

---
*Generated 2025-06-23 08:29 UTC*