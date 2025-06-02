# ❌ Failed KSI Validation Report

**Generated:** 2025-06-02T08:08:08.112732Z
**Total Failures:** 35

---

## ❌ KSI-CMT-03: Change Management

- **Validation ID:** `KSI-CMT-03`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No rule defined for this KSI  
- **CLI Command:** `aws codebuild batch-get-projects`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:07.998381  

---

## ❌ KSI-IAM-06: Identity and Access Management

- **Validation ID:** `KSI-IAM-06`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No password policy found  
- **CLI Command:** `aws iam get-account-password-policy`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:07.998489  

---

## ❌ KSI-SVC-07: Service Configuration

- **Validation ID:** `KSI-SVC-07`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No patch groups found  
- **CLI Command:** `aws ssm describe-patch-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:07.998559  

---

## ❌ KSI-CED-01: Cybersecurity Education

- **Validation ID:** `KSI-CED-01`  
- **KSI Family:** Cybersecurity Education  
- **Assertion Reason:** ❌ No SSO users found  
- **CLI Command:** `aws sso list-users --instance-arn arn:aws:sso:::instance/ssoins-1234567890abcdef`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:07.998764  

---

## ❌ KSI-CMT-01: Change Management

- **Validation ID:** `KSI-CMT-01`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No rule defined for this KSI  
- **CLI Command:** `AttributeValue=Modify"`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:07.998835  

---

## ❌ KSI-MLA-02: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-02`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No metric filters found  
- **CLI Command:** `aws logs describe-metric-filters`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:07.998890  

---

## ❌ KSI-PIY-03: Policy and Inventory

- **Validation ID:** `KSI-PIY-03`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No Trusted Advisor checks found  
- **CLI Command:** `aws support describe-trusted-advisor-checks --language en`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:07.998943  

---

## ❌ KSI-SVC-01: Service Configuration

- **Validation ID:** `KSI-SVC-01`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No web ACLs found  
- **CLI Command:** `aws wafv2 list-web-acls`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:07.998995  

---

## ❌ KSI-CNA-07: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-07`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No Well-Architected workloads found  
- **CLI Command:** `aws wellarchitected list-workloads`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:07.999043  

---

## ❌ KSI-PIY-06: Policy and Inventory

- **Validation ID:** `KSI-PIY-06`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No organization structure found  
- **CLI Command:** `aws organizations describe-organization`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:07.999095  

---

## ❌ KSI-CMT-04: Change Management

- **Validation ID:** `KSI-CMT-04`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No rule defined for this KSI  
- **CLI Command:** `aws ssm list-documents`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.000995  

---

## ❌ KSI-MLA-06: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-06`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No vulnerabilities found  
- **CLI Command:** `aws inspector2 list-vulnerabilities`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.001248  

---

## ❌ KSI-TPR-04: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-04`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No Inspector findings found  
- **CLI Command:** `aws inspector2 list-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.001334  

---

## ❌ KSI-PIY-05: Policy and Inventory

- **Validation ID:** `KSI-PIY-05`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No compliance rules found  
- **CLI Command:** `aws config describe-compliance-by-config-rule`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.021583  

---

## ❌ KSI-RPL-04: Recovery Planning

- **Validation ID:** `KSI-RPL-04`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No restore jobs found  
- **CLI Command:** `aws backup list-restore-jobs`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.021678  

---

## ❌ KSI-INR-03: Incident Reporting

- **Validation ID:** `KSI-INR-03`  
- **KSI Family:** Incident Reporting  
- **Assertion Reason:** ❌ No Inspector findings found  
- **CLI Command:** `aws inspector list-findings`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.021738  

---

## ❌ KSI-MLA-03: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-03`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No subscription filters found  
- **CLI Command:** `aws logs describe-subscription-filters`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.024622  

---

## ❌ KSI-SVC-04: Service Configuration

