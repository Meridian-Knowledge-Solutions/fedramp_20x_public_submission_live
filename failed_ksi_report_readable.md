# ❌ Failed KSI Validation Report

**Generated:** 2025-06-05T23:49:48.307247Z
**Total Failures:** 50

---

## ❌ KSI-CMT-03: Change Management

- **Validation ID:** `KSI-CMT-03`  
- **KSI Family:** Change Management  
- **Assertion Reason:** ❌ No check build presence (Items) found  
- **CLI Command:** `aws codebuild list-projects`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.252609  

---

## ❌ KSI-IAM-06: Identity and Access Management

- **Validation ID:** `KSI-IAM-06`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM roles found — cannot evaluate privileged disablement readiness  
- **CLI Command:** `aws iam list-users --query 'Users[?contains(UserName, `admin`) || contains(UserName, `root`)]' --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.252685  

---

## ❌ KSI-IAM-06: Identity and Access Management

- **Validation ID:** `KSI-IAM-06`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM roles found — cannot evaluate privileged disablement readiness  
- **CLI Command:** `aws logs describe-log-groups --log-group-name-prefix '/aws/lambda' --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.252688  

---

## ❌ KSI-IAM-06: Identity and Access Management

- **Validation ID:** `KSI-IAM-06`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM roles found — cannot evaluate privileged disablement readiness  
- **CLI Command:** `aws events list-rules --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.252691  

---

## ❌ KSI-IAM-06: Identity and Access Management

- **Validation ID:** `KSI-IAM-06`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM roles found — cannot evaluate privileged disablement readiness  
- **CLI Command:** `aws cloudwatch describe-alarms --alarm-names 'HighPrivilegedActivity' --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.252695  

---

## ❌ KSI-IAM-06: Identity and Access Management

- **Validation ID:** `KSI-IAM-06`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM roles found — cannot evaluate privileged disablement readiness  
- **CLI Command:** `aws iam generate-credential-report --output json && aws iam get-credential-report --output text`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.252698  

---

## ❌ KSI-IAM-01: Identity and Access Management

- **Validation ID:** `KSI-IAM-01`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ Rule error: 'str' object has no attribute 'get'  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.252925  

---

## ❌ KSI-MLA-02: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-02`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No CloudTrail trails found  
- **CLI Command:** `aws cloudwatch describe-alarms --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.253163  

---

## ❌ KSI-MLA-02: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-02`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No CloudTrail trails found  
- **CLI Command:** `aws logs describe-metric-filters --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.253166  

---

## ❌ KSI-MLA-02: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-02`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No CloudTrail trails found  
- **CLI Command:** `aws events list-rules --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.253168  

---

## ❌ KSI-MLA-02: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-02`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No CloudTrail trails found  
- **CLI Command:** `aws lambda list-functions --query 'Functions[?contains(FunctionName, `log`) || contains(FunctionName, `audit`)]' --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.253170  

---

## ❌ KSI-MLA-02: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-02`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No CloudTrail trails found  
- **CLI Command:** `aws opensearch list-domain-names --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.253172  

---

## ❌ KSI-MLA-06: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-06`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ Rule error: 'list' object has no attribute 'get'  
- **CLI Command:** `aws securityhub get-findings --query 'Findings[?Compliance.Status==`FAILED`]' --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.256651  

---

## ❌ KSI-MLA-06: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-06`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No Security Hub findings found  
- **CLI Command:** `aws ssm describe-patch-group-state --patch-group production --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.256657  

---

## ❌ KSI-MLA-06: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-06`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ Rule error: 'str' object has no attribute 'get'  
- **CLI Command:** `aws inspector2 list-findings --filter-criteria '{"severities":[{"comparison":"EQUALS","value":"CRITICAL"},{"comparison":"EQUALS","value":"HIGH"}]}' --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.256661  

---

## ❌ KSI-MLA-06: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-06`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ Rule error: 'str' object has no attribute 'get'  
- **CLI Command:** `aws support describe-cases --language en --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.256664  

---

## ❌ KSI-MLA-06: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-06`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No Security Hub findings found  
- **CLI Command:** `aws organizations list-accounts --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.256666  

---

## ❌ KSI-PIY-05: Policy and Inventory

- **Validation ID:** `KSI-PIY-05`  
- **KSI Family:** Policy and Inventory  
- **Assertion Reason:** ❌ No AWS Config rules found (ConfigRules list empty)  
- **CLI Command:** `aws configservice describe-config-rules --max-results 1`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.257080  

---

## ❌ KSI-CNA-05: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-05`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ No WAFv2 WebACLs found (WebACLs list empty)  
- **CLI Command:** `aws wafv2 list-web-acls --scope CLOUDFRONT --region us-east-1`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.257288  

