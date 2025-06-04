# ❌ Failed KSI Validation Report

**Generated:** 2025-06-04T02:27:49.210010Z
**Total Failures:** 28

---

## ❌ KSI-CMT-03: Change Management

- **Validation ID:** `KSI-CMT-03`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No check build presence (Items) found  
- **CLI Command:** `aws codebuild list-projects`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.164411  

---

## ❌ KSI-SVC-07: Service Configuration

- **Validation ID:** `KSI-SVC-07`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No patch groups defined (Mappings is empty)  
- **CLI Command:** `aws ssm describe-patch-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.164530  

---

## ❌ KSI-IAM-01: Identity and Access Management

- **Validation ID:** `KSI-IAM-01`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No users found in AWS SSO Identity Center  
- **CLI Command:** `aws identitystore list-users --identity-store-id <ID_STORE_ID>`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.164646  

---

## ❌ KSI-CMT-01: Change Management

- **Validation ID:** `KSI-CMT-01`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No check config mgmt (Items) found  
- **CLI Command:** `aws config describe-configuration-recorders`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.164771  

---

## ❌ KSI-PIY-03: Policy and Inventory

- **Validation ID:** `KSI-PIY-03`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `aws iam list-policies`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.164886  

---

## ❌ KSI-SVC-01: Service Configuration

- **Validation ID:** `KSI-SVC-01`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ SSM agent present but managing 0 instances. Cannot enforce configuration baselines.  
- **CLI Command:** `aws ssm describe-instance-information --max-results 50`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.164933  

---

## ❌ KSI-CNA-07: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-07`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No official AMIs found (Images list empty)  
- **CLI Command:** `aws ec2 describe-images --owners self`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.164980  

---

## ❌ KSI-CMT-04: Change Management

- **Validation ID:** `KSI-CMT-04`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No check ci testing (Items) found  
- **CLI Command:** `aws codebuild list-projects`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.165139  

---

## ❌ KSI-PIY-05: Policy and Inventory

- **Validation ID:** `KSI-PIY-05`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No AWS Config rules found (ConfigRules list empty)  
- **CLI Command:** `aws config describe-config-rules`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.165337  

---

## ❌ KSI-INR-03: Incident Reporting

- **Validation ID:** `KSI-INR-03`  
- **KSI Family:** Incident Reporting  
- **Assertion Reason:** ❌ No critical incident findings returned from Security Hub  
- **CLI Command:** `aws securityhub get-findings --filters SeverityLabel=CRITICAL --max-results 20`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.165484  

---

## ❌ KSI-CNA-05: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-05`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No WAFv2 WebACLs found (WebACLs list empty)  
- **CLI Command:** `aws wafv2 list-web-acls --scope REGIONAL`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.165572  

---

## ❌ KSI-MLA-03: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-03`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No Inspector2 findings found (Findings list empty)  
- **CLI Command:** `aws inspector2 list-findings --filter vulnerabilitySource=CVE --max-results 25`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.165618  

---

## ❌ KSI-SVC-04: Service Configuration

- **Validation ID:** `KSI-SVC-04`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No SSM associations found (Associations list empty)  
- **CLI Command:** `aws ssm list-associations`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.165660  

---

## ❌ KSI-CNA-04: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-04`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `aws ec2 describe-instances`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.165857  

---

## ❌ KSI-CED-02: Cybersecurity Education

- **Validation ID:** `KSI-CED-02`  
- **KSI Family:** Cybersecurity Education  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `aws iam list-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.165902  

---

## ❌ KSI-TPR-01: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-01`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ IAM role scan failed: Output too large or not JSON serializable  
- **CLI Command:** `aws iam list-roles`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.165946  

---

## ❌ KSI-MLA-05: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-05`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No AWS Config rules found — cannot confirm IaC evaluation  
- **CLI Command:** `aws config describe-config-rules`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.166235  

---

## ❌ KSI-MLA-04: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-04`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No managed instances found — SSM not in use  
- **CLI Command:** `aws ssm list-managed-instances`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.166281  

---

## ❌ KSI-IAM-04: Identity and Access Management

- **Validation ID:** `KSI-IAM-04`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ IAM policy query failed: Output too large or not JSON serializable  
- **CLI Command:** `aws iam get-account-authorization-details`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.166324  

---

## ❌ KSI-TPR-03: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-03`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No Inspector2 scan coverage found — supply chain risk monitoring not in place  
- **CLI Command:** `aws inspector2 list-coverage`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.166442  

---

## ❌ KSI-SVC-02: Service Configuration

- **Validation ID:** `KSI-SVC-02`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No load balancers found — unable to confirm network encryption enforcement  
- **CLI Command:** `aws elbv2 describe-load-balancers`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.166489  

---

## ❌ KSI-IAM-05: Identity and Access Management

- **Validation ID:** `KSI-IAM-05`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM summary map found — unable to assess zero trust posture  
- **CLI Command:** `aws iam get-account-summary`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.166548  

---

## ❌ KSI-PIY-07: Policy and Inventory

- **Validation ID:** `KSI-PIY-07`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No review supply chain decision (Items) found  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.166597  

---

## ❌ KSI-INR-01: Incident Reporting

- **Validation ID:** `KSI-INR-01`  
- **KSI Family:** Incident Reporting  
- **Assertion Reason:** ❌ No check reporting (Items) found  
- **CLI Command:** `aws securityhub get-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.166640  

---

## ❌ KSI-CMT-05: Change Management

- **Validation ID:** `KSI-CMT-05`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No check sops (Items) found  
- **CLI Command:** `aws ssm describe-document`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.166784  

---

## ❌ KSI-RPL-03: Recovery Planning

- **Validation ID:** `KSI-RPL-03`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No verify restore points (Items) found  
- **CLI Command:** `aws backup list-recovery-points-by-backup-vault`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.166826  

---

## ❌ KSI-IAM-03: Identity and Access Management

- **Validation ID:** `KSI-IAM-03`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No check role granularity (Items) found  
- **CLI Command:** `aws iam list-roles`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.166866  

---

## ❌ KSI-MLA-01: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-01`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No siem visibility (Items) found  
- **CLI Command:** `aws logs describe-log-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T02:27:49.166913  

---

