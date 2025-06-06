# ❌ Failed KSI Validation Report

*Automated report generated from FedRAMP 20x validation pipeline*

## 📊 Executive Summary

- **Overall Pass Rate:** 45.1% (23/51)
- **Failed KSIs:** 28
- **Validation Method:** multi-command-v2
- **Last Updated:** 2025-06-06T05:52:21.613477Z

### Category Breakdown
- **KSI-CNA** (Cloud Native Architecture): 4/7 failed
- **KSI-CMT** (Change Management): 3/5 failed
- **KSI-IAM** (Identity and Access Management): 4/6 failed
- **KSI-SVC** (Service Configuration): 2/7 failed
- **KSI-MLA** (Monitoring, Logging, and Auditing): 3/6 failed
- **KSI-PIY** (Policy and Inventory): 3/7 failed
- **KSI-RPL** (Recovery Planning): 3/4 failed
- **KSI-TPR** (Third-Party Information Resources): 3/4 failed
- **KSI-INR** (Incident Reporting): 3/3 failed

---

## ❌ Failed KSI Details

### KSI-CMT: Change Management

#### ❌ KSI-CMT-01

**Control:** Change Management
**Reason:** ❌ Rule execution error: 'str' object has no attribute 'get'
**Commands:** `2 commands: aws cloudtrail describe-trails --output json; aws config describe-configuration-recorders --output json`
**Evidence Analysis:** ⚠️ 1/2 commands failed execution | 📊 1 CloudTrail configurations | ⚠️ No usable output
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-CMT-03

**Control:** Change Management
**Reason:** ❌ No automated testing and validation: ❌ No CodeBuild projects for automated testing; ❌ No CodePipelines for automated change validation
**Commands:** `2 commands (2 successful): aws codebuild list-projects --output json; aws codepipeline list-pipelines --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-CMT-05

**Control:** Change Management
**Reason:** ❌ No risk and impact evaluation documentation found in evidence_v2/KSI-CMT-05/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 05:52:21 UTC

---

### KSI-CNA: Cloud Native Architecture

#### ❌ KSI-CNA-02

**Control:** Cloud Native Architecture
**Reason:** ❌ Rule execution error: 'list' object has no attribute 'get'
**Commands:** `2 commands: aws ec2 describe-subnets --output json; aws ec2 describe-security-groups --query 'SecurityGroups[?GroupName!=`default`]' --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ⚠️ No usable output
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-CNA-05

**Control:** Cloud Native Architecture
**Reason:** ❌ Rule execution error: 'str' object has no attribute 'get'
**Commands:** `1 commands: aws shield describe-subscription --output json`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ⚠️ No usable output
**Commands Executed:** 1
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-CNA-06

**Control:** Cloud Native Architecture
**Reason:** ❌ Rule execution error: 'list' object has no attribute 'get'
**Commands:** `2 commands: aws ec2 describe-subnets --query 'Subnets[*].{SubnetId:SubnetId,AvailabilityZone:AvailabilityZone}' --output json; aws backup list-backup-plans --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | 📋 6 items retrieved | 💾 2 backup plans configured
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-CNA-07

**Control:** Cloud Native Architecture
**Reason:** ❌ Rule execution error: 'str' object has no attribute 'get'
**Commands:** `1 commands: aws config describe-config-rules --output json`
**Evidence Analysis:** ⚠️ 1/1 commands failed execution | ⚠️ No usable output
**Commands Executed:** 1
**Validated:** 2025-06-06 05:52:21 UTC

---

### KSI-IAM: Identity and Access Management

#### ❌ KSI-IAM-01

**Control:** Identity and Access Management
**Reason:** ❌ Only virtual MFA found (1 devices) - phishing-resistant MFA required
**Commands:** `2 commands (2 successful): aws iam list-users --output json; aws iam list-mfa-devices --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | 👤 3 IAM users found | 🔐 1 MFA devices detected
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-IAM-02

