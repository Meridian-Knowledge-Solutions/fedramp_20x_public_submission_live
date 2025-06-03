# ❌ Failed KSI Validation Report

**Generated:** 2025-06-03T20:36:59.721532Z
**Total Failures:** 42

---

## ❌ KSI-CMT-03: Change Management

- **Validation ID:** `KSI-CMT-03`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No check build presence (Items) found  
- **CLI Command:** `aws codebuild list-projects`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.668993  

---

## ❌ KSI-SVC-07: Service Configuration

- **Validation ID:** `KSI-SVC-07`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No patch groups defined (Mappings is empty)  
- **CLI Command:** `aws ssm describe-patch-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.669236  

---

## ❌ KSI-IAM-01: Identity and Access Management

- **Validation ID:** `KSI-IAM-01`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No users found in AWS SSO Identity Center  
- **CLI Command:** `aws identitystore list-users --identity-store-id <ID_STORE_ID>`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.669448  

---

## ❌ KSI-CMT-01: Change Management

- **Validation ID:** `KSI-CMT-01`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No check config mgmt (Items) found  
- **CLI Command:** `aws config describe-configuration-recorders`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.669684  

---

## ❌ KSI-PIY-03: Policy and Inventory

- **Validation ID:** `KSI-PIY-03`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ Rule error: name 'os' is not defined  
- **CLI Command:** `aws iam list-policies`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.669900  

---

## ❌ KSI-SVC-01: Service Configuration

- **Validation ID:** `KSI-SVC-01`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No list managed instances (InstanceInformationList) found  
- **CLI Command:** `aws ssm describe-instance-information`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.669985  

---

## ❌ KSI-CNA-07: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-07`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No confirm official amis (Items) found  
- **CLI Command:** `aws ec2 describe-images`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.670092  

---

## ❌ KSI-RPL-01: Recovery Planning

- **Validation ID:** `KSI-RPL-01`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No confirm backup rto (Items) found  
- **CLI Command:** `aws backup list-backup-plans`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.670307  

---

## ❌ KSI-CMT-04: Change Management

- **Validation ID:** `KSI-CMT-04`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No check ci testing (Items) found  
- **CLI Command:** `aws codebuild list-projects`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.670397  

---

## ❌ KSI-MLA-06: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-06`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No check sh prioritization (Items) found  
- **CLI Command:** `aws securityhub get-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.670528  

---

## ❌ KSI-TPR-04: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-04`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No check upstream alerting (Items) found  
- **CLI Command:** `aws securityhub get-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.670627  

---

## ❌ KSI-INR-02: Incident Reporting

- **Validation ID:** `KSI-INR-02`  
- **KSI Family:** Incident Reporting  
- **Assertion Reason:** ❌ No check log of past incidents (Items) found  
- **CLI Command:** `aws securityhub get-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.670722  

---

## ❌ KSI-PIY-05: Policy and Inventory

- **Validation ID:** `KSI-PIY-05`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No check resource evaluation (Items) found  
- **CLI Command:** `aws config describe-config-rules`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.670819  

---

## ❌ KSI-RPL-04: Recovery Planning

- **Validation ID:** `KSI-RPL-04`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No check for drills (Items) found  
- **CLI Command:** `aws backup list-backup-jobs`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.670911  

---

## ❌ KSI-INR-03: Incident Reporting

- **Validation ID:** `KSI-INR-03`  
- **KSI Family:** Incident Reporting  
- **Assertion Reason:** ❌ No review aar patterns (Items) found  
- **CLI Command:** `aws securityhub get-insight-results`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.670999  

---

## ❌ KSI-PIY-02: Policy and Inventory

- **Validation ID:** `KSI-PIY-02`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No rule defined for this KSI  
- **CLI Command:** `aws iam list-policies`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.671115  

---

## ❌ KSI-CNA-05: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-05`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No inspect interface policies (WebACLs) found  
- **CLI Command:** `aws wafv2 list-web-acls`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.671214  

---

## ❌ KSI-MLA-03: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-03`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No list findings (Items) found  
- **CLI Command:** `aws inspector2 list-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.671303  

---

## ❌ KSI-SVC-04: Service Configuration

- **Validation ID:** `KSI-SVC-04`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No check config state mgmt (Items) found  
- **CLI Command:** `aws ssm list-associations`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.671391  

---

## ❌ KSI-PIY-01: Policy and Inventory

- **Validation ID:** `KSI-PIY-01`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No asset discovery (Reservations) found  
- **CLI Command:** `aws ec2 describe-instances`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.671599  

---

## ❌ KSI-PIY-04: Policy and Inventory

- **Validation ID:** `KSI-PIY-04`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No check sdlc (Items) found  
- **CLI Command:** `aws codepipeline list-pipelines`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.671689  

---

## ❌ KSI-CNA-04: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-04`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No check instance profiles (Reservations) found  
- **CLI Command:** `aws ec2 describe-instances`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.671781  

