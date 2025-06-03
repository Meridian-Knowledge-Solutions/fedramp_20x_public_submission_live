# ❌ Failed KSI Validation Report

**Generated:** 2025-06-03T01:06:31.218252Z
**Total Failures:** 43

---

## ❌ KSI-CMT-03: Change Management

- **Validation ID:** `KSI-CMT-03`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No rule defined for this KSI  
- **CLI Command:** `aws codebuild list-projects`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.175612  

---

## ❌ KSI-IAM-06: Identity and Access Management

- **Validation ID:** `KSI-IAM-06`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No password policy found  
- **CLI Command:** `aws iam get-account-authorization-details`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.175672  

---

## ❌ KSI-SVC-07: Service Configuration

- **Validation ID:** `KSI-SVC-07`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No patch groups found  
- **CLI Command:** `aws ssm describe-patch-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.175726  

---

## ❌ KSI-CNA-01: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-01`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No Network ACLs found  
- **CLI Command:** `aws ec2 describe-security-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.175784  

---

## ❌ KSI-CMT-01: Change Management

- **Validation ID:** `KSI-CMT-01`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No rule defined for this KSI  
- **CLI Command:** `aws config describe-configuration-recorders`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.175978  

---

## ❌ KSI-MLA-02: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-02`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No metric filters found  
- **CLI Command:** `aws logs describe-destinations`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176030  

---

## ❌ KSI-PIY-03: Policy and Inventory

- **Validation ID:** `KSI-PIY-03`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No Trusted Advisor checks found  
- **CLI Command:** `aws iam list-policies`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176080  

---

## ❌ KSI-SVC-01: Service Configuration

- **Validation ID:** `KSI-SVC-01`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No web ACLs found  
- **CLI Command:** `aws ssm describe-instance-information`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176162  

---

## ❌ KSI-CNA-07: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-07`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No Well-Architected workloads found  
- **CLI Command:** `aws ec2 describe-images`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176220  

---

## ❌ KSI-PIY-06: Policy and Inventory

- **Validation ID:** `KSI-PIY-06`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No organization structure found  
- **CLI Command:** `aws iam list-users`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176278  

---

## ❌ KSI-CMT-04: Change Management

- **Validation ID:** `KSI-CMT-04`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No rule defined for this KSI  
- **CLI Command:** `aws codebuild list-projects`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176380  

---

## ❌ KSI-MLA-06: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-06`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No vulnerabilities found  
- **CLI Command:** `aws securityhub get-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176454  

---

## ❌ KSI-TPR-04: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-04`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No Inspector findings found  
- **CLI Command:** `aws securityhub get-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176501  

---

## ❌ KSI-INR-02: Incident Reporting

- **Validation ID:** `KSI-INR-02`  
- **KSI Family:** Incident Reporting  
- **Assertion Reason:** ❌ No SecurityHub findings found  
- **CLI Command:** `aws securityhub get-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176545  

---

## ❌ KSI-PIY-05: Policy and Inventory

- **Validation ID:** `KSI-PIY-05`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No compliance rules found  
- **CLI Command:** `aws config describe-config-rules`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176593  

---

## ❌ KSI-RPL-04: Recovery Planning

- **Validation ID:** `KSI-RPL-04`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No restore jobs found  
- **CLI Command:** `aws backup list-backup-jobs`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176638  

---

## ❌ KSI-INR-03: Incident Reporting

- **Validation ID:** `KSI-INR-03`  
- **KSI Family:** Incident Reporting  
- **Assertion Reason:** ❌ No Inspector findings found  
- **CLI Command:** `aws securityhub get-insight-results`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176684  

---

## ❌ KSI-PIY-02: Policy and Inventory

- **Validation ID:** `KSI-PIY-02`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No IAM policies found  
- **CLI Command:** `aws iam list-policies`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176727  

---

## ❌ KSI-CNA-05: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-05`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No VPCs found  
- **CLI Command:** `aws ec2 describe-network-interfaces`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176770  

---