---

## ❌ KSI-TPR-01: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-01`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No active Access Analyzers found — unable to evaluate third-party access risk  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.257714  

---

## ❌ KSI-MLA-05: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-05`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ Rule error: 'str' object has no attribute 'get'  
- **CLI Command:** `aws config describe-config-rules --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.258046  

---

## ❌ KSI-MLA-05: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-05`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No AWS Config rules found — cannot confirm IaC evaluation  
- **CLI Command:** `aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.258050  

---

## ❌ KSI-MLA-05: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-05`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ Rule error: 'str' object has no attribute 'get'  
- **CLI Command:** `aws cloudformation detect-stack-drift --stack-name production-stack --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.258052  

---

## ❌ KSI-MLA-05: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-05`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No AWS Config rules found — cannot confirm IaC evaluation  
- **CLI Command:** `aws codeartifact list-repositories --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.258054  

---

## ❌ KSI-MLA-05: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-05`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No AWS Config rules found — cannot confirm IaC evaluation  
- **CLI Command:** `aws codebuild list-projects --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.258056  

---

## ❌ KSI-MLA-04: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-04`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ Rule error: 'str' object has no attribute 'get'  
- **CLI Command:** `aws inspector2 get-configuration --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.260208  

---

## ❌ KSI-MLA-04: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-04`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ Rule error: 'list' object has no attribute 'get'  
- **CLI Command:** `aws securityhub get-findings --query 'Findings[?ProductName==`Inspector`]' --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.260223  

---

## ❌ KSI-MLA-04: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-04`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ Rule error: 'list' object has no attribute 'get'  
- **CLI Command:** `aws ec2 describe-instances --query 'Reservations[*].Instances[*].{InstanceId:InstanceId,State:State.Name,SecurityGroups:SecurityGroups}' --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.260231  

---

## ❌ KSI-IAM-04: Identity and Access Management

- **Validation ID:** `KSI-IAM-04`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM principals or policies found — cannot confirm least-privileged access model  
- **CLI Command:** `aws iam list-roles --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.260639  

---

## ❌ KSI-IAM-04: Identity and Access Management

- **Validation ID:** `KSI-IAM-04`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ Unexpected output format  
- **CLI Command:** `aws iam list-attached-role-policies --role-name AdminRole --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.260653  

---

## ❌ KSI-IAM-04: Identity and Access Management

- **Validation ID:** `KSI-IAM-04`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM principals or policies found — cannot confirm least-privileged access model  
- **CLI Command:** `aws iam generate-credential-report --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.260658  

---

## ❌ KSI-IAM-04: Identity and Access Management

- **Validation ID:** `KSI-IAM-04`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ Unexpected output format  
- **CLI Command:** `aws iam get-credential-report --output text`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.260661  

---

## ❌ KSI-TPR-03: Third-Party Information Resources

- **Validation ID:** `KSI-TPR-03`  
- **KSI Family:** Third-Party Information Resources  
- **Assertion Reason:** ❌ No Inspector2 scan coverage or fallback member evidence found  
- **CLI Command:** `aws inspector2 list-members`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.260889  

---

## ❌ KSI-SVC-02: Service Configuration

- **Validation ID:** `KSI-SVC-02`  
- **KSI Family:** Service Configuration  
- **Assertion Reason:** ❌ No load balancers found — unable to confirm network encryption enforcement  
- **CLI Command:** `aws elbv2 describe-load-balancers`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261010  

