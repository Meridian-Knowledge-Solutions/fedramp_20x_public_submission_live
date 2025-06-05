# ❌ Failed KSI Validation Report

**Generated:** 2025-06-05T00:46:26.590576Z
**Total Failures:** 12

---

## ❌ KSI-CMT-03: Change Management

- **Validation ID:** `KSI-CMT-03`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No check build presence (Items) found  
- **CLI Command:** `aws codebuild list-projects`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T00:46:26.546326  

---

## ❌ KSI-IAM-06: Identity and Access Management

- **Validation ID:** `KSI-IAM-06`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ Rule error: 'str' object has no attribute 'get'  
- **CLI Command:** `aws iam list-policies --scope Local --query 'Policies[*].PolicyName' --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T00:46:26.546391  

---

## ❌ KSI-SVC-01: Service Configuration

- **Validation ID:** `KSI-SVC-01`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ Unexpected structure or missing InstanceInformationList in output.  
- **CLI Command:** `aws ssm describe-instance-information --max-results 5`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T00:46:26.546915  

---

## ❌ KSI-PIY-05: Policy and Inventory

- **Validation ID:** `KSI-PIY-05`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No AWS Config rules found (ConfigRules list empty)  
- **CLI Command:** `aws configservice describe-config-rules --max-results 1`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T00:46:26.547425  

---

## ❌ KSI-CNA-05: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-05`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No WAFv2 WebACLs found (WebACLs list empty)  
- **CLI Command:** `aws wafv2 list-web-acls --scope CLOUDFRONT --region us-east-1`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T00:46:26.547653  

---

## ❌ KSI-TPR-01: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-01`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ IAM role scan failed: Output too large or not JSON serializable  
- **CLI Command:** `aws iam list-roles`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T00:46:26.548063  

---

## ❌ KSI-MLA-05: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-05`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No AWS Config rules found — cannot confirm IaC evaluation  
- **CLI Command:** `aws config describe-config-rules`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T00:46:26.548390  

---

## ❌ KSI-IAM-04: Identity and Access Management

- **Validation ID:** `KSI-IAM-04`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ IAM policy query failed: Output too large or not JSON serializable  
- **CLI Command:** `aws iam get-account-authorization-details --max-items 50`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T00:46:26.548487  

---

## ❌ KSI-TPR-03: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-03`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No Inspector2 scan coverage or fallback member evidence found  
- **CLI Command:** `aws inspector2 list-members`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T00:46:26.548595  

---

## ❌ KSI-SVC-02: Service Configuration

- **Validation ID:** `KSI-SVC-02`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No load balancers found — unable to confirm network encryption enforcement  
- **CLI Command:** `aws elbv2 describe-load-balancers`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T00:46:26.548684  

---

## ❌ KSI-IAM-05: Identity and Access Management

- **Validation ID:** `KSI-IAM-05`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM summary map found — unable to assess zero trust posture  
- **CLI Command:** `aws iam get-account-summary`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T00:46:26.548760  

---

## ❌ KSI-CNA-03: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-03`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ Found 1 public route(s) not scoped for utility/bastion use: rtb-0ed80c2df92e37cad  
- **CLI Command:** `aws ec2 describe-route-tables`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T00:46:26.548950  

---