## ❌ KSI-MLA-03: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-03`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No subscription filters found  
- **CLI Command:** `aws inspector2 list-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176812  

---

## ❌ KSI-SVC-04: Service Configuration

- **Validation ID:** `KSI-SVC-04`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No configuration recorder statuses found  
- **CLI Command:** `aws ssm list-associations`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176855  

---

## ❌ KSI-PIY-01: Policy and Inventory

- **Validation ID:** `KSI-PIY-01`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No discovered resources  
- **CLI Command:** `aws ec2 describe-instances`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176949  

---

## ❌ KSI-PIY-04: Policy and Inventory

- **Validation ID:** `KSI-PIY-04`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No CodeCommit repositories found  
- **CLI Command:** `aws codepipeline list-pipelines`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.176992  

---

## ❌ KSI-CNA-04: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-04`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No EC2 reservations found  
- **CLI Command:** `aws ec2 describe-instances`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177035  

---

## ❌ KSI-CED-02: Cybersecurity Education

- **Validation ID:** `KSI-CED-02`  
- **KSI Family:** Cybersecurity Education  
- **Assertion Reason:** ❌ No IAM groups found  
- **CLI Command:** `aws iam list-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177077  

---

## ❌ KSI-TPR-01: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-01`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No CloudFormation stack resources found  
- **CLI Command:** `aws iam list-roles`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177136  

---

## ❌ KSI-CMT-02: Change Management

- **Validation ID:** `KSI-CMT-02`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No rule defined for this KSI  
- **CLI Command:** `aws ec2 describe-instances`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177186  

---

## ❌ KSI-SVC-03: Service Configuration

- **Validation ID:** `KSI-SVC-03`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No KMS keys found  
- **CLI Command:** `aws ec2 describe-volumes`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177231  

---

## ❌ KSI-TPR-02: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-02`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No SecurityHub findings for FedRAMP Moderate  
- **CLI Command:** `aws ec2 describe-instances`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177275  

---

## ❌ KSI-SVC-05: Service Configuration

- **Validation ID:** `KSI-SVC-05`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No DRT access role found  
- **CLI Command:** `aws ec2 describe-images`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177316  

---

## ❌ KSI-RPL-02: Recovery Planning

- **Validation ID:** `KSI-RPL-02`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No recovery points found  
- **CLI Command:** `aws backup list-backup-selections`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177360  

---

## ❌ KSI-MLA-05: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-05`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No config rules found  
- **CLI Command:** `aws config describe-config-rules`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177405  

---

## ❌ KSI-MLA-04: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-04`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No destinations found  
- **CLI Command:** `aws inspector2 list-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177448  

---

## ❌ KSI-SVC-06: Service Configuration

- **Validation ID:** `KSI-SVC-06`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No key rotation status  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177540  

---

## ❌ KSI-TPR-03: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-03`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ SecurityHub hub not described  
- **CLI Command:** `aws inspector2 list-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177584  

---

## ❌ KSI-SVC-02: Service Configuration

- **Validation ID:** `KSI-SVC-02`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No VPN connections found  
- **CLI Command:** `aws elbv2 describe-load-balancers`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177626  

---

## ❌ KSI-IAM-05: Identity and Access Management

- **Validation ID:** `KSI-IAM-05`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No account authorization details found  
- **CLI Command:** `aws iam get-account-summary`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177682  

---

## ❌ KSI-PIY-07: Policy and Inventory

- **Validation ID:** `KSI-PIY-07`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No document permissions found  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177730  

---

## ❌ KSI-INR-01: Incident Reporting

- **Validation ID:** `KSI-INR-01`  
- **KSI Family:** Incident Reporting  
- **Assertion Reason:** ❌ No SecurityHub insights found  
- **CLI Command:** `aws securityhub get-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177775  

---

## ❌ KSI-CNA-03: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-03`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No security groups found  
- **CLI Command:** `aws ec2 describe-route-tables`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177822  

---

## ❌ KSI-CMT-05: Change Management

- **Validation ID:** `KSI-CMT-05`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No rule defined for this KSI  
- **CLI Command:** `aws ssm describe-document`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177921  

---

## ❌ KSI-RPL-03: Recovery Planning

- **Validation ID:** `KSI-RPL-03`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No backup jobs found  
- **CLI Command:** `aws backup list-recovery-points-by-backup-vault`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.177965  

---

## ❌ KSI-IAM-03: Identity and Access Management

- **Validation ID:** `KSI-IAM-03`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM roles found  
- **CLI Command:** `aws iam list-roles`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T01:06:31.178008  

---

