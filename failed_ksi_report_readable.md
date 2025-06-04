# ❌ Failed KSI Validation Report

**Generated:** 2025-06-04T23:52:47.618580Z
**Total Failures:** 32

---

## ❌ KSI-CMT-03: Change Management

- **Validation ID:** `KSI-CMT-03`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No check build presence (Items) found  
- **CLI Command:** `aws codebuild list-projects`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.569813  

---

## ❌ KSI-IAM-06: Identity and Access Management

- **Validation ID:** `KSI-IAM-06`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ Rule error: 'str' object has no attribute 'get'  
- **CLI Command:** `aws iam list-policies --scope Local --query 'Policies[*].PolicyName' --output json`  
- **Interpretation:** ⚠️ Error reading CLI output: 'str' object has no attribute 'get'  
- **Timestamp:** 2025-06-04T23:52:47.569876  

---

## ❌ KSI-CNA-01: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-01`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No security groups returned  
- **CLI Command:** `aws ec2 describe-security-groups`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.570018  

---

## ❌ KSI-CED-01: Cybersecurity Education

- **Validation ID:** `KSI-CED-01`  
- **KSI Family:** Cybersecurity Education  
- **Assertion Reason:** ❌ No IAM users or static training evidence found  
- **CLI Command:** `aws iam list-users`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.570160  

---

## ❌ KSI-CMT-01: Change Management

- **Validation ID:** `KSI-CMT-01`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No CloudTrail trails found — cannot verify config change monitoring  
- **CLI Command:** `aws cloudtrail describe-trails`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.570235  

---

## ❌ KSI-MLA-02: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-02`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No CloudTrail trails found  
- **CLI Command:** `aws cloudtrail describe-trails`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.570295  

---

## ❌ KSI-CNA-07: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-07`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ Rule error: 'list' object has no attribute 'get'  
- **CLI Command:** `aws ec2 describe-instances --query Reservations[*].Instances[*].ImageId`  
- **Interpretation:** ⚠️ Error reading CLI output: 'list' object has no attribute 'get'  
- **Timestamp:** 2025-06-04T23:52:47.570443  

---

## ❌ KSI-RPL-01: Recovery Planning

- **Validation ID:** `KSI-RPL-01`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No backup plans found (BackupPlansList empty)  
- **CLI Command:** `aws backup list-backup-plans`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.570551  

---

## ❌ KSI-MLA-06: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-06`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No Security Hub findings found  
- **CLI Command:** `aws securityhub get-findings --max-results 5`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.570676  

---

## ❌ KSI-TPR-04: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-04`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No upstream alerting findings and no static attestation found.  
- **CLI Command:** `aws securityhub get-findings --max-results 1`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.570765  

---

## ❌ KSI-INR-02: Incident Reporting

- **Validation ID:** `KSI-INR-02`  
- **KSI Family:** Incident Reporting  
- **Assertion Reason:** ❌ No Security Hub findings related to past incidents found (empty Findings list)  
- **CLI Command:** `aws securityhub get-findings --max-results 1`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.570848  

---

## ❌ KSI-PIY-05: Policy and Inventory

- **Validation ID:** `KSI-PIY-05`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No AWS Config rules found (ConfigRules list empty)  
- **CLI Command:** `aws configservice describe-config-rules --max-results 1`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.570939  

---

## ❌ KSI-RPL-04: Recovery Planning

- **Validation ID:** `KSI-RPL-04`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No backup jobs found (BackupJobs list empty)  
- **CLI Command:** `aws backup list-backup-jobs`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.570999  

---

## ❌ KSI-PIY-02: Policy and Inventory

- **Validation ID:** `KSI-PIY-02`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No IAM policies found (Policies list empty)  
- **CLI Command:** `aws iam list-policies --max-items 5`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.571110  

---

## ❌ KSI-CNA-05: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-05`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No WAFv2 WebACLs found (WebACLs list empty)  
- **CLI Command:** `aws wafv2 list-web-acls --scope CLOUDFRONT --region us-east-1`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.571158  

