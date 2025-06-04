# ❌ Failed KSI Validation Report

**Generated:** 2025-06-04T15:58:32.224143Z
**Total Failures:** 46

---

## ❌ KSI-CNA-02: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-02`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No subnets found — cannot evaluate segmentation  
- **CLI Command:** `aws ec2 describe-subnets`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.162153  

---

## ❌ KSI-CMT-03: Change Management

- **Validation ID:** `KSI-CMT-03`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No check build presence (Items) found  
- **CLI Command:** `aws codebuild list-projects`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.162231  

---

## ❌ KSI-SVC-07: Service Configuration

- **Validation ID:** `KSI-SVC-07`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `aws ssm describe-patch-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.162371  

---

## ❌ KSI-CNA-01: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-01`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No security groups returned  
- **CLI Command:** `aws ec2 describe-security-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.162431  

---

## ❌ KSI-IAM-01: Identity and Access Management

- **Validation ID:** `KSI-IAM-01`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No users found in AWS SSO Identity Center  
- **CLI Command:** `aws identitystore list-users --identity-store-id <ID_STORE_ID> --query 'Users[*].UserId'`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.162488  

---

## ❌ KSI-CED-01: Cybersecurity Education

- **Validation ID:** `KSI-CED-01`  
- **KSI Family:** Cybersecurity Education  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `aws iam list-users`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.162553  

---

## ❌ KSI-CMT-01: Change Management

- **Validation ID:** `KSI-CMT-01`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No CloudTrail trails found — cannot verify config change monitoring  
- **CLI Command:** `aws cloudtrail describe-trails`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.162626  

---

## ❌ KSI-MLA-02: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-02`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No CloudTrail trails found  
- **CLI Command:** `aws cloudtrail describe-trails`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.162723  

---

## ❌ KSI-PIY-03: Policy and Inventory

- **Validation ID:** `KSI-PIY-03`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `aws iam list-policies`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.162787  

---

## ❌ KSI-SVC-01: Service Configuration

- **Validation ID:** `KSI-SVC-01`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ Unexpected structure or missing InstanceInformationList in output.  
- **CLI Command:** `aws ssm describe-instance-information --max-results 50`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.162839  

---

## ❌ KSI-CNA-07: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-07`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `aws ec2 describe-instances --query Reservations[*].Instances[*].ImageId`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.162889  

---

## ❌ KSI-PIY-06: Policy and Inventory

- **Validation ID:** `KSI-PIY-06`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No IAM user policies found (AttachedPolicies is empty)  
- **CLI Command:** `aws iam list-attached-user-policies`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.162939  

---

## ❌ KSI-RPL-01: Recovery Planning

- **Validation ID:** `KSI-RPL-01`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No backup plans found (BackupPlansList empty)  
- **CLI Command:** `aws backup list-backup-plans`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163008  

---

## ❌ KSI-CMT-04: Change Management

- **Validation ID:** `KSI-CMT-04`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `aws codebuild list-projects`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163059  

---

## ❌ KSI-MLA-06: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-06`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No Security Hub findings found (Findings list empty)  
- **CLI Command:** `aws securityhub get-findings --max-results 25`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163125  

---

## ❌ KSI-TPR-04: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-04`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `aws securityhub get-findings --max-results 25`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163174  

---

## ❌ KSI-INR-02: Incident Reporting

- **Validation ID:** `KSI-INR-02`  
- **KSI Family:** Incident Reporting  
- **Assertion Reason:** ❌ No Security Hub findings related to past incidents found (empty Findings list)  
- **CLI Command:** `aws securityhub get-findings --max-results 25`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163225  

---

## ❌ KSI-PIY-05: Policy and Inventory

- **Validation ID:** `KSI-PIY-05`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No AWS Config rules found (ConfigRules list empty)  
- **CLI Command:** `aws config describe-compliance-by-config-rule --max-results 25`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163277  

---

## ❌ KSI-RPL-04: Recovery Planning

- **Validation ID:** `KSI-RPL-04`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No backup jobs found (BackupJobs list empty)  
- **CLI Command:** `aws backup list-backup-jobs`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163324  

---

## ❌ KSI-PIY-02: Policy and Inventory

- **Validation ID:** `KSI-PIY-02`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No IAM policies found (Policies list empty)  
- **CLI Command:** `aws iam list-policies --max-results 5`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163415  

---

## ❌ KSI-CNA-05: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-05`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No WAFv2 WebACLs found (WebACLs list empty)  
- **CLI Command:** `aws wafv2 list-web-acls --scope REGIONAL`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163459  

---

## ❌ KSI-MLA-03: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-03`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No Inspector2 findings found (Findings list empty)  
- **CLI Command:** `aws inspector2 list-findings --filter vulnerabilitySource=CVE --max-results 25`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163503  

---

## ❌ KSI-SVC-04: Service Configuration

