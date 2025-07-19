# KSI-TPR-01: Identify all third-party information resources

## Overview

**Category:** Third-Party Information Resources
**Status:** PASS
**Last Check:** 2025-07-19 10:35

**What it validates:** Identify all third-party information resources

**Why it matters:** Validates third-party resource identification through service discovery, marketplace usage analysis, and external service integration tracking

## Validation Method

1. `aws marketplace-entitlement list-entitlements --output json`
   *Check AWS Marketplace entitlements for third-party service usage*

2. `aws servicecatalog list-portfolios --output json`
   *Validate Service Catalog for third-party solution deployments and management*

3. **Manual Review:** Check evidence_v2/KSI-TPR-01/ for third_party_inventory.xlsx, vendor_relationship_matrix.pdf, and external_service_dependencies.pdf

## Latest Results

WARNING Partial third-party identification (expand documentation): FAIL No cross-account role data for third-party integration analysis
- PASS Documented third-party inventory: sbom_including_elastic.json, fedramp_moderate_vendor_list.xlsx, Elasticsearch Inc._06.04.2024_Self_Attestation.pdf

---
*Generated 2025-07-19 10:35 UTC*