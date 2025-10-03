# KSI Documentation Index

This directory contains documentation for all Key Security Indicators (KSIs).

## Change Management

- [PASS] [KSI-CMT-01](KSI-CMT-01.md): Document a change management policy for all system modifications
- [PASS] [KSI-CMT-02](KSI-CMT-02.md): Use self-service templates and image repositories for provisioning
- [PASS] [KSI-CMT-03](KSI-CMT-03.md): Use CI/CD pipelines for deploying changes
- [FAIL] [KSI-CMT-04](KSI-CMT-04.md): Have a documented change management procedure
- [FAIL] [KSI-CMT-05](KSI-CMT-05.md): Analyze security impact of changes before implementation

## Cloud Native Architecture

- [PASS] [KSI-CNA-01](KSI-CNA-01.md): Implement DDoS protection and defense-in-depth network security
- [PASS] [KSI-CNA-02](KSI-CNA-02.md): Segment network and compute resources into security zones
- [PASS] [KSI-CNA-03](KSI-CNA-03.md): Restrict public network accessibility except through a limited number of managed access points
- [PASS] [KSI-CNA-04](KSI-CNA-04.md): Clearly define and deploy security controls as code to enforce the principle of least functionality
- [PASS] [KSI-CNA-05](KSI-CNA-05.md): Protect against denial of service attacks and unwanted spam
- [PASS] [KSI-CNA-06](KSI-CNA-06.md): Deploy highly available components and services
- [PASS] [KSI-CNA-07](KSI-CNA-07.md): Maximize use of managed services and cloud resources
- [PASS] [KSI-CNA-08](KSI-CNA-08.md): Use automated services to persistently assess the security posture of all services and automatically enforce secure operations

## Cybersecurity Education

- [PASS] [KSI-CED-01](KSI-CED-01.md): Provide role-based security training for personnel
- [PASS] [KSI-CED-02](KSI-CED-02.md): Provide specialized security training for privileged users
- [PASS] [KSI-CED-03](KSI-CED-03.md): Provide security awareness training on risks from social engineering and other attacks

## Identity and Access Management

- [PASS] [KSI-IAM-01](KSI-IAM-01.md): Enforce multi-factor authentication (MFA) using methods that are difficult to intercept or impersonate (phishing-resistant MFA) for all user authentication
- [PASS] [KSI-IAM-02](KSI-IAM-02.md): Implement enterprise-wide identity federation
- [PASS] [KSI-IAM-03](KSI-IAM-03.md): Implement least privilege access via role-based access control policies
- [PASS] [KSI-IAM-04](KSI-IAM-04.md): Clearly define user roles and implement user-to-role mapping
- [PASS] [KSI-IAM-05](KSI-IAM-05.md): Separate duties between users
- [PASS] [KSI-IAM-06](KSI-IAM-06.md): Implement fine-grained automated actions on security events related to authentication and access control
- [PASS] [KSI-IAM-07](KSI-IAM-07.md): Implement a consistent identity management process

## Incident Reporting

- [PASS] [KSI-INR-01](KSI-INR-01.md): Document incident handling procedures
- [PASS] [KSI-INR-02](KSI-INR-02.md): Establish an insider threat program
- [PASS] [KSI-INR-03](KSI-INR-03.md): Implement automated incident response procedures

## Monitoring, Logging, and Auditing

- [PASS] [KSI-MLA-01](KSI-MLA-01.md): Implement end-to-end logging to capture security events
- [PASS] [KSI-MLA-02](KSI-MLA-02.md): Regularly review and audit logs
- [PASS] [KSI-MLA-03](KSI-MLA-03.md): Rapidly detect and remediate or mitigate vulnerabilities
- [PASS] [KSI-MLA-05](KSI-MLA-05.md): Use change management tools to enforce, track and report configuration changes
- [PASS] [KSI-MLA-07](KSI-MLA-07.md): Use log aggregation services that accept logs from CSO-provided services
- [PASS] [KSI-MLA-08](KSI-MLA-08.md): Protect audit logs to support after-the-fact investigations

## Policy and Inventory

- [PASS] [KSI-PIY-01](KSI-PIY-01.md): Maintain an inventory of authorized users
- [PASS] [KSI-PIY-02](KSI-PIY-02.md): Maintain an inventory of all software installed on systems
- [PASS] [KSI-PIY-03](KSI-PIY-03.md): Define baselines for approved hardware, software, and firmware components
- [PASS] [KSI-PIY-04](KSI-PIY-04.md): Maintain an inventory of authorized software
- [PASS] [KSI-PIY-05](KSI-PIY-05.md): Maintain a data protection policy that addresses data retention requirements
- [PASS] [KSI-PIY-06](KSI-PIY-06.md): Have dedicated security staff and budget with executive support
- [PASS] [KSI-PIY-07](KSI-PIY-07.md): Document the system security policy

## Recovery Planning

- [PASS] [KSI-RPL-01](KSI-RPL-01.md): Establish a recovery time objective (RTO) and recovery point objective (RPO) for the system
- [PASS] [KSI-RPL-02](KSI-RPL-02.md): Document system recovery procedures
- [PASS] [KSI-RPL-03](KSI-RPL-03.md): Back up information regularly per the recovery point objective
- [PASS] [KSI-RPL-04](KSI-RPL-04.md): Test recovery procedures regularly

## Service Configuration

- [PASS] [KSI-SVC-01](KSI-SVC-01.md): Maintain hardened system images and configurations
- [PASS] [KSI-SVC-02](KSI-SVC-02.md): Use encryption in transit with TLS 1.2 or higher
- [PASS] [KSI-SVC-03](KSI-SVC-03.md): Encrypt data at rest
- [PASS] [KSI-SVC-04](KSI-SVC-04.md): Use configuration management systems to manage cloud services and apply configuration as code to CSO-provided cloud services
- [PASS] [KSI-SVC-05](KSI-SVC-05.md): Use logging and monitoring to detect abnormal changes to configuration
- [PASS] [KSI-SVC-06](KSI-SVC-06.md): Use centralized key management services
- [PASS] [KSI-SVC-07](KSI-SVC-07.md): Perform regularly scheduled scans for vulnerabilities and apply patches promptly
- [PASS] [KSI-SVC-08](KSI-SVC-08.md): Use infrastructure as code to apply controls to the provisioning and management of resources
- [PASS] [KSI-SVC-09](KSI-SVC-09.md): Use TLS 1.2 or higher versions of secure protocols
- [PASS] [KSI-SVC-10](KSI-SVC-10.md): Perform regularly scheduled backups

## Third-Party Information Resources

- [PASS] [KSI-TPR-01](KSI-TPR-01.md): Document the cloud service provider (CSP) in the system security policy
- [PASS] [KSI-TPR-03](KSI-TPR-03.md): Document all third-party services used in the system security policy
- [PASS] [KSI-TPR-04](KSI-TPR-04.md): Conduct vulnerability scans for applications and operating systems

## Summary

- **Total KSIs:** 56
- **Passing:** 54
- **Failing:** 2
- **Not Tested:** 0

---
*Generated 2025-10-03 19:13 UTC*