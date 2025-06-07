# ❌ Failed KSI Validation Report

*Automated report generated from FedRAMP 20x validation pipeline*

## 📊 Executive Summary

- **Overall Pass Rate:** 96.1% (49/51)
- **Failed KSIs:** 2
- **Validation Method:** multi-command-v2
- **Last Updated:** 2025-06-07T20:23:23.920130Z

### Category Breakdown
- **KSI-CMT** (Change Management): 1/5 failed
- **KSI-CNA** (Cloud Native Architecture): 1/7 failed

---

## ❌ Failed KSI Details

### KSI-CMT: Change Management

#### ❌ KSI-CMT-03

**Control:** Change Management
**Reason:** ❌ No automated testing and validation: ❌ No CodeBuild projects for automated testing; ❌ No CodePipelines for automated change validation
**Commands:** `2 commands (2 successful): aws codebuild list-projects --output json; aws codepipeline list-pipelines --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received
**Commands Executed:** 2
**Validated:** 2025-06-07 20:23:23 UTC

---

### KSI-CNA: Cloud Native Architecture

#### ❌ KSI-CNA-05

**Control:** Cloud Native Architecture
**Reason:** ❌ AWS Shield error: 
**Commands:** `1 commands (0 successful): aws shield describe-subscription --output json`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ⚠️ No usable output
**Commands Executed:** 1
**Validated:** 2025-06-07 20:23:23 UTC

---
## 🔧 Remediation Guidance

### Configuration Issues (1 KSIs)
- **Action:** Review and fix AWS service configurations
- **Priority:** Medium - Configuration changes needed
- **Affected KSIs:** KSI-CMT-03

### Technical Issues (1 KSIs)
- **Action:** Check AWS CLI configuration, permissions, and service availability
- **Priority:** High - Technical resolution needed
- **Affected KSIs:** KSI-CNA-05
---

*Report generated on 2025-06-07 20:23:23 UTC*
*Source: unified_ksi_validations.json*