- **Validation ID:** `KSI-SVC-04`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No configuration recorder statuses found  
- **CLI Command:** `aws config describe-configuration-recorder-status`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.024711  

---

## ❌ KSI-PIY-01: Policy and Inventory

- **Validation ID:** `KSI-PIY-01`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No discovered resources  
- **CLI Command:** `aws config list-discovered-resources --resource-type AWS::EC2::Instance`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.024854  

---

## ❌ KSI-PIY-04: Policy and Inventory

- **Validation ID:** `KSI-PIY-04`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No CodeCommit repositories found  
- **CLI Command:** `aws codecommit list-repositories`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.024905  

---

## ❌ KSI-CNA-04: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-04`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No EC2 reservations found  
- **CLI Command:** `aws ec2 describe-instances`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.024954  

---

## ❌ KSI-CED-02: Cybersecurity Education

- **Validation ID:** `KSI-CED-02`  
- **KSI Family:** Cybersecurity Education  
- **Assertion Reason:** ❌ No IAM groups found  
- **CLI Command:** `aws iam list-groups`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.025002  

---

## ❌ KSI-TPR-01: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-01`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No CloudFormation stack resources found  
- **CLI Command:** `aws config list-discovered-resources --resource-type AWS::CloudFormation::Stack`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.025083  

---

## ❌ KSI-CMT-02: Change Management

- **Validation ID:** `KSI-CMT-02`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No rule defined for this KSI  
- **CLI Command:** `aws s3api list-object-versions --bucket your-terraform-state-bucket`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.025138  

---

## ❌ KSI-TPR-02: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-02`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No SecurityHub findings for FedRAMP Moderate  
- **CLI Command:** `aws securityhub get-findings --filters ProductArn={Value=arn:aws:securityhub:::product/aws/fedramp-moderate;Comparison=EQUALS}`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.025241  

---

## ❌ KSI-SVC-05: Service Configuration

- **Validation ID:** `KSI-SVC-05`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No DRT access role found  
- **CLI Command:** `aws shield describe-drt-access`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.025289  

---

## ❌ KSI-RPL-02: Recovery Planning

- **Validation ID:** `KSI-RPL-02`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ No recovery points found  
- **CLI Command:** `aws backup list-recovery-points-by-backup-vault --backup-vault-name default`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.025336  

---

## ❌ KSI-MLA-05: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-05`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No config rules found  
- **CLI Command:** `aws config describe-config-rules`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.025431  

---

## ❌ KSI-MLA-04: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-04`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No destinations found  
- **CLI Command:** `aws logs describe-destinations`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.025484  

---

## ❌ KSI-SVC-06: Service Configuration

- **Validation ID:** `KSI-SVC-06`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No key rotation status  
- **CLI Command:** `aws kms list-key-rotation-status`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.025590  

---

## ❌ KSI-TPR-03: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-03`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ SecurityHub hub not described  
- **CLI Command:** `aws securityhub describe-hub`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.025638  

---

## ❌ KSI-SVC-02: Service Configuration

- **Validation ID:** `KSI-SVC-02`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No VPN connections found  
- **CLI Command:** `aws ec2 describe-vpn-connections`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.025685  

---

## ❌ KSI-PIY-07: Policy and Inventory

- **Validation ID:** `KSI-PIY-07`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No document permissions found  
- **CLI Command:** `aws ssm describe-document-permissions`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.066662  

---

## ❌ KSI-INR-01: Incident Reporting

- **Validation ID:** `KSI-INR-01`  
- **KSI Family:** Incident Reporting  
- **Assertion Reason:** ❌ No SecurityHub insights found  
- **CLI Command:** `aws securityhub list-insights`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.066791  

---

## ❌ KSI-CMT-05: Change Management

- **Validation ID:** `KSI-CMT-05`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No rule defined for this KSI  
- **CLI Command:** `aws cloudwatch describe-alarms`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-02T08:08:08.066974  

---

