# KSI-IAM-01: Enforce phishing-resistant MFA for all user authentication

## Overview

**Category:** Identity and Access Management
**Status:** PASS
**Last Check:** 2025-06-23 02:20

**What it validates:** Enforce phishing-resistant MFA for all user authentication

**Why it matters:** Validates MFA enforcement through Identity Center configuration evidence showing always-on MFA requirements, combined with traditional IAM user analysis

## Validation Method

1. `aws iam list-users --output json`
   *Get traditional IAM users for MFA analysis*

2. `aws iam list-mfa-devices --output json`
   *Check traditional IAM MFA devices*

3. `aws sso-admin list-instances --output json`
   *Get Identity Center instances*

4. `aws identitystore list-users --identity-store-id d-9067ccc0ff --output json`
   *Get Identity Center users for accurate user count*

5. **Manual Review:** Check evidence_v2/KSI-IAM-01/ for sso_mfa_enforcement_screenshot.png showing Identity Center MFA always-on configuration

## Latest Results

PASS Strong MFA coverage (80% coverage): PASS Identity Center: 1 active instance(s)
- PASS Identity Center users: 8
- PASS MFA enforcement evidence: Identity Center MFA always-on configuration
- Traditional IAM users: 2

---
*Generated 2025-06-23 02:20 UTC*