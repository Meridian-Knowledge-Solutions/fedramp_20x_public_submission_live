# ❌ Failed KSI Validation Report

*Automated report generated from FedRAMP 20x validation pipeline*

## 📊 Executive Summary

- **Overall Pass Rate:** 32.7% (17/52)
- **Failed KSIs:** 35
- **Validation Method:** multi-command-v2
- **Last Updated:** 2025-06-06T03:51:14.713011Z

### Category Breakdown
- **KSI-CNA** (Cloud Native Architecture): 5/7 failed
- **KSI-CMT** (Change Management): 3/5 failed
- **KSI-IAM** (Identity and Access Management): 5/6 failed
- **KSI-SVC** (Service Configuration): 5/7 failed
- **KSI-CED** (Cybersecurity Education): 1/2 failed
- **KSI-MLA** (Monitoring, Logging, and Auditing): 4/6 failed
- **KSI-PIY** (Policy and Inventory): 2/7 failed
- **KSI-RPL** (Recovery Planning): 4/4 failed
- **terraform** (Unknown category): 1/1 failed
- **KSI-TPR** (Third-Party Information Resources): 3/4 failed
- **KSI-INR** (Incident Reporting): 2/3 failed

---

## ❌ Failed KSI Details

### KSI-CED: Cybersecurity Education

#### ❌ KSI-CED-01

**Control:** Cybersecurity Education
**Reason:** ❌ No IAM users or static training evidence found
**Commands:** `1 commands (0 successful): aws iam list-users`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | 👤 3 IAM users found
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

---

### KSI-CMT: Change Management

#### ❌ KSI-CMT-01

**Control:** Change Management
**Reason:** ❌ No CloudTrail trails found — cannot verify config change monitoring
**Commands:** `1 commands (0 successful): aws cloudtrail describe-trails`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | 📊 1 CloudTrail configurations
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-CMT-02

**Control:** Change Management
**Reason:** ❌ No active StackSets found — cannot confirm redeployment model for infrastructure changes
**Commands:** `1 commands (0 successful): aws cloudformation list-stack-sets --status ACTIVE`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ✅ Command output received
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-CMT-03

**Control:** Change Management
**Reason:** ❌ No check build presence (Items) found
**Commands:** `1 commands (0 successful): aws codebuild list-projects`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ✅ Command output received
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

---

### KSI-CNA: Cloud Native Architecture

#### ❌ KSI-CNA-01

**Control:** Cloud Native Architecture
**Reason:** ❌ No security groups returned
**Commands:** `1 commands (0 successful): aws ec2 describe-security-groups`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | 🛡️ 1 security groups analyzed
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-CNA-02

**Control:** Cloud Native Architecture
**Reason:** ❌ No subnets found — cannot evaluate segmentation
**Commands:** `1 commands (0 successful): aws ec2 describe-subnets`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ✅ Command output received
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-CNA-03

**Control:** Cloud Native Architecture
**Reason:** ❌ No route tables found to evaluate
**Commands:** `1 commands (0 successful): aws ec2 describe-route-tables`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ✅ Command output received
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-CNA-05

**Control:** Cloud Native Architecture
**Reason:** ❌ No WAFv2 WebACLs found (WebACLs list empty)
**Commands:** `1 commands (0 successful): aws wafv2 list-web-acls --scope CLOUDFRONT --region us-east-1`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ✅ Command output received
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-CNA-06

**Control:** Cloud Native Architecture
**Reason:** ❌ No route tables found for HA routing
**Commands:** `1 commands (0 successful): aws ec2 describe-route-tables`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ✅ Command output received
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

---

### KSI-IAM: Identity and Access Management

#### ❌ KSI-IAM-02

**Control:** Identity and Access Management
**Reason:** ❌ No users found — identity model appears empty
**Commands:** `4 commands (3 successful): REDACTED_FOR_SECURITY; aws iam list-mfa-devices --output json (+2 more)`
**Evidence Analysis:** ⚠️ 1/4 commands failed execution | 📋 3 items retrieved | 🔐 1 MFA devices detected | ⚠️ No usable output
**Commands Executed:** 4
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-IAM-03

**Control:** Identity and Access Management
**Reason:** ❌ No IAM roles found — cannot verify role granularity for service accounts
**Commands:** `4 commands (3 successful): aws iam list-roles --output json; aws iam list-instance-profiles --output json (+2 more)`
**Evidence Analysis:** ⚠️ 1/4 commands failed execution | ✅ Command output received | ✅ Command output received | ✅ Command output received
**Commands Executed:** 4
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-IAM-04

