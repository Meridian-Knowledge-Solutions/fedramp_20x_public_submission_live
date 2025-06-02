# ❌ Failed KSI Validation Report

Last Updated: `2025-06-02T06:35:47.707496Z`

## ❌ KSI-CMT-03: 
**Validation ID:** `KSI-CMT-03`  
**Reason:** ❌ No rule defined for this KSI  
**CLI Command:** `aws codebuild batch-get-projects`  

---

## ❌ KSI-IAM-06: 
**Validation ID:** `KSI-IAM-06`  
**Reason:** ❌ No password policy found  
**CLI Command:** `aws iam get-account-password-policy`  

---

## ❌ KSI-SVC-07: 
**Validation ID:** `KSI-SVC-07`  
**Reason:** ❌ No patch groups found  
**CLI Command:** `aws ssm describe-patch-groups`  

---

## ❌ KSI-CED-01: 
**Validation ID:** `KSI-CED-01`  
**Reason:** ❌ No SSO users found  
**CLI Command:** `aws sso list-users --instance-arn arn:aws:sso:::instance/ssoins-1234567890abcdef`  

---

## ❌ KSI-CMT-01: 
**Validation ID:** `KSI-CMT-01`  
**Reason:** ❌ No rule defined for this KSI  
**CLI Command:** `AttributeValue=Modify"`  

---

## ❌ KSI-MLA-02: 
**Validation ID:** `KSI-MLA-02`  
**Reason:** ❌ No metric filters found  
**CLI Command:** `aws logs describe-metric-filters`  

---

## ❌ KSI-PIY-03: 
**Validation ID:** `KSI-PIY-03`  
**Reason:** ❌ No Trusted Advisor checks found  
**CLI Command:** `aws support describe-trusted-advisor-checks --language en`  

---

## ❌ KSI-SVC-01: 
**Validation ID:** `KSI-SVC-01`  
**Reason:** ❌ No web ACLs found  
**CLI Command:** `aws wafv2 list-web-acls`  

---

## ❌ KSI-CNA-07: 
**Validation ID:** `KSI-CNA-07`  
**Reason:** ❌ No Well-Architected workloads found  
**CLI Command:** `aws wellarchitected list-workloads`  

---

## ❌ KSI-PIY-06: 
**Validation ID:** `KSI-PIY-06`  
**Reason:** ❌ No organization structure found  
**CLI Command:** `aws organizations describe-organization`  

---

## ❌ KSI-CMT-04: 
**Validation ID:** `KSI-CMT-04`  
**Reason:** ❌ No rule defined for this KSI  
**CLI Command:** `aws ssm list-documents`  

---

## ❌ KSI-MLA-06: 
**Validation ID:** `KSI-MLA-06`  
**Reason:** ❌ No vulnerabilities found  
**CLI Command:** `aws inspector2 list-vulnerabilities`  

---

## ❌ KSI-TPR-04: 
**Validation ID:** `KSI-TPR-04`  
**Reason:** ❌ No Inspector findings found  
**CLI Command:** `aws inspector2 list-findings`  

---

## ❌ KSI-PIY-05: 
**Validation ID:** `KSI-PIY-05`  
**Reason:** ❌ No compliance rules found  
**CLI Command:** `aws config describe-compliance-by-config-rule`  

---

## ❌ KSI-RPL-04: 
**Validation ID:** `KSI-RPL-04`  
**Reason:** ❌ No restore jobs found  
**CLI Command:** `aws backup list-restore-jobs`  

---

## ❌ KSI-INR-03: 
**Validation ID:** `KSI-INR-03`  
**Reason:** ❌ No Inspector findings found  
**CLI Command:** `aws inspector list-findings`  

---

## ❌ KSI-MLA-03: 
**Validation ID:** `KSI-MLA-03`  
**Reason:** ❌ No subscription filters found  
**CLI Command:** `aws logs describe-subscription-filters`  

---