**Control:** Identity and Access Management
**Reason:** ❌ Insufficient secure authentication: ❌ No password policy configured
**Commands:** `2 commands (1 successful): REDACTED_FOR_SECURITY; REDACTED_FOR_SECURITY`
**Evidence Analysis:** ⚠️ 1/2 commands failed execution | ⚠️ No usable output | ✅ Command output received
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-IAM-03

**Control:** Identity and Access Management
**Reason:** ❌ Rule execution error: 'str' object has no attribute 'get'
**Commands:** `2 commands: aws iam list-roles --output json; aws iam list-service-linked-roles --output json`
**Evidence Analysis:** ⚠️ 1/2 commands failed execution | ✅ Command output received | ⚠️ No usable output
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-IAM-06

**Control:** Identity and Access Management
**Reason:** ❌ No automated response to suspicious activity: ❌ No CloudWatch alarms found for automated monitoring; ⚠️ 1 Lambda functions found but none security-focused
**Commands:** `2 commands (2 successful): aws cloudwatch describe-alarms --output json; aws lambda list-functions --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

---

### KSI-INR: Incident Reporting

#### ❌ KSI-INR-01

**Control:** Incident Reporting
**Reason:** ❌ No comprehensive incident reporting procedures found in evidence_v2/KSI-INR-01/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-INR-02

**Control:** Incident Reporting
**Reason:** ❌ No comprehensive incident logging and analysis: ⚠️ No dedicated security log groups found (may use general logging); ❌ No manual incident tracking documentation found; ⚠️ No recent incident pattern analysis (should be periodic)
**Commands:** `2 commands (2 successful): aws logs describe-log-groups --log-group-name-prefix '/aws/security' --output json; evidence_check`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | 📄 Manual evidence validation
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-INR-03

**Control:** Incident Reporting
**Reason:** ❌ No comprehensive after action reporting and lessons learned integration found in evidence_v2/KSI-INR-03/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 05:52:21 UTC

---

### KSI-MLA: Monitoring, Logging, and Auditing

#### ❌ KSI-MLA-02

**Control:** Monitoring, Logging, and Auditing
**Reason:** ❌ No regular log review mechanisms: ❌ No CloudWatch alarms for automated log review; ⚠️ No metric filters found for log analysis
**Commands:** `2 commands (2 successful): aws cloudwatch describe-alarms --output json; aws logs describe-metric-filters --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-MLA-04

