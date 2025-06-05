# ❌ Failed KSI Validation Report

**Generated:** 2025-06-05T07:51:26.477657Z
**Total Failures:** 15

---

## ❌ KSI-CNA-02: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-02`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ Rule error: 'str' object has no attribute 'get'  
- **CLI Command:** `aws ec2 describe-subnets --query 'Subnets[*].SubnetId'`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.434515  

---

## ❌ KSI-CMT-03: Change Management

- **Validation ID:** `KSI-CMT-03`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No check build presence (Items) found  
- **CLI Command:** `aws codebuild list-projects`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.434588  

---

## ❌ KSI-IAM-06: Identity and Access Management

- **Validation ID:** `KSI-IAM-06`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM roles found — cannot evaluate privileged disablement readiness  
- **CLI Command:** `aws iam list-account-authorization-details --query 'RoleDetailList[*].RoleName'`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.434652  

---

## ❌ KSI-CNA-01: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-01`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ Rule error: 'str' object has no attribute 'get'  
- **CLI Command:** `aws ec2 describe-security-groups --query 'SecurityGroups[*].GroupId'`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.434774  

---

## ❌ KSI-MLA-02: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-02`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ Rule error: 'str' object has no attribute 'get'  
- **CLI Command:** `aws cloudtrail describe-trails --query 'trailList[*].Name'`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.435008  

---

## ❌ KSI-RPL-01: Recovery Planning

- **Validation ID:** `KSI-RPL-01`  
- **KSI Family:** Recovery Planning  
- **Assertion Reason:** ❌ Rule error: 'str' object has no attribute 'get'  
- **CLI Command:** `aws backup list-backup-plans --query 'BackupPlansList[*].BackupPlanName'`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.435304  

---

## ❌ KSI-PIY-05: Policy and Inventory

- **Validation ID:** `KSI-PIY-05`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No AWS Config rules found (ConfigRules list empty)  
- **CLI Command:** `aws configservice describe-config-rules --max-results 1`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.435647  

---

## ❌ KSI-CNA-05: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-05`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No WAFv2 WebACLs found (WebACLs list empty)  
- **CLI Command:** `aws wafv2 list-web-acls --scope CLOUDFRONT --region us-east-1 --query 'WebACLs[*].Name'`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.435833  

---

## ❌ KSI-TPR-01: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-01`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No active Access Analyzers found — unable to evaluate third-party access risk  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.436202  

---

## ❌ KSI-MLA-05: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-05`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No AWS Config rules found — cannot confirm IaC evaluation  
- **CLI Command:** `aws config describe-config-rules`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.436528  

---

## ❌ KSI-IAM-04: Identity and Access Management

- **Validation ID:** `KSI-IAM-04`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM principals or policies found — cannot confirm least-privileged access model  
- **CLI Command:** `aws iam list-policies --scope Local --query 'Policies[*].PolicyName'`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.436624  

---

## ❌ KSI-TPR-03: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-03`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No Inspector2 scan coverage or fallback member evidence found  
- **CLI Command:** `aws inspector2 list-members --query 'members[*].accountId'`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.436724  

---

## ❌ KSI-SVC-02: Service Configuration

- **Validation ID:** `KSI-SVC-02`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No load balancers found — unable to confirm network encryption enforcement  
- **CLI Command:** `aws elbv2 describe-load-balancers`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.436769  

---

## ❌ KSI-IAM-05: Identity and Access Management

- **Validation ID:** `KSI-IAM-05`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM summary map found — unable to assess zero trust posture  
- **CLI Command:** `aws iam get-account-summary`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.436824  

---

## ❌ KSI-CNA-03: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-03`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ Rule error: 'str' object has no attribute 'get'  
- **CLI Command:** `aws ec2 describe-route-tables --query 'RouteTables[*].RouteTableId'`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T07:51:26.436995  

---