## ❌ KSI-SVC-04: 
**Validation ID:** `KSI-SVC-04`  
**Reason:** ❌ No configuration recorder statuses found  
**CLI Command:** `aws config describe-configuration-recorder-status`  

---

## ❌ KSI-PIY-01: 
**Validation ID:** `KSI-PIY-01`  
**Reason:** ❌ No discovered resources  
**CLI Command:** `aws config list-discovered-resources --resource-type AWS::EC2::Instance`  

---

## ❌ KSI-PIY-04: 
**Validation ID:** `KSI-PIY-04`  
**Reason:** ❌ No CodeCommit repositories found  
**CLI Command:** `aws codecommit list-repositories`  

---

## ❌ KSI-CNA-04: 
**Validation ID:** `KSI-CNA-04`  
**Reason:** ❌ No EC2 reservations found  
**CLI Command:** `aws ec2 describe-instances`  

---

## ❌ KSI-CED-02: 
**Validation ID:** `KSI-CED-02`  
**Reason:** ❌ No IAM groups found  
**CLI Command:** `aws iam list-groups`  

---

## ❌ KSI-TPR-01: 
**Validation ID:** `KSI-TPR-01`  
**Reason:** ❌ No CloudFormation stack resources found  
**CLI Command:** `aws config list-discovered-resources --resource-type AWS::CloudFormation::Stack`  

---

## ❌ KSI-CMT-02: 
**Validation ID:** `KSI-CMT-02`  
**Reason:** ❌ No rule defined for this KSI  
**CLI Command:** `aws s3api list-object-versions --bucket your-terraform-state-bucket`  

---

## ❌ KSI-TPR-02: 
**Validation ID:** `KSI-TPR-02`  
**Reason:** ❌ No SecurityHub findings for FedRAMP Moderate  
**CLI Command:** `aws securityhub get-findings --filters ProductArn={Value=arn:aws:securityhub:::product/aws/fedramp-moderate;Comparison=EQUALS}`  

---

## ❌ KSI-SVC-05: 
**Validation ID:** `KSI-SVC-05`  
**Reason:** ❌ No DRT access role found  
**CLI Command:** `aws shield describe-drt-access`  

---

## ❌ KSI-RPL-02: 
**Validation ID:** `KSI-RPL-02`  
**Reason:** ❌ No recovery points found  
**CLI Command:** `aws backup list-recovery-points-by-backup-vault --backup-vault-name default`  

---

## ❌ KSI-MLA-05: 
**Validation ID:** `KSI-MLA-05`  
**Reason:** ❌ No config rules found  
**CLI Command:** `aws config describe-config-rules`  

---

## ❌ KSI-MLA-04: 
**Validation ID:** `KSI-MLA-04`  
**Reason:** ❌ No destinations found  
**CLI Command:** `aws logs describe-destinations`  

---

## ❌ KSI-SVC-06: 
**Validation ID:** `KSI-SVC-06`  
**Reason:** ❌ No key rotation status  
**CLI Command:** `aws kms list-key-rotation-status`  

---

## ❌ KSI-TPR-03: 
**Validation ID:** `KSI-TPR-03`  
**Reason:** ❌ SecurityHub hub not described  
**CLI Command:** `aws securityhub describe-hub`  

---

## ❌ KSI-SVC-02: 
**Validation ID:** `KSI-SVC-02`  
**Reason:** ❌ No VPN connections found  
**CLI Command:** `aws ec2 describe-vpn-connections`  

---

## ❌ KSI-PIY-07: 
**Validation ID:** `KSI-PIY-07`  
**Reason:** ❌ No document permissions found  
**CLI Command:** `aws ssm describe-document-permissions`  

---

## ❌ KSI-INR-01: 
**Validation ID:** `KSI-INR-01`  
**Reason:** ❌ No SecurityHub insights found  
**CLI Command:** `aws securityhub list-insights`  

---

## ❌ KSI-CMT-05: 
**Validation ID:** `KSI-CMT-05`  
**Reason:** ❌ No rule defined for this KSI  
**CLI Command:** `aws cloudwatch describe-alarms`  

---