---

## ❌ KSI-CED-02: Cybersecurity Education

- **Validation ID:** `KSI-CED-02`  
- **KSI Family:** Cybersecurity Education  
- **Assertion Reason:** ❌ No check role training (Items) found  
- **CLI Command:** `aws iam list-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.671870  

---

## ❌ KSI-TPR-01: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-01`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No detect 3rd party (Items) found  
- **CLI Command:** `aws iam list-roles`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.671961  

---

## ❌ KSI-CMT-02: Change Management

- **Validation ID:** `KSI-CMT-02`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No detect manual changes (Reservations) found  
- **CLI Command:** `aws ec2 describe-instances`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.672072  

---

## ❌ KSI-SVC-03: Service Configuration

- **Validation ID:** `KSI-SVC-03`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No check encrypted volumes (ServerSideEncryptionConfiguration) found  
- **CLI Command:** `aws rds describe-db-instances && aws ec2 describe-volumes && aws s3api get-bucket-encryption`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.672164  

---

## ❌ KSI-TPR-02: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-02`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No check fedramp use (Reservations) found  
- **CLI Command:** `aws ec2 describe-instances`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.672252  

---

## ❌ KSI-SVC-05: Service Configuration

- **Validation ID:** `KSI-SVC-05`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No check signed amis (Items) found  
- **CLI Command:** `aws ec2 describe-images`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.672349  

---

## ❌ KSI-RPL-02: Recovery Planning

- **Validation ID:** `KSI-RPL-02`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No check backup targets (Items) found  
- **CLI Command:** `aws backup list-backup-selections`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.672442  

---

## ❌ KSI-MLA-05: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-05`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No review iac eval (Items) found  
- **CLI Command:** `aws config describe-config-rules`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.672538  

---

## ❌ KSI-MLA-04: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-04`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No check scan frequency (InstanceInformationList) found  
- **CLI Command:** `aws ssm describe-instance-information`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.672629  

---

## ❌ KSI-IAM-04: Identity and Access Management

- **Validation ID:** `KSI-IAM-04`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No review policies (Items) found  
- **CLI Command:** `aws iam get-account-authorization-details`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.672717  

---

## ❌ KSI-SVC-06: Service Configuration

- **Validation ID:** `KSI-SVC-06`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No check key lifecycle mgmt (Items) found  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.672812  

---

## ❌ KSI-TPR-03: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-03`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No supply chain risk (Items) found  
- **CLI Command:** `aws inspector2 list-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.672902  

---

## ❌ KSI-SVC-02: Service Configuration

- **Validation ID:** `KSI-SVC-02`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No inspect traffic encryption (Items) found  
- **CLI Command:** `aws elbv2 describe-load-balancers`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.672994  

---

## ❌ KSI-IAM-05: Identity and Access Management

- **Validation ID:** `KSI-IAM-05`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No detect privilege risks (Items) found  
- **CLI Command:** `aws iam get-account-summary`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.673129  

---

## ❌ KSI-PIY-07: Policy and Inventory

- **Validation ID:** `KSI-PIY-07`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No review supply chain decision (Items) found  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.673224  

---

## ❌ KSI-INR-01: Incident Reporting

- **Validation ID:** `KSI-INR-01`  
- **KSI Family:** Incident Reporting  
- **Assertion Reason:** ❌ No check reporting (Items) found  
- **CLI Command:** `aws securityhub get-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.673304  

---

## ❌ KSI-CMT-05: Change Management

- **Validation ID:** `KSI-CMT-05`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No check sops (Items) found  
- **CLI Command:** `aws ssm describe-document`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.673559  

---

## ❌ KSI-RPL-03: Recovery Planning

- **Validation ID:** `KSI-RPL-03`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No verify restore points (Items) found  
- **CLI Command:** `aws backup list-recovery-points-by-backup-vault`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.673638  

---

## ❌ KSI-IAM-03: Identity and Access Management

- **Validation ID:** `KSI-IAM-03`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No check role granularity (Items) found  
- **CLI Command:** `aws iam list-roles`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.673709  

---

## ❌ KSI-MLA-01: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-01`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No siem visibility (Items) found  
- **CLI Command:** `aws logs describe-log-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-03T20:36:59.673794  

---

