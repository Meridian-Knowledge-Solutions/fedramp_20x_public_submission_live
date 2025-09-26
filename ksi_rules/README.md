# KSI Documentation Index

This directory contains documentation for all Key Security Indicators (KSIs).

## Change Management

- [PASS] [KSI-CMT-01](KSI-CMT-01.md): Log and monitor system modifications
- [PASS] [KSI-CMT-02](KSI-CMT-02.md): Execute changes through redeployment of version controlled immutable resources rather than direct modification wherever possible
- [PASS] [KSI-CMT-03](KSI-CMT-03.md): Implement automated testing and validation of changes prior to deployment
- [PASS] [KSI-CMT-04](KSI-CMT-04.md): Have a documented change management procedure
- [PASS] [KSI-CMT-05](KSI-CMT-05.md): Evaluate the risk and potential impact of any change

## Cloud Native Architecture

- [PASS] [KSI-CNA-01](KSI-CNA-01.md): Configure ALL information resources to limit inbound and outbound traffic
- [PASS] [KSI-CNA-02](KSI-CNA-02.md): Design systems to minimize the attack surface and minimize lateral movement if compromised
- [PASS] [KSI-CNA-03](KSI-CNA-03.md): Use logical networking and related capabilities to enforce traffic flow controls
- [PASS] [KSI-CNA-04](KSI-CNA-04.md): Use immutable infrastructure with strictly defined functionality and privileges by default.
- [PASS] [KSI-CNA-05](KSI-CNA-05.md): Have denial of service protection
- [PASS] [KSI-CNA-06](KSI-CNA-06.md): Design systems for high availability and rapid recovery
- [PASS] [KSI-CNA-07](KSI-CNA-07.md): Ensure cloud-native information resources are implemented based on host provider's best practices and documented guidance

## Cybersecurity Education

- [PASS] [KSI-CED-01](KSI-CED-01.md): Ensure all employees receive security awareness training
- [PASS] [KSI-CED-02](KSI-CED-02.md): Require role-specific training for high risk roles, including at least roles with privileged access
- [PASS] [KSI-CED-03](KSI-CED-03.md): Require role-specific training for development and engineering staff covering best practices for delivering secure software

## Identity and Access Management

- [FAIL] [KSI-IAM-01](KSI-IAM-01.md): Enforce multi-factor authentication (MFA) using methods that are difficult to intercept or impersonate (phishing-resistant MFA) for all user authentication
- [PASS] [KSI-IAM-02](KSI-IAM-02.md): Use secure passwordless methods for user authentication and authorization when feasible, otherwise enforce strong passwords with MFA
- [PASS] [KSI-IAM-03](KSI-IAM-03.md): Enforce appropriately secure authentication methods for non-user accounts and services
- [PASS] [KSI-IAM-04](KSI-IAM-04.md): Use a least-privileged, role and attribute-based, and just-in-time security authorization model for all user and non-user accounts and services
- [PASS] [KSI-IAM-05](KSI-IAM-05.md): Apply zero trust design principles
- [PASS] [KSI-IAM-06](KSI-IAM-06.md): Automatically disable or otherwise secure accounts with privileged access in response to suspicious activity
- [PASS] [KSI-IAM-07](KSI-IAM-07.md): Securely manage the lifecycle and privileges of all accounts, roles, and groups

## Incident Reporting

- [PASS] [KSI-INR-01](KSI-INR-01.md): Document, report, and analyze security incidents to ensure regulatory compliance and continuous security improvement
- [PASS] [KSI-INR-02](KSI-INR-02.md): Maintain a log of incidents and periodically review past incidents for patterns or vulnerabilities
- [PASS] [KSI-INR-03](KSI-INR-03.md): Generate after action reports and regularly incorporate lessons learned into operations

## Monitoring, Logging, and Auditing

