# KSI-CMT-05: Analyze security impact of changes before implementation

## Overview

**Category:** Change Management
**Status:** FAIL
**Last Check:** 2025-10-03 19:13

**What it validates:** Analyze security impact of changes before implementation

**Why it matters:** Validates pre-change impact assessment through terraform plans, patch compliance reports, and Change Manager request documentation

## Validation Method

1. `aws s3 ls s3://$(aws s3api list-buckets --query 'Buckets[?contains(Name, `terraform`) || contains(Name, `tfstate`)].Name | [0]' --output text)/plans/ --recursive 2>/dev/null | tail -20 || echo 'No plans found'`
   *Terraform plans as evidence of IaC impact assessment*

2. `aws ssm describe-patch-baselines --output json`
   *Patch baseline definitions showing patching impact scope*

3. `aws ssm describe-instance-patch-states --instance-id $(aws ssm describe-instance-information --query 'InstanceInformationList[0].InstanceId' --output text) --output json 2>/dev/null || echo '{"InstancePatchStates": []}'`
   *Patch compliance state as pre-patching impact assessment*

4. `aws ssm get-change-request-list --max-results 50 --output json 2>/dev/null || echo '{"ChangeRequestSummaryItems": []}'`
   *Change Manager requests containing documented change impacts*

5. `aws s3api list-buckets --query 'Buckets[?contains(Name, `terraform`) || contains(Name, `tfstate`)].Name' --output json`
   *Verify terraform state bucket exists (baseline for plan storage)*

## Latest Results

FAIL Insufficient impact assessment evidence (20%): FAIL No terraform plan evidence found - IaC impact assessment not documented
- PASS Patch baselines defined: 17 baseline(s)
- INFO No Change Manager requests found - may not be actively used yet

---
*Generated 2025-10-03 19:13 UTC*