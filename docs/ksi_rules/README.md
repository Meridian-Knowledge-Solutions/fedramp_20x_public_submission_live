# KSI Documentation Index

This directory contains documentation for all Key Security Indicators (KSIs).

## Change Management

- [PASS] [KSI-CMT-01](KSI-CMT-01.md): Establish and maintain configuration baselines
- [PASS] [KSI-CMT-02](KSI-CMT-02.md): Execute changes through redeployment of version controlled immutable resources rather than direct modification wherever possible
- [PASS] [KSI-CMT-03](KSI-CMT-03.md): Implement automated testing and validation of changes prior to deployment
- [PASS] [KSI-CMT-04](KSI-CMT-04.md): Have a documented change management procedure
- [PASS] [KSI-CMT-05](KSI-CMT-05.md): Evaluate the risk and potential impact of any change

## Cloud Native Architecture

- [PASS] [KSI-CNA-01](KSI-CNA-01.md): Configure ALL information resources to limit inbound and outbound traffic
- [PASS] [KSI-CNA-02](KSI-CNA-02.md): Design systems to minimize the attack surface and minimize lateral movement if compromised
- [PASS] [KSI-CNA-03](KSI-CNA-03.md): Use logical networking for traffic flow controls
- [PASS] [KSI-CNA-04](KSI-CNA-04.md): Use immutable infrastructure patterns
- [PASS] [KSI-CNA-05](KSI-CNA-05.md): Have denial of service protection
- [PASS] [KSI-CNA-06](KSI-CNA-06.md): Design for high availability and recovery
- [PASS] [KSI-CNA-07](KSI-CNA-07.md): Follow AWS best practices

## Cybersecurity Education

- [PASS] [KSI-CED-01](KSI-CED-01.md): Ensure all employees receive security awareness training
- [PASS] [KSI-CED-02](KSI-CED-02.md): Require role-specific training for high risk roles, including at least roles with privileged access

## Identity and Access Management

- [PASS] [KSI-IAM-01](KSI-IAM-01.md): Enforce phishing-resistant MFA for all user authentication
- [PASS] [KSI-IAM-02](KSI-IAM-02.md): Use secure passwordless methods for user authentication and authorization when feasible, otherwise enforce strong passwords with MFA
- [PASS] [KSI-IAM-03](KSI-IAM-03.md): Enforce appropriately secure authentication methods for non-user accounts and services
- [PASS] [KSI-IAM-04](KSI-IAM-04.md): Use a least-privileged, role and attribute-based, and just-in-time security authorization model for all user and non-user accounts and services
- [PASS] [KSI-IAM-05](KSI-IAM-05.md): Apply zero trust design principles
- [PASS] [KSI-IAM-06](KSI-IAM-06.md): Automatically disable or otherwise secure accounts with privileged access in response to suspicious activity

## Incident Reporting

- [PASS] [KSI-INR-01](KSI-INR-01.md): Report incidents according to FedRAMP requirements and cloud service provider policies
- [PASS] [KSI-INR-02](KSI-INR-02.md): Maintain a log of incidents and periodically review past incidents for patterns or vulnerabilities
- [PASS] [KSI-INR-03](KSI-INR-03.md): Generate after action reports and regularly incorporate lessons learned into operations with automated incident tracking

## Monitoring, Logging, and Auditing

- [PASS] [KSI-MLA-01](KSI-MLA-01.md): Operate a SIEM or similar system for centralized, tamper-resistant logging
- [PASS] [KSI-MLA-02](KSI-MLA-02.md): Regularly review and audit logs
- [PASS] [KSI-MLA-03](KSI-MLA-03.md): Rapidly detect and remediate or mitigate vulnerabilities
- [PASS] [KSI-MLA-04](KSI-MLA-04.md): Perform authenticated vulnerability scanning on information resources
- [PASS] [KSI-MLA-05](KSI-MLA-05.md): Perform Infrastructure as Code and configuration evaluation and testing
- [PASS] [KSI-MLA-06](KSI-MLA-06.md): Centrally track and prioritize mitigation/remediation of identified vulnerabilities

## Policy and Inventory

- [PASS] [KSI-PIY-01](KSI-PIY-01.md): Have an up-to-date information resource inventory or code defining all deployed assets, software, and services
- [PASS] [KSI-PIY-02](KSI-PIY-02.md): Have policies outlining the security objectives of all information resources
- [PASS] [KSI-PIY-03](KSI-PIY-03.md): Maintain a vulnerability disclosure program
- [PASS] [KSI-PIY-04](KSI-PIY-04.md): Build security considerations into SDLC and align with CISA Secure By Design principles
- [PASS] [KSI-PIY-05](KSI-PIY-05.md): Document methods used to evaluate information resource implementations
- [PASS] [KSI-PIY-06](KSI-PIY-06.md): Have dedicated staff and budget for security with executive support
- [PASS] [KSI-PIY-07](KSI-PIY-07.md): Document risk management decisions for software supply chain security

## Recovery Planning

- [PASS] [KSI-RPL-01](KSI-RPL-01.md): Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)
- [PASS] [KSI-RPL-02](KSI-RPL-02.md): Develop and maintain a recovery plan that aligns with defined recovery objectives
- [PASS] [KSI-RPL-03](KSI-RPL-03.md): Perform system backups aligned with recovery objectives
- [PASS] [KSI-RPL-04](KSI-RPL-04.md): Regularly test the capability to recover from incidents and contingencies

## Service Configuration

- [PASS] [KSI-SVC-01](KSI-SVC-01.md): Harden and review network and system configurations
- [PASS] [KSI-SVC-02](KSI-SVC-02.md): Encrypt or otherwise secure network traffic
- [PASS] [KSI-SVC-03](KSI-SVC-03.md): Encrypt all federal and sensitive information at rest
- [PASS] [KSI-SVC-04](KSI-SVC-04.md): Manage configuration centrally
- [PASS] [KSI-SVC-05](KSI-SVC-05.md): Enforce system and information resource integrity through cryptographic means
- [PASS] [KSI-SVC-06](KSI-SVC-06.md): Use automated key management systems to manage, protect, and regularly rotate digital keys and certificates
- [PASS] [KSI-SVC-07](KSI-SVC-07.md): Use consistent, risk-informed approach for applying security patches

## Third-Party Information Resources

- [PASS] [KSI-TPR-01](KSI-TPR-01.md): Identify all third-party information resources
- [PASS] [KSI-TPR-02](KSI-TPR-02.md): Regularly confirm services handling federal information are FedRAMP authorized and securely configured
- [PASS] [KSI-TPR-03](KSI-TPR-03.md): Identify and prioritize mitigation of potential supply chain risks
- [PASS] [KSI-TPR-04](KSI-TPR-04.md): Monitor third party software for upstream vulnerabilities with contractual notification or active monitoring

## Summary

- **Total KSIs:** 51
- **Passing:** 51
- **Failing:** 0
- **Not Tested:** 0

---
*Generated 2025-07-12 02:43 UTC*