---

## ❌ KSI-CNA-06: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-06`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No check ha routing (RouteTables) found  
- **CLI Command:** `aws ec2 describe-route-tables`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.571294  

---

## ❌ KSI-CMT-02: Change Management

- **Validation ID:** `KSI-CMT-02`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No active StackSets found — cannot confirm redeployment model for infrastructure changes  
- **CLI Command:** `aws cloudformation list-stack-sets --status ACTIVE`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.571596  

---

## ❌ KSI-SVC-03: Service Configuration

- **Validation ID:** `KSI-SVC-03`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No KMS keys found — unable to confirm encryption infrastructure readiness  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.571654  

---

## ❌ KSI-SVC-05: Service Configuration

- **Validation ID:** `KSI-SVC-05`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No AMIs found — unable to confirm cryptographic enforcement of system image integrity  
- **CLI Command:** `aws ec2 describe-images`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.571745  

---

## ❌ KSI-RPL-02: Recovery Planning

- **Validation ID:** `KSI-RPL-02`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No backup plans found — unable to confirm backup targets  
- **CLI Command:** `aws backup list-backup-plans`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.571797  

---

## ❌ KSI-MLA-05: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-05`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No AWS Config rules found — cannot confirm IaC evaluation  
- **CLI Command:** `aws config describe-config-rules`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.571846  

---

## ❌ KSI-IAM-04: Identity and Access Management

- **Validation ID:** `KSI-IAM-04`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM principals or policies found — cannot confirm least-privileged access model  
- **CLI Command:** `aws iam get-account-authorization-details --max-items 50`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.571977  

---

## ❌ KSI-SVC-06: Service Configuration

- **Validation ID:** `KSI-SVC-06`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No KMS keys found — cannot confirm key lifecycle management  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.572027  

---

## ❌ KSI-TPR-03: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-03`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No Inspector2 scan coverage or fallback member evidence found  
- **CLI Command:** `aws inspector2 list-members`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.572078  

---

## ❌ KSI-SVC-02: Service Configuration

- **Validation ID:** `KSI-SVC-02`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No load balancers found — unable to confirm network encryption enforcement  
- **CLI Command:** `aws elbv2 describe-load-balancers`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.572123  

---

## ❌ KSI-IAM-05: Identity and Access Management

- **Validation ID:** `KSI-IAM-05`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM summary map found — unable to assess zero trust posture  
- **CLI Command:** `aws iam get-account-summary`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.572183  

---

## ❌ KSI-INR-01: Incident Reporting

- **Validation ID:** `KSI-INR-01`  
- **KSI Family:** Incident Reporting  
- **Assertion Reason:** ❌ No SecurityHub findings found — incident reporting may not be active  
- **CLI Command:** `aws securityhub get-findings --max-results 1`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.572299  

---

## ❌ KSI-CNA-03: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-03`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No route tables found to evaluate  
- **CLI Command:** `aws ec2 describe-route-tables`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.572352  

---

## ❌ KSI-IAM-02: Identity and Access Management

- **Validation ID:** `KSI-IAM-02`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No check auth models (Users) found  
- **CLI Command:** `aws iam list-users`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.572403  

---

## ❌ KSI-RPL-03: Recovery Planning

- **Validation ID:** `KSI-RPL-03`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No backup plans found — unable to verify recovery posture definition  
- **CLI Command:** `aws backup list-backup-plans`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.572499  

---

## ❌ KSI-IAM-03: Identity and Access Management

- **Validation ID:** `KSI-IAM-03`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM roles found — cannot verify role granularity for service accounts  
- **CLI Command:** `aws iam list-roles --max-items 5`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.572565  

---

## ❌ KSI-MLA-01: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-01`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No CloudWatch log groups found — SIEM visibility not verifiable  
- **CLI Command:** `aws logs describe-log-groups`  
- **Interpretation:** ❌ CLI command failed to execute successfully.  
- **Timestamp:** 2025-06-04T23:52:47.572619  

---

