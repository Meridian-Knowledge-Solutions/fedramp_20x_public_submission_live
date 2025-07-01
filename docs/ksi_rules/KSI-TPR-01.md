# KSI-TPR-01: Identify all third-party information resources

## Overview

**Category:** Third-Party Information Resources
**Status:** PASS
**Last Check:** 2025-07-01 03:31

**What it validates:** Identify all third-party information resources

**Why it matters:** Validates third-party resource identification through AWS services and documented third-party inventory

## Validation Method

1. `aws iam list-roles --query 'Roles[?contains(AssumeRolePolicyDocument, `sts:AssumeRole`)]' --output json`
   *Check for cross-account roles indicating third-party integrations*

2. **Manual Review:** Check evidence_v2/KSI-TPR-01/ for third_party_inventory.xlsx, saas_services_list.pdf, and vendor_registry.pdf

## Latest Results

- WARNING Partial third-party identification (expand documentation): PASS Documented third-party inventory: sbom_including_elastic.json, fedramp_moderate_vendor_list.xlsx, Elasticsearch Inc._06.04.2024_Self_Attestation.pdf

---
*Generated 2025-07-01 03:31 UTC*