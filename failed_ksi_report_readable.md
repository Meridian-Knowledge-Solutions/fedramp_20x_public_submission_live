# ❌ Failed KSI Validation Report

*Automated report generated from FedRAMP 20x validation pipeline*

## 📊 Executive Summary

- **Overall Pass Rate:** 60.8% (31/51)
- **Failed KSIs:** 20
- **Validation Method:** multi-command-v2
- **Last Updated:** 2025-06-06T08:10:04.439076Z

### Category Breakdown
- **KSI-CNA** (Cloud Native Architecture): 2/7 failed
- **KSI-CMT** (Change Management): 2/5 failed
- **KSI-IAM** (Identity and Access Management): 3/6 failed
- **KSI-SVC** (Service Configuration): 1/7 failed
- **KSI-MLA** (Monitoring, Logging, and Auditing): 2/6 failed
- **KSI-PIY** (Policy and Inventory): 2/7 failed
- **KSI-RPL** (Recovery Planning): 3/4 failed
- **KSI-TPR** (Third-Party Information Resources): 3/4 failed
- **KSI-INR** (Incident Reporting): 2/3 failed

---

## ❌ Failed KSI Details

### KSI-CMT: Change Management

#### ❌ KSI-CMT-03

**Control:** Change Management
**Reason:** ❌ No automated testing and validation: ❌ No CodeBuild projects for automated testing; ❌ No CodePipelines for automated change validation
**Commands:** `2 commands (2 successful): aws codebuild list-projects --output json; aws codepipeline list-pipelines --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received
**Commands Executed:** 2
**Validated:** 2025-06-06 08:10:04 UTC

#### ❌ KSI-CMT-05

**Control:** Change Management
**Reason:** ❌ No risk and impact evaluation documentation found in evidence_v2/KSI-CMT-05/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 08:10:04 UTC

---

### KSI-CNA: Cloud Native Architecture

#### ❌ KSI-CNA-05

**Control:** Cloud Native Architecture
**Reason:** ❌ AWS Shield error: 
**Commands:** `1 commands (0 successful): aws shield describe-subscription --output json`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ⚠️ No usable output
**Commands Executed:** 1
**Validated:** 2025-06-06 08:10:04 UTC

#### ❌ KSI-CNA-07

**Control:** Cloud Native Architecture
**Reason:** ❌ Config service error: 
**Commands:** `1 commands (0 successful): aws config describe-config-rules --output json`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ⚠️ No usable output
**Commands Executed:** 1
**Validated:** 2025-06-06 08:10:04 UTC

---

### KSI-IAM: Identity and Access Management

#### ❌ KSI-IAM-01

**Control:** Identity and Access Management
**Reason:** ❌ Only virtual MFA found (1 devices) - phishing-resistant MFA required
**Commands:** `2 commands (2 successful): aws iam list-users --output json; aws iam list-mfa-devices --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | 👤 3 IAM users found | 🔐 1 MFA devices detected
**Commands Executed:** 2
**Validated:** 2025-06-06 08:10:04 UTC

#### ❌ KSI-IAM-02

**Control:** Identity and Access Management
**Reason:** ❌ Insufficient secure authentication: ❌ No password policy configured
**Commands:** `2 commands (1 successful): REDACTED_FOR_SECURITY; REDACTED_FOR_SECURITY`
**Evidence Analysis:** ⚠️ 1/2 commands failed execution | ⚠️ No usable output | ✅ Command output received
**Commands Executed:** 2
**Validated:** 2025-06-06 08:10:04 UTC

#### ❌ KSI-IAM-06

**Control:** Identity and Access Management
**Reason:** ❌ No automated response to suspicious activity: ❌ No CloudWatch alarms found for automated monitoring; ⚠️ 1 Lambda functions found but none security-focused
**Commands:** `2 commands (2 successful): aws cloudwatch describe-alarms --output json; aws lambda list-functions --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received
**Commands Executed:** 2
**Validated:** 2025-06-06 08:10:04 UTC

---

### KSI-INR: Incident Reporting

#### ❌ KSI-INR-02

**Control:** Incident Reporting
**Reason:** ❌ No comprehensive incident logging and analysis: ⚠️ No dedicated security log groups found (may use general logging); ❌ No manual incident tracking documentation found; ⚠️ No recent incident pattern analysis (should be periodic)
**Commands:** `2 commands (2 successful): aws logs describe-log-groups --log-group-name-prefix '/aws/security' --output json; evidence_check`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | 📄 Manual evidence validation
**Commands Executed:** 2
**Validated:** 2025-06-06 08:10:04 UTC

#### ❌ KSI-INR-03

**Control:** Incident Reporting
**Reason:** ❌ No comprehensive after action reporting and lessons learned integration found in evidence_v2/KSI-INR-03/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 08:10:04 UTC

---

### KSI-MLA: Monitoring, Logging, and Auditing

#### ❌ KSI-MLA-02

**Control:** Monitoring, Logging, and Auditing
**Reason:** ❌ No regular log review mechanisms: ❌ No CloudWatch alarms for automated log review; ⚠️ No metric filters found for log analysis
**Commands:** `2 commands (2 successful): aws cloudwatch describe-alarms --output json; aws logs describe-metric-filters --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received
**Commands Executed:** 2
**Validated:** 2025-06-06 08:10:04 UTC

