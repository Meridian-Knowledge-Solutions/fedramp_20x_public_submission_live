# ❌ Failed KSI Validation Report

*Automated report generated from FedRAMP 20x validation pipeline*

## 📊 Executive Summary

- **Overall Pass Rate:** 92.2% (47/51)
- **Failed KSIs:** 4
- **Validation Method:** multi-command-v2
- **Last Updated:** 2025-06-07T07:39:33.491094Z

### Category Breakdown
- **KSI-CMT** (Change Management): 1/5 failed
- **KSI-CNA** (Cloud Native Architecture): 2/7 failed
- **KSI-TPR** (Third-Party Information Resources): 1/4 failed

---

## ❌ Failed KSI Details

### KSI-CMT: Change Management

#### ❌ KSI-CMT-03

**Control:** Change Management
**Reason:** ❌ No automated testing and validation: ❌ No CodeBuild projects for automated testing; ❌ No CodePipelines for automated change validation
**Commands:** `2 commands (2 successful): aws codebuild list-projects --output json; aws codepipeline list-pipelines --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received
**Commands Executed:** 2
**Validated:** 2025-06-07 07:39:33 UTC

---

### KSI-CNA: Cloud Native Architecture

#### ❌ KSI-CNA-05

**Control:** Cloud Native Architecture
**Reason:** ❌ AWS Shield error: 
**Commands:** `1 commands (0 successful): aws shield describe-subscription --output json`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ⚠️ No usable output
**Commands Executed:** 1
**Validated:** 2025-06-07 07:39:33 UTC

#### ❌ KSI-CNA-07

**Control:** Cloud Native Architecture
**Reason:** ❌ Config service error: 
**Commands:** `1 commands (0 successful): aws config describe-config-rules --output json`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ⚠️ No usable output
**Commands Executed:** 1
**Validated:** 2025-06-07 07:39:33 UTC

---

### KSI-TPR: Third-Party Information Resources

#### ❌ KSI-TPR-03

**Control:** Third-Party Information Resources
**Reason:** ❌ No supply chain risk assessment and mitigation found in evidence_v2/KSI-TPR-03/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-07 07:39:33 UTC

---
## 🔧 Remediation Guidance

### Configuration Issues (1 KSIs)
- **Action:** Review and fix AWS service configurations
- **Priority:** Medium - Configuration changes needed
- **Affected KSIs:** KSI-CMT-03

### Technical Issues (2 KSIs)
- **Action:** Check AWS CLI configuration, permissions, and service availability
- **Priority:** High - Technical resolution needed
- **Affected KSIs:** KSI-CNA-05, KSI-CNA-07

### Missing Documentation (1 KSIs)
- **Action:** Upload required evidence to appropriate `evidence_v2/KSI-*/` directories
- **Priority:** Medium - Manual evidence required
- **Affected KSIs:** KSI-TPR-03
---

*Report generated on 2025-06-07 07:39:33 UTC*
*Source: unified_ksi_validations.json*