- [PASS] [KSI-MLA-01](KSI-MLA-01.md): Operate a Security Information and Event Management (SIEM) or similar system(s) for centralized, tamper-resistant logging of events, activities, and changes
- [PASS] [KSI-MLA-02](KSI-MLA-02.md): Regularly review and audit logs
- [PASS] [KSI-MLA-03](KSI-MLA-03.md): Rapidly detect and remediate or mitigate vulnerabilities
- [PASS] [KSI-MLA-05](KSI-MLA-05.md): Perform Infrastructure as Code and configuration evaluation and testing
- [PASS] [KSI-MLA-07](KSI-MLA-07.md): Maintain a list of information resources and event types that will be monitored, logged, and audited
- [PASS] [KSI-MLA-08](KSI-MLA-08.md): Use a least-privileged, role and attribute-based, and just-in-time access authorization model for access to log data

## Policy and Inventory

- [PASS] [KSI-PIY-01](KSI-PIY-01.md): Establish and maintain complete inventories of all information resources
- [PASS] [KSI-PIY-02](KSI-PIY-02.md): Establish and maintain organization-wide information security and technology policies
- [PASS] [KSI-PIY-03](KSI-PIY-03.md): Maintain a vulnerability disclosure program
- [PASS] [KSI-PIY-04](KSI-PIY-04.md): Build security and privacy considerations into the Software Development Lifecycle and align with CISA Secure By Design principles
- [PASS] [KSI-PIY-05](KSI-PIY-05.md): Document methods used to evaluate information resource implementations
- [FAIL] [KSI-PIY-06](KSI-PIY-06.md): Have staff and budget for security commensurate with the size, complexity, scope, executive priorities, and risk of the service offering that demonstrates commitment to delivering a secure service
- [PASS] [KSI-PIY-07](KSI-PIY-07.md): Document risk management decisions for software supply chain security

## Recovery Planning

- [PASS] [KSI-RPL-01](KSI-RPL-01.md): Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)
- [PASS] [KSI-RPL-02](KSI-RPL-02.md): Develop and maintain a recovery plan that aligns with defined recovery objectives
- [PASS] [KSI-RPL-03](KSI-RPL-03.md): Perform system backups aligned with recovery objectives
- [PASS] [KSI-RPL-04](KSI-RPL-04.md): Regularly test the capability to recover from incidents and contingencies

## Service Configuration

- [PASS] [KSI-SVC-01](KSI-SVC-01.md): Harden and review network and system configurations
- [PASS] [KSI-SVC-02](KSI-SVC-02.md): Encrypt or secure network traffic
- [PASS] [KSI-SVC-03](KSI-SVC-03.md): Encrypt all federal and sensitive information at rest
- [PASS] [KSI-SVC-04](KSI-SVC-04.md): Manage configuration centrally
- [PASS] [KSI-SVC-05](KSI-SVC-05.md): Continuously verify information resource integrity
- [PASS] [KSI-SVC-06](KSI-SVC-06.md): Use automated key management systems to manage, protect, and regularly rotate digital keys and certificates
- [PASS] [KSI-SVC-07](KSI-SVC-07.md): Use a consistent, risk-informed approach for applying security patches
- [PASS] [KSI-SVC-08](KSI-SVC-08.md): Ensure that changes do not introduce or leave behind residual elements that could negatively affect confidentiality, integrity, or availability
- [PASS] [KSI-SVC-09](KSI-SVC-09.md): Use mechanisms that continuously validate the authenticity and integrity of communications between information resources
- [PASS] [KSI-SVC-10](KSI-SVC-10.md): Remove unwanted information promptly, including from backups if appropriate

## Third-Party Information Resources

- [PASS] [KSI-TPR-01](KSI-TPR-01.md): Identify all third-party information resources
- [PASS] [KSI-TPR-03](KSI-TPR-03.md): Identify and prioritize mitigation of potential supply chain risks
- [PASS] [KSI-TPR-04](KSI-TPR-04.md): Monitor third party software for upstream vulnerabilities

## Summary

- **Total KSIs:** 55
- **Passing:** 53
- **Failing:** 2
- **Not Tested:** 0

---
*Generated 2025-09-26 19:15 UTC*