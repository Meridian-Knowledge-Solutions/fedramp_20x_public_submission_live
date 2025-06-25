# KSI-PIY-01: Have an up-to-date information resource inventory or code defining all deployed assets, software, and services

## Overview

**Category:** Policy and Inventory
**Status:** PASS
**Last Check:** 2025-06-25 18:26

**What it validates:** Have an up-to-date information resource inventory or code defining all deployed assets, software, and services

**Why it matters:** Validates asset inventory through AWS resource discovery and documented inventory records

## Validation Method

1. `aws resourcegroupstaggingapi get-resources --output json`
   *Get comprehensive resource inventory across all AWS services*

2. **Manual Review:** Check evidence_v2/KSI-PIY-01/ for asset_inventory.xlsx and software_inventory.pdf

## Latest Results

WARNING Partial inventory coverage (expand documentation): PASS AWS resource inventory: 73 tagged resources discovered
- FAIL No manual asset inventory documentation found

---
*Generated 2025-06-25 18:26 UTC*