---

## ❌ KSI-IAM-05: Identity and Access Management

- **Validation ID:** `KSI-IAM-05`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ Rule error: 'list' object has no attribute 'get'  
- **CLI Command:** `aws iam list-policies --scope AWS --query 'Policies[?contains(PolicyName, `Condition`)]' --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261151  

---

## ❌ KSI-IAM-05: Identity and Access Management

- **Validation ID:** `KSI-IAM-05`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM summary map found — unable to assess zero trust posture  
- **CLI Command:** `aws logs describe-log-groups --log-group-name-prefix '/aws/cloudtrail' --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261156  

---

## ❌ KSI-IAM-05: Identity and Access Management

- **Validation ID:** `KSI-IAM-05`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ Rule error: 'str' object has no attribute 'get'  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261161  

---

## ❌ KSI-IAM-05: Identity and Access Management

- **Validation ID:** `KSI-IAM-05`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM summary map found — unable to assess zero trust posture  
- **CLI Command:** `aws organizations list-accounts --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261164  

---

## ❌ KSI-IAM-05: Identity and Access Management

- **Validation ID:** `KSI-IAM-05`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM summary map found — unable to assess zero trust posture  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261167  

---

## ❌ KSI-CNA-03: Cloud Native Architecture

- **Validation ID:** `KSI-CNA-03`  
- **KSI Family:** Cloud Native Architecture  
- **Assertion Reason:** ❌ Found 1 public route(s) not scoped for utility/bastion use: rtb-0ed80c2df92e37cad  
- **CLI Command:** `aws ec2 describe-route-tables`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261384  

---

## ❌ KSI-IAM-02: Identity and Access Management

- **Validation ID:** `KSI-IAM-02`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No users found — identity model appears empty  
- **CLI Command:** `aws iam list-mfa-devices --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261459  

---

## ❌ KSI-IAM-02: Identity and Access Management

- **Validation ID:** `KSI-IAM-02`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ Unexpected output format  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261461  

---

## ❌ KSI-IAM-02: Identity and Access Management

- **Validation ID:** `KSI-IAM-02`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No users found — identity model appears empty  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261463  

---

## ❌ KSI-IAM-03: Identity and Access Management

- **Validation ID:** `KSI-IAM-03`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM roles found — cannot verify role granularity for service accounts  
- **CLI Command:** `aws iam list-instance-profiles --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261688  

---

## ❌ KSI-IAM-03: Identity and Access Management

- **Validation ID:** `KSI-IAM-03`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ No IAM roles found — cannot verify role granularity for service accounts  
- **CLI Command:** `aws sts get-caller-identity --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261690  

---

## ❌ KSI-IAM-03: Identity and Access Management

- **Validation ID:** `KSI-IAM-03`  
- **KSI Family:** Identity and Access Management  
- **Assertion Reason:** ❌ Unexpected output format  
- **CLI Command:** `aws iam list-service-linked-roles --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261691  

---

## ❌ KSI-MLA-01: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-01`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No CloudWatch log groups found — SIEM visibility not verifiable  
- **CLI Command:** `aws cloudtrail describe-trails --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261767  

---

## ❌ KSI-MLA-01: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-01`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ Unexpected output format  
- **CLI Command:** `aws config describe-configuration-recorders --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261773  

---

## ❌ KSI-MLA-01: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-01`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ Unexpected output format  
- **CLI Command:** `aws s3api get-bucket-logging --bucket cloudtrail-logs --output json`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261775  

---

## ❌ KSI-MLA-01: Monitoring, Logging, and Auditing

- **Validation ID:** `KSI-MLA-01`  
- **KSI Family:** Monitoring, Logging, and Auditing  
- **Assertion Reason:** ❌ No CloudWatch log groups found — SIEM visibility not verifiable  
- **CLI Command:** `REDACTED_FOR_SECURITY`  
- **Interpretation:** ⚠️ No evidence path specified.  
- **Timestamp:** 2025-06-05T23:49:48.261777  

---