**Control:** Monitoring, Logging, and Auditing
**Reason:** ❌ No authenticated vulnerability scanning: ❌ No Inspector coverage found for authenticated scanning; ℹ️ No EC2 instances found (acceptable for low-impact if using other services)
**Commands:** `2 commands (2 successful): aws inspector2 list-coverage --output json; aws ec2 describe-instances --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-MLA-05

**Control:** Monitoring, Logging, and Auditing
**Reason:** ❌ Rule execution error: 'str' object has no attribute 'get'
**Commands:** `2 commands: aws config describe-config-rules --output json; aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`
**Evidence Analysis:** ⚠️ 1/2 commands failed execution | ⚠️ No usable output | 🏗️ 2 CloudFormation stacks
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

---

### KSI-PIY: Policy and Inventory

#### ❌ KSI-PIY-02

**Control:** Policy and Inventory
**Reason:** ❌ No security policies found in evidence_v2/KSI-PIY-02/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-PIY-05

**Control:** Policy and Inventory
**Reason:** ❌ No evaluation methodology documentation found in evidence_v2/KSI-PIY-05/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-PIY-07

**Control:** Policy and Inventory
**Reason:** ❌ No supply chain risk management documentation found in evidence_v2/KSI-PIY-07/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 05:52:21 UTC

---

### KSI-RPL: Recovery Planning

#### ❌ KSI-RPL-01

**Control:** Recovery Planning
**Reason:** ❌ No RTO/RPO definitions found in evidence_v2/KSI-RPL-01/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-RPL-02

**Control:** Recovery Planning
**Reason:** ❌ No comprehensive recovery plan found in evidence_v2/KSI-RPL-02/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-RPL-04

**Control:** Recovery Planning
**Reason:** ❌ No regular recovery testing capability found in evidence_v2/KSI-RPL-04/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 05:52:21 UTC

---

### KSI-SVC: Service Configuration

#### ❌ KSI-SVC-04

**Control:** Service Configuration
**Reason:** ❌ Rule execution error: 'str' object has no attribute 'get'
**Commands:** `2 commands: aws ssm describe-parameters --output json; aws config describe-configuration-recorders --output json`
**Evidence Analysis:** ⚠️ 1/2 commands failed execution | ✅ Command output received | ⚠️ No usable output
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-SVC-06

**Control:** Service Configuration
**Reason:** ❌ No automated key management systems found: ℹ️ No ACM certificates found (acceptable for low-impact)
**Commands:** `2 commands (2 successful): REDACTED_FOR_SECURITY; aws acm list-certificates --output json`
**Evidence Analysis:** ✅ All 2 commands executed successfully | ✅ Command output received | ✅ Command output received
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

---

### KSI-TPR: Third-Party Information Resources

#### ❌ KSI-TPR-01

**Control:** Third-Party Information Resources
**Reason:** ❌ Rule execution error: 'str' object has no attribute 'get'
**Commands:** `2 commands: aws iam list-roles --query 'Roles[?contains(AssumeRolePolicyDocument, `sts:AssumeRole`)]' --output json; evidence_check`
**Evidence Analysis:** ⚠️ 1/2 commands failed execution | ⚠️ No usable output | 📄 Manual evidence validation
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-TPR-03

**Control:** Third-Party Information Resources
**Reason:** ❌ No supply chain risk assessment and mitigation found in evidence_v2/KSI-TPR-03/
**Commands:** `1 commands (1 successful): evidence_check`
**Evidence Analysis:** ✅ All 1 commands executed successfully | 📄 Manual evidence validation
**Commands Executed:** 1
**Validated:** 2025-06-06 05:52:21 UTC

#### ❌ KSI-TPR-04

**Control:** Third-Party Information Resources
**Reason:** ❌ Rule execution error: 'str' object has no attribute 'get'
**Commands:** `2 commands: aws inspector2 list-findings --filter-criteria '{"component":[{"comparison":"EQUALS","value":"*"}]}' --max-results 20 --output json; evidence_check`
**Evidence Analysis:** ⚠️ 1/2 commands failed execution | ⚠️ No usable output | 📄 Manual evidence validation
**Commands Executed:** 2
**Validated:** 2025-06-06 05:52:21 UTC

---
## 🔧 Remediation Guidance

### Technical Issues (10 KSIs)
- **Action:** Check AWS CLI configuration, permissions, and service availability
- **Priority:** High - Technical resolution needed
- **Affected KSIs:** KSI-CNA-02, KSI-CMT-01, KSI-CNA-07, KSI-TPR-04, KSI-CNA-05, KSI-SVC-04, KSI-CNA-06, KSI-TPR-01, KSI-MLA-05, KSI-IAM-03

### Configuration Issues (8 KSIs)
- **Action:** Review and fix AWS service configurations
- **Priority:** Medium - Configuration changes needed
- **Affected KSIs:** KSI-CMT-03, KSI-IAM-06, KSI-IAM-01, KSI-MLA-02, KSI-INR-02, KSI-MLA-04, KSI-SVC-06, KSI-IAM-02

### Missing Documentation (10 KSIs)
- **Action:** Upload required evidence to appropriate `evidence_v2/KSI-*/` directories
- **Priority:** Medium - Manual evidence required
- **Affected KSIs:** KSI-RPL-01, KSI-PIY-05, KSI-RPL-04, KSI-INR-03, KSI-PIY-02, KSI-RPL-02, KSI-TPR-03, KSI-PIY-07, KSI-INR-01, KSI-CMT-05
---

*Report generated on 2025-06-06 05:52:21 UTC*
*Source: unified_ksi_validations.json*
