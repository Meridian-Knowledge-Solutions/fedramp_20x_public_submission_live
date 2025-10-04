# KSI-CMT-04: Have a documented change management procedure

## Overview

**Category:** Change Management
**Status:** FAIL
**Last Check:** 2025-10-04 02:56

**What it validates:** Have a documented change management procedure

**Why it matters:** Validates hybrid change management: Change Manager templates for high-risk operational changes + IaC workflow for infrastructure deployments

## Validation Method

1. `aws ssm list-documents --filters 'Key=Owner,Values=Self' 'Key=DocumentType,Values=Automation' --output json`
   *List custom Change Manager automation templates*

2. `aws ssm describe-document --name $(aws ssm list-documents --filters 'Key=Owner,Values=Self' 'Key=DocumentType,Values=Automation' --query 'DocumentIdentifiers[0].Name' --output text) --output json 2>/dev/null || echo '{"Document": null}'`
   *Retrieve first custom template to validate approval configuration*

3. `aws ssm get-change-request-list --filters 'Key=DocumentName,Values=$(aws ssm list-documents --filters Key=Owner,Values=Self --query DocumentIdentifiers[0].Name --output text)' --max-results 50 --output json 2>/dev/null || echo '{"ChangeRequestSummaryItems": []}'`
   *Check for Change Manager execution history*

4. `aws s3api list-buckets --query 'Buckets[?contains(Name, `terraform`) || contains(Name, `tfstate`)].Name' --output json`
   *Validate terraform state storage (IaC change tracking)*

5. `aws dynamodb list-tables --query 'TableNames[?contains(@, `terraform`) || contains(@, `lock`)]' --output json`
   *Validate terraform state locking (IaC coordination)*

6. `aws ssm get-parameter --name '/change-management/procedures' --output json || echo '{"Parameter": null}'`
   *Check for documented change management procedures*

## Latest Results

FAIL No change management system detected (0%): FAIL No custom Change Manager templates found
- WARNING No IaC state management detected - verify terraform configuration

---
*Generated 2025-10-04 02:56 UTC*