**Control:** Identity and Access Management
**Reason:** ❌ No IAM principals or policies found — cannot confirm least-privileged access model
**Commands:** `5 commands (4 successful): aws iam list-roles --output json; aws iam list-policies --scope Local --output json (+3 more)`
**Evidence Analysis:** ⚠️ 1/5 commands failed execution | ✅ Command output received | ✅ Command output received | ⚠️ No usable output
**Commands Executed:** 5
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-IAM-05

**Control:** Identity and Access Management
**Reason:** ❌ No IAM summary map found — unable to assess zero trust posture
**Commands:** `5 commands (4 successful): aws iam list-policies --scope AWS --query 'Policies[?contains(PolicyName, `Condition`)]' --output json; aws logs describe-log-groups --log-group-name-prefix '/aws/cloudtr...`
**Evidence Analysis:** ⚠️ 1/5 commands failed execution | ⚠️ No usable output | ✅ Command output received | ⚠️ No usable output
**Commands Executed:** 5
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-IAM-06

**Control:** Identity and Access Management
**Reason:** ❌ No IAM roles found — cannot evaluate privileged disablement readiness
**Commands:** `5 commands (5 successful): aws iam list-users --query 'Users[?contains(UserName, `admin`) || contains(UserName, `root`)]' --output json; aws logs describe-log-groups --log-group-name-prefix '/aws/l...`
**Evidence Analysis:** ✅ All 5 commands executed successfully | ⚠️ No usable output | ✅ Command output received | ✅ Command output received
**Commands Executed:** 5
**Validated:** 2025-06-06 03:51:14 UTC

---

### KSI-INR: Incident Reporting

#### ❌ KSI-INR-01

**Control:** Incident Reporting
**Reason:** ❌ No SecurityHub findings found — incident reporting may not be active
**Commands:** `1 commands (0 successful): aws securityhub get-findings --max-results 1`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | 🔍 1 security findings
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-INR-02

**Control:** Incident Reporting
**Reason:** ❌ No Security Hub findings related to past incidents found (empty Findings list)
**Commands:** `1 commands (0 successful): aws securityhub get-findings --max-results 1`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | 🔍 1 security findings
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

---

### KSI-MLA: Monitoring, Logging, and Auditing

#### ❌ KSI-MLA-01

**Control:** Monitoring, Logging, and Auditing
**Reason:** ❌ No CloudWatch log groups found — SIEM visibility not verifiable
**Commands:** `5 commands (3 successful): aws cloudtrail describe-trails --output json; aws logs describe-log-groups --output json (+3 more)`
**Evidence Analysis:** ⚠️ 2/5 commands failed execution | 📊 1 CloudTrail configurations | ✅ Command output received | ⚠️ No usable output
**Commands Executed:** 5
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-MLA-02

**Control:** Monitoring, Logging, and Auditing
**Reason:** ❌ No CloudTrail trails found
**Commands:** `5 commands (5 successful): aws cloudwatch describe-alarms --output json; aws logs describe-metric-filters --output json (+3 more)`
**Evidence Analysis:** ✅ All 5 commands executed successfully | ✅ Command output received | ✅ Command output received | ✅ Command output received
**Commands Executed:** 5
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-MLA-05

**Control:** Monitoring, Logging, and Auditing
**Reason:** ❌ No AWS Config rules found — cannot confirm IaC evaluation
**Commands:** `5 commands (3 successful): aws config describe-config-rules --output json; aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json (+3 more)`
**Evidence Analysis:** ⚠️ 2/5 commands failed execution | ⚠️ No usable output | 🏗️ 2 CloudFormation stacks | ⚠️ No usable output
**Commands Executed:** 5
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-MLA-06

**Control:** Monitoring, Logging, and Auditing
**Reason:** ❌ No Security Hub findings found
**Commands:** `5 commands (3 successful): aws securityhub get-findings --query 'Findings[?Compliance.Status==`FAILED`]' --output json; aws ssm describe-patch-group-state --patch-group production --output json (+3...`
**Evidence Analysis:** ⚠️ 2/5 commands failed execution | 📋 118 items retrieved | ✅ Command output received | ⚠️ No usable output
**Commands Executed:** 5
**Validated:** 2025-06-06 03:51:14 UTC

---

### KSI-PIY: Policy and Inventory

#### ❌ KSI-PIY-02

**Control:** Policy and Inventory
**Reason:** ❌ No IAM policies found (Policies list empty)
**Commands:** `1 commands (0 successful): aws iam list-policies --max-items 5`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ✅ Command output received
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-PIY-05

**Control:** Policy and Inventory
**Reason:** ❌ No AWS Config rules found (ConfigRules list empty)
**Commands:** `1 commands (0 successful): aws configservice describe-config-rules --max-results 1`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ❌ 
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

---

### KSI-RPL: Recovery Planning

#### ❌ KSI-RPL-01

**Control:** Recovery Planning
**Reason:** ❌ No backup plans found (BackupPlansList empty)
**Commands:** `1 commands (0 successful): aws backup list-backup-plans`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | 💾 2 backup plans configured
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-RPL-02

**Control:** Recovery Planning
**Reason:** ❌ No backup plans found — unable to confirm backup targets
**Commands:** `1 commands (0 successful): aws backup list-backup-plans`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | 💾 2 backup plans configured
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-RPL-03

**Control:** Recovery Planning
**Reason:** ❌ No backup plans found — unable to verify recovery posture definition
**Commands:** `1 commands (0 successful): aws backup list-backup-plans`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | 💾 2 backup plans configured
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-RPL-04

**Control:** Recovery Planning
**Reason:** ❌ No backup jobs found (BackupJobs list empty)
**Commands:** `1 commands (0 successful): aws backup list-backup-jobs`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ❌ Output too large or not JSON serializable
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

---

### KSI-SVC: Service Configuration

#### ❌ KSI-SVC-01

**Control:** Service Configuration
**Reason:** ❌ Unexpected structure or missing InstanceInformationList in output.
**Commands:** `1 commands (0 successful): aws ssm describe-instance-information --max-results 5`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ✅ Command output received
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-SVC-02

**Control:** Service Configuration
**Reason:** ❌ No load balancers found — unable to confirm network encryption enforcement
**Commands:** `1 commands (0 successful): aws elbv2 describe-load-balancers`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ✅ Command output received
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-SVC-03

**Control:** Service Configuration
**Reason:** ❌ No KMS keys found — unable to confirm encryption infrastructure readiness
**Commands:** `1 commands (0 successful): REDACTED_FOR_SECURITY`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ✅ Command output received
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-SVC-05

**Control:** Service Configuration
**Reason:** ❌ No AMIs found — unable to confirm cryptographic enforcement of system image integrity
**Commands:** `1 commands (0 successful): aws ec2 describe-images`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ❌ Output too large or not JSON serializable
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-SVC-06

**Control:** Service Configuration
**Reason:** ❌ No KMS keys found — cannot confirm key lifecycle management
**Commands:** `1 commands (0 successful): REDACTED_FOR_SECURITY`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ✅ Command output received
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

---

### KSI-TPR: Third-Party Information Resources

#### ❌ KSI-TPR-01

**Control:** Third-Party Information Resources
**Reason:** ❌ No active Access Analyzers found — unable to evaluate third-party access risk
**Commands:** `1 commands (0 successful): REDACTED_FOR_SECURITY`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ✅ Command output received
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-TPR-03

**Control:** Third-Party Information Resources
**Reason:** ❌ No Inspector2 scan coverage or fallback member evidence found
**Commands:** `1 commands (0 successful): aws inspector2 list-members`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ✅ Command output received
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

#### ❌ KSI-TPR-04

**Control:** Third-Party Information Resources
**Reason:** ❌ No upstream alerting findings and no static attestation found.
**Commands:** `1 commands (0 successful): aws securityhub get-findings --max-results 1`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | 🔍 1 security findings
**Commands Executed:** 1
**Validated:** 2025-06-06 03:51:14 UTC

---

### terraform: Unknown category

#### ❌ terraform

**Control:** Unknown category
**Reason:** ❌ No cli_output.json file found
**Evidence Analysis:** ❌ No CLI output file found
**Commands Executed:** 0
**Validated:** 2025-06-06 03:51:14 UTC

---
## 🔧 Remediation Guidance

### Configuration Issues (35 KSIs)
- **Action:** Review and fix AWS service configurations
- **Priority:** Medium - Configuration changes needed
- **Affected KSIs:** KSI-CNA-02, KSI-CMT-03, KSI-IAM-06, KSI-CNA-01, KSI-CED-01, KSI-CMT-01, KSI-MLA-02, KSI-SVC-01, KSI-RPL-01, terraform, KSI-MLA-06, KSI-TPR-04, KSI-INR-02, KSI-PIY-05, KSI-RPL-04, KSI-PIY-02, KSI-CNA-05, KSI-CNA-06, KSI-TPR-01, KSI-CMT-02, KSI-SVC-03, KSI-SVC-05, KSI-RPL-02, KSI-MLA-05, KSI-IAM-04, KSI-SVC-06, KSI-TPR-03, KSI-SVC-02, KSI-IAM-05, KSI-INR-01, KSI-CNA-03, KSI-IAM-02, KSI-RPL-03, KSI-IAM-03, KSI-MLA-01
---

*Report generated on 2025-06-06 03:51:14 UTC*
*Source: unified_ksi_validations.json*