- **Validation ID:** `KSI-SVC-04`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No SSM associations found (Associations list empty)  
- **CLI Command:** `aws ssm list-associations`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163546  

---

## ❌ KSI-CNA-06: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-06`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No check ha routing (RouteTables) found  
- **CLI Command:** `aws ec2 describe-route-tables`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163595  

---

## ❌ KSI-PIY-04: Policy and Inventory

- **Validation ID:** `KSI-PIY-04`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `aws cloudformation list-stack-sets --status ACTIVE`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163722  

---

## ❌ KSI-CNA-04: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-04`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `aws ec2 describe-instances`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163785  

---

## ❌ KSI-CED-02: Cybersecurity Education

- **Validation ID:** `KSI-CED-02`  
- **KSI Family:** Cybersecurity Education  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `aws iam list-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163833  

---

## ❌ KSI-CMT-02: Change Management

- **Validation ID:** `KSI-CMT-02`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No active StackSets found — cannot confirm redeployment model for infrastructure changes  
- **CLI Command:** `aws cloudformation list-stack-sets --status ACTIVE`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163936  

---

## ❌ KSI-SVC-03: Service Configuration

- **Validation ID:** `KSI-SVC-03`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No KMS keys found — unable to confirm encryption infrastructure readiness  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.163995  

---

## ❌ KSI-SVC-05: Service Configuration

- **Validation ID:** `KSI-SVC-05`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No AMIs found — unable to confirm cryptographic enforcement of system image integrity  
- **CLI Command:** `aws ec2 describe-images`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164090  

---

## ❌ KSI-RPL-02: Recovery Planning

- **Validation ID:** `KSI-RPL-02`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No backup plans found — unable to confirm backup targets  
- **CLI Command:** `aws backup list-backup-plans`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164143  

---

## ❌ KSI-MLA-05: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-05`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No AWS Config rules found — cannot confirm IaC evaluation  
- **CLI Command:** `aws config describe-config-rules`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164193  

---

## ❌ KSI-MLA-04: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-04`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No managed instances found — SSM not in use  
- **CLI Command:** `aws ssm list-managed-instances`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164242  

---

## ❌ KSI-IAM-04: Identity and Access Management

- **Validation ID:** `KSI-IAM-04`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM principals or policies found — cannot confirm least-privileged access model  
- **CLI Command:** `aws iam get-account-authorization-details --query '{GroupCount: length(Groups) RoleCount: length(RoleDetailList)}'`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164287  

---

## ❌ KSI-SVC-06: Service Configuration

- **Validation ID:** `KSI-SVC-06`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No KMS keys found — cannot confirm key lifecycle management  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164337  

---

## ❌ KSI-TPR-03: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-03`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No Inspector2 scan coverage found — supply chain risk monitoring not in place  
- **CLI Command:** `aws inspector2 list-coverage`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164382  

---

## ❌ KSI-SVC-02: Service Configuration

- **Validation ID:** `KSI-SVC-02`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No load balancers found — unable to confirm network encryption enforcement  
- **CLI Command:** `aws elbv2 describe-load-balancers`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164431  

---

## ❌ KSI-IAM-05: Identity and Access Management

- **Validation ID:** `KSI-IAM-05`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM summary map found — unable to assess zero trust posture  
- **CLI Command:** `aws iam get-account-summary`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164490  

---

## ❌ KSI-PIY-07: Policy and Inventory

- **Validation ID:** `KSI-PIY-07`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164541  

---

## ❌ KSI-INR-01: Incident Reporting

- **Validation ID:** `KSI-INR-01`  
- **KSI Family:** Incident Reporting  
- **Assertion Reason:** ❌ No SecurityHub findings found — incident reporting may not be active  
- **CLI Command:** `aws securityhub get-findings --max-results 25`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164587  

---

## ❌ KSI-CNA-03: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-03`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No route tables found to evaluate  
- **CLI Command:** `aws ec2 describe-route-tables`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164637  

---

## ❌ KSI-IAM-02: Identity and Access Management

- **Validation ID:** `KSI-IAM-02`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No check auth models (Users) found  
- **CLI Command:** `aws iam list-users`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164689  

---

## ❌ KSI-CMT-05: Change Management

- **Validation ID:** `KSI-CMT-05`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `aws ssm describe-document`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164783  

---

## ❌ KSI-RPL-03: Recovery Planning

- **Validation ID:** `KSI-RPL-03`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No backup plans found — unable to verify recovery posture definition  
- **CLI Command:** `aws backup list-backup-plans`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164841  

---

## ❌ KSI-IAM-03: Identity and Access Management

- **Validation ID:** `KSI-IAM-03`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM roles found — cannot verify role granularity for service accounts  
- **CLI Command:** `aws iam list-roles --max-items 25`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164886  

---

## ❌ KSI-MLA-01: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-01`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No CloudWatch log groups found — SIEM visibility not verifiable  
- **CLI Command:** `aws logs describe-log-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-04T15:58:32.164937  

---