#### ❌ KSI-MLA-04

**Control:** Monitoring, Logging, and Auditing
**Reason:** ❌ No authenticated vulnerability scanning: ❌ No Inspector coverage found for authenticated scanning; ℹ️ No EC2 instances found (acceptable for low-impact if using other services)
**Commands:** `2 commands (2 successful): aws inspector2 list-coverage --output json; aws ec2 describe-instances --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received
**Commands Executed:** 2
**Validated:** 2025-06-06 08:10:04 UTC

---

### KSI-PIY: Policy and Inventory

#### ❌ KSI-PIY-05

**Control:** Policy and Inventory
**Reason:** ❌ No evaluation methodology documentation found in evidence_v2/KSI-PIY-05/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 08:10:04 UTC

#### ❌ KSI-PIY-07

**Control:** Policy and Inventory
**Reason:** ❌ No supply chain risk management documentation found in evidence_v2/KSI-PIY-07/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 08:10:04 UTC

---

### KSI-RPL: Recovery Planning

#### ❌ KSI-RPL-01

**Control:** Recovery Planning
**Reason:** ❌ No RTO/RPO definitions found in evidence_v2/KSI-RPL-01/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 08:10:04 UTC

#### ❌ KSI-RPL-02

**Control:** Recovery Planning
**Reason:** ❌ No comprehensive recovery plan found in evidence_v2/KSI-RPL-02/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 08:10:04 UTC

#### ❌ KSI-RPL-04

**Control:** Recovery Planning
**Reason:** ❌ No regular recovery testing capability found in evidence_v2/KSI-RPL-04/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 08:10:04 UTC

---

### KSI-SVC: Service Configuration

#### ❌ KSI-SVC-06

**Control:** Service Configuration
**Reason:** ❌ No automated key management systems found: ℹ️ No ACM certificates found (acceptable for low-impact)
**Commands:** `2 commands (2 successful): REDACTED_FOR_SECURITY; aws acm list-certificates --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received
**Commands Executed:** 2
**Validated:** 2025-06-06 08:10:04 UTC

---

### KSI-TPR: Third-Party Information Resources

#### ❌ KSI-TPR-01

**Control:** Third-Party Information Resources
**Reason:** ❌ Third-party information resources not comprehensively identified: ❌ No cross-account role data for third-party integration analysis; ❌ No manual third-party inventory documentation found
**Commands:** `2 commands (1 successful): aws iam list-roles --query 'Roles[?contains(AssumeRolePolicyDocument, `sts:AssumeRole`)]' --output json; evidence_check`
**Evidence Analysis:** ⚠️ 1/2 commands failed execution | ⚠️ No usable output | 📄 Manual evidence validation
**Commands Executed:** 2
**Validated:** 2025-06-06 08:10:04 UTC

#### ❌ KSI-TPR-03

**Control:** Third-Party Information Resources
**Reason:** ❌ No supply chain risk assessment and mitigation found in evidence_v2/KSI-TPR-03/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 08:10:04 UTC

#### ❌ KSI-TPR-04

**Control:** Third-Party Information Resources
**Reason:** ❌ No comprehensive third-party vulnerability monitoring: ❌ No Inspector vulnerability monitoring data; ❌ No contractual vulnerability notification agreements found
**Commands:** `2 commands (1 successful): aws inspector2 list-findings --filter-criteria '{"component":[{"comparison":"EQUALS","value":"*"}]}' --max-results 20 --output json; evidence_check`
**Evidence Analysis:** ⚠️ 1/2 commands failed execution | ⚠️ No usable output | 📄 Manual evidence validation
**Commands Executed:** 2
**Validated:** 2025-06-06 08:10:04 UTC

---
## 🔧 Remediation Guidance

### Configuration Issues (10 KSIs)
- **Action:** Review and fix AWS service configurations
- **Priority:** Medium - Configuration changes needed
- **Affected KSIs:** KSI-CMT-03, KSI-IAM-06, KSI-IAM-01, KSI-MLA-02, KSI-TPR-04, KSI-INR-02, KSI-TPR-01, KSI-MLA-04, KSI-SVC-06, KSI-IAM-02

### Technical Issues (2 KSIs)
- **Action:** Check AWS CLI configuration, permissions, and service availability
- **Priority:** High - Technical resolution needed
- **Affected KSIs:** KSI-CNA-07, KSI-CNA-05

### Missing Documentation (8 KSIs)
- **Action:** Upload required evidence to appropriate `evidence_v2/KSI-*/` directories
- **Priority:** Medium - Manual evidence required
- **Affected KSIs:** KSI-RPL-01, KSI-PIY-05, KSI-RPL-04, KSI-INR-03, KSI-RPL-02, KSI-TPR-03, KSI-PIY-07, KSI-CMT-05
---

*Report generated on 2025-06-06 08:10:04 UTC*
*Source: unified_ksi_validations.json*
