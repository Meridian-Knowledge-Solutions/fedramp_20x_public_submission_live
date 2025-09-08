#!/usr/bin/env python3
"""
FedRAMP KSI Evaluation Logic Explainer - COMPLETE EDITION
=========================================================
This tool explains the evaluation logic for ALL 51 Key Security Implementation (KSI) 
controls in human-readable terms for 3PAO assessors and FedRAMP stakeholders.

Based on: Meridian FedRAMP 20x Phase One SRTM v06.24.2025
Updated: June 27, 2025
"""

def explain_ksi_logic():
    """
    Explains the evaluation logic for ALL KSIs in the assessment script.
    Each KSI follows a pattern: Parse inputs → Check evidence → Score → Return result
    """
    
    ksi_explanations = {
        # ===== CLOUD NETWORKING & ARCHITECTURE (CNA) - 7 KSIs =====
        "KSI_CNA_01": {
            "title": "Configure ALL information resources to limit inbound and outbound traffic",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF Security Groups exist AND most are restrictive (not 0.0.0.0/0 for SSH/RDP):
                ✅ Award points for ingress controls
            IF Security Groups have restrictive egress (empty rules or specific targets):
                ✅ Award points for egress controls  
            IF Network ACLs have custom rules (not just defaults):
                ✅ Award bonus points for subnet-level controls
            IF NAT Gateways + VPC Endpoints exist:
                ✅ Award points for controlled routing
            IF WAF configurations exist:
                ✅ Award points for application-layer protection
            ELSE:
                ❌ Insufficient traffic controls
            """,
            "passing_criteria": "≥80% restrictive security groups + some egress controls + network segmentation",
            "cli_commands": [
                "aws ec2 describe-security-groups --output json",
                "aws ec2 describe-network-acls --output json", 
                "aws ec2 describe-route-tables --output json",
                "aws ec2 describe-nat-gateways --output json",
                "aws ec2 describe-vpc-endpoints --output json",
                "aws wafv2 list-web-acls --scope REGIONAL --output json",
                "aws elbv2 describe-load-balancers --output json",
                "aws logs describe-log-groups --log-group-name-prefix /aws/vpc/flowlogs --output json"
            ]
        },
        
        "KSI_CNA_02": {
            "title": "Design systems to minimize attack surface and lateral movement",
            "evidence_type": "AWS CLI Commands", 
            "logic": """
            IF Subnets exist AND ≥70% are private:
                ✅ Award points for attack surface minimization
            IF Multi-AZ deployment (≥2 availability zones):
                ✅ Award points for segmentation
            IF Security Groups use specific rules (not wide open):
                ✅ Award points for micro-segmentation
            IF Instances in private subnets AND databases not public:
                ✅ Award points for workload isolation
            IF Load balancers are internal vs internet-facing where appropriate:
                ✅ Award points for controlled exposure
            ELSE:
                ❌ High attack surface
            """,
            "passing_criteria": "Private subnet placement + multi-AZ + restrictive security groups + database isolation",
            "cli_commands": [
                "aws ec2 describe-subnets --output json",
                "aws ec2 describe-security-groups --output json",
                "aws ec2 describe-instances --output json",
                "aws ec2 describe-network-acls --output json",
                "aws elbv2 describe-load-balancers --output json",
                "aws lambda list-functions --output json",
                "aws rds describe-db-instances --output json"
            ]
        },

        "KSI_CNA_03": {
            "title": "Use logical networking for traffic flow controls",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF Route Tables have intentional routes (local + IGW/NAT):
                ✅ Award points for routing infrastructure
            IF Network ACLs have custom rules (specific ports/CIDRs):
                ✅ Award points for access control
            IF VPC Endpoints exist:
                ✅ Award points for private service access
            IF Transit Gateway OR VPC Peering configured:
                ✅ Award points for logical networking
            IF Single VPC setup:
                ✅ Award full points (appropriate design)
            IF Multi-VPC but no Transit Gateway:
                ⚠️ Consider centralized control
            """,
            "passing_criteria": "Functional routing + access controls + appropriate architecture",
            "cli_commands": [
                "aws ec2 describe-route-tables --output json",
                "aws ec2 describe-network-acls --output json", 
                "aws ec2 describe-vpc-endpoints --output json",
                "aws ec2 describe-transit-gateways --output json",
                "aws ec2 describe-vpc-peering-connections --output json",
                "aws elbv2 describe-load-balancers --output json",
                "aws route53 list-hosted-zones --output json",
                "aws ec2 describe-nat-gateways --output json",
                "aws logs describe-log-groups --log-group-name-prefix /aws/vpc/flowlogs --output json"
            ]
        },

        "KSI_CNA_04": {
            "title": "Use immutable infrastructure patterns",
            "evidence_type": "AWS CLI Commands + Evidence Files",
            "logic": """
            IF CloudFormation stacks exist AND successful:
                ✅ Award points for IaC foundation
            IF Instances have Terraform patterns (naming, tags):
                ✅ Award points for Infrastructure as Code
            IF Launch Templates OR Auto Scaling Groups exist:
                ✅ Award points for standardized deployment
            IF Lambda functions exist:
                ✅ Award points for serverless (inherently immutable)
            IF Custom AMIs exist with versioning:
                ✅ Award points for immutable base images
            IF S3 buckets contain terraform state patterns:
                ✅ Award points for mature IaC
            ELSE:
                ❌ No immutable patterns detected
            """,
            "passing_criteria": "CloudFormation + Terraform patterns OR serverless + standardized deployment",
            "cli_commands": [
                "aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags,LaunchTime,ImageId]' --output json",
                "aws ec2 describe-launch-templates --output json",
                "aws autoscaling describe-auto-scaling-groups --output json",
                "aws ec2 describe-images --owners self --output json",
                "aws lambda list-functions --output json",
                "aws s3api list-buckets --query 'Buckets[?contains(Name, terraform) || contains(Name, tfstate)]' --output json",
                "aws dynamodb list-tables --output json",
                "aws codebuild list-projects --output json",
                "aws ssm describe-parameters --output json"
            ]
        },

        "KSI_CNA_05": {
            "title": "Have denial of service protection",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF AWS Shield Advanced subscription exists:
                ✅ Award premium protection points
            ELSE:
                ✅ AWS Shield Standard (automatic baseline)
            IF Regional WAF Web ACLs exist:
                ✅ Award application protection points
            IF CloudFront distributions exist:
                ✅ Award edge-based protection points
            IF Multi-AZ Load Balancers exist:
                ✅ Award service resilience points
            IF Route 53 hosted zones exist:
                ✅ Award DNS protection points
            IF Auto Scaling Groups configured:
                ✅ Award capacity-based mitigation points
            """,
            "passing_criteria": "Shield Standard + Regional WAF + Multi-AZ ALB + Route 53",
            "cli_commands": [
                "aws wafv2 list-web-acls --scope REGIONAL --output json",
                "aws wafv2 list-web-acls --scope CLOUDFRONT --output json",
                "aws cloudfront list-distributions --output json",
                "aws elbv2 describe-load-balancers --output json",
                "aws autoscaling describe-auto-scaling-groups --output json",
                "aws route53 list-hosted-zones --output json",
                "aws cloudwatch describe-alarms --output json"
            ]
        },

        "KSI_CNA_06": {
            "title": "Design systems for high availability and rapid recovery",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF Subnets distributed across ≥2 availability zones:
                ✅ Award points for network-level HA
            IF RDS Multi-AZ deployments exist:
                ✅ Award points for database HA
            IF Load Balancers span multiple AZs:
                ✅ Award points for application-layer HA
            IF Auto Scaling Groups configured for multi-AZ:
                ✅ Award points for compute resilience
            IF Backup plans exist:
                ✅ Award points for recovery capability
            IF EBS snapshots exist:
                ✅ Award points for storage recovery
            IF S3 buckets configured for redundancy:
                ✅ Award points for storage HA
            """,
            "passing_criteria": "Multi-AZ distribution + database HA + backup strategy + load balancing",
            "cli_commands": [
                "aws ec2 describe-subnets --output json",
                "aws ec2 describe-availability-zones --output json",
                "aws rds describe-db-instances --output json",
                "aws elbv2 describe-load-balancers --output json",
                "aws autoscaling describe-auto-scaling-groups --output json",
                "aws backup list-backup-plans --output json",
                "aws ec2 describe-snapshots --owner-ids self --output json",
                "aws s3api list-buckets --output json",
                "aws route53 list-hosted-zones --output json"
            ]
        },

        "KSI_CNA_07": {
            "title": "Cloud-native best practices implementation",
            "evidence_type": "AWS CLI Commands + Evidence Files",
            "logic": """
            IF AWS Config rules exist for compliance monitoring:
                ✅ Award points for best practice enforcement
            IF CloudTrail logging is active:
                ✅ Award points for security best practices
            IF KMS keys exist for encryption:
                ✅ Award points for security best practices
            IF IAM configuration follows patterns:
                ✅ Award points for security best practices
            IF Organizations setup for governance:
                ✅ Award points for enterprise best practices
            IF Evidence files show AMI baseline strategy:
                ✅ Award points for cloud-native implementation
            """,
            "passing_criteria": "Config rules + CloudTrail + KMS + appropriate governance",
            "cli_commands": [
                "aws configservice describe-config-rules --output json",
                "aws cloudtrail describe-trails --output json",
                "aws cloudtrail get-trail-status --output json",
                "aws kms list-keys --output json",
                "aws iam get-account-summary --output json",
                "aws ec2 describe-instances --output json",
                "aws elbv2 describe-load-balancers --output json",
                "aws autoscaling describe-auto-scaling-groups --output json",
                "aws s3api list-buckets --output json",
                "aws cloudwatch describe-alarms --output json",
                "aws backup list-backup-plans --output json",
                "aws organizations describe-organization --output json"
            ]
        },

        # ===== SERVICES (SVC) - 7 KSIs =====
        "KSI_SVC_01": {
            "title": "Harden and review network and system configurations", 
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF Security Groups are mostly restrictive:
                ✅ Award network hardening points
            IF SSM instances under management:
                ✅ Award system management points
            IF Config rules active:
                ✅ Award compliance automation points
            IF GuardDuty detectors exist:
                ✅ Award threat detection points
            IF Organizations with ALL features:
                ✅ Award enterprise governance points
            IF WAF configured for application protection:
                ✅ Award application hardening points
            """,
            "passing_criteria": "Restrictive security groups + system management + compliance rules + threat detection",
            "cli_commands": [
                "aws ec2 describe-security-groups --output json",
                "aws ec2 describe-instances --output json",
                "aws ec2 describe-network-acls --output json",
                "aws config describe-config-rules --output json",
                "aws guardduty list-detectors --output json",
                "aws wafv2 list-web-acls --scope REGIONAL --output json",
                "aws ssm describe-patch-baselines --output json",
                "aws ssm describe-instance-information --output json",
                "aws inspector2 get-configuration --output json",
                "aws organizations describe-organization --output json"
            ]
        },

        "KSI_SVC_02": {
            "title": "Encrypt or otherwise secure network traffic",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF ACM certificates exist for TLS/SSL:
                ✅ Award network encryption points
            IF Load Balancers configured with SSL:
                ✅ Award HTTPS enforcement points
            IF VPC endpoints exist for private communications:
                ✅ Award private traffic points
            IF Security Groups restrict to HTTPS/TLS ports:
                ✅ Award secure protocol enforcement points
            """,
            "passing_criteria": "SSL/TLS certificates + HTTPS enforcement + secure protocols",
            "cli_commands": [
                "aws acm list-certificates --output json",
                "aws elbv2 describe-load-balancers --output json",
                "aws elbv2 describe-listeners --output json",
                "aws ec2 describe-vpc-endpoints --output json",
                "aws ec2 describe-security-groups --output json"
            ]
        },

        "KSI_SVC_03": {
            "title": "Encrypt all federal and sensitive information at rest",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF S3 buckets exist:
                ✅ Assume encrypted (validation needed)
            IF EBS volumes encrypted (BackupRetentionPeriod > 0):
                ✅ Award block storage encryption points
            IF RDS instances have StorageEncrypted=true:
                ✅ Award database encryption points
            IF KMS keys exist (especially customer-managed):
                ✅ Award key management points
            IF DynamoDB tables exist:
                ✅ Award NoSQL encryption points
            IF No storage resources:
                ✅ Nothing to encrypt (acceptable)
            """,
            "passing_criteria": "Encrypted EBS volumes OR encrypted RDS OR comprehensive encryption strategy",
            "cli_commands": [
                "aws s3api list-buckets --output json",
                "aws ec2 describe-volumes --output json",
                "aws rds describe-db-instances --output json",
                "aws rds describe-db-snapshots --owner-type self --output json",
                "aws dynamodb list-tables --output json",
                "aws elasticache describe-cache-clusters --output json",
                "aws redshift describe-clusters --output json",
                "aws efs describe-file-systems --output json",
                "aws backup list-backup-vaults --output json",
                "aws kms list-keys --output json"
            ]
        },

        "KSI_SVC_04": {
            "title": "Manage configuration centrally",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF Systems Manager Parameter Store has parameters:
                ✅ Award centralized configuration points
            IF AWS Config recorders active:
                ✅ Award configuration monitoring points
            IF CloudFormation stacks exist:
                ✅ Award IaC configuration points
            IF Secrets Manager secrets exist:
                ✅ Award secure configuration management points
            IF SSM documents exist for automation:
                ✅ Award workflow automation points
            """,
            "passing_criteria": "Parameter Store + Config + IaC + secure secrets management",
            "cli_commands": [
                "aws ssm describe-parameters --output json",
                "aws config describe-configuration-recorders --output json",
                "aws ssm list-documents --document-filter-list key=DocumentType,value=Command --output json",
                "aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json",
                "aws secretsmanager list-secrets --output json",
                "aws ssm describe-patch-baselines --output json",
                "aws config describe-config-rules --output json",
                "aws ssm describe-instance-information --output json",
                "aws servicecatalog search-products --output json",
                "aws organizations describe-organization --output json"
            ]
        },

        "KSI_SVC_05": {
            "title": "Enforce system and information resource integrity",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF CloudTrail log file validation enabled:
                ✅ Award tamper-evident logging points
            IF KMS keys available for integrity protection:
                ✅ Award cryptographic integrity points
            IF S3 bucket versioning enabled:
                ✅ Award object integrity points
            IF AWS Config tracking configuration changes:
                ✅ Award configuration integrity points
            IF CloudWatch alarms for integrity violations:
                ✅ Award integrity monitoring points
            """,
            "passing_criteria": "CloudTrail validation + KMS + versioning + Config tracking",
            "cli_commands": [
                "aws cloudtrail describe-trails --output json",
                "aws kms list-keys --output json",
                "aws kms list-aliases --output json",
                "aws s3api list-buckets --output json",
                "aws rds describe-db-instances --output json",
                "aws config describe-configuration-recorders --output json",
                "aws cloudwatch describe-alarms --output json",
                "aws sns list-topics --output json",
                "aws backup list-backup-vaults --output json",
                "aws organizations describe-organization --output json"
            ]
        },

        "KSI_SVC_06": {
            "title": "Use automated key management systems",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF KMS keys exist for automated key management:
                ✅ Award key management points
            IF ACM certificates exist for automated certificate lifecycle:
                ✅ Award certificate management points
            IF Secrets Manager configured for rotation:
                ✅ Award automated rotation points
            IF SecureString parameters in SSM:
                ✅ Award encrypted configuration points
            IF CloudFormation manages keys and certificates:
                ✅ Award IaC key management points
            """,
            "passing_criteria": "KMS + ACM + automated rotation + secure parameter management",
            "cli_commands": [
                "aws kms list-keys --output json",
                "aws acm list-certificates --output json",
                "aws kms list-aliases --output json",
                "aws ssm describe-parameters --parameter-filters Key=Type,Values=SecureString --output json",
                "aws secretsmanager list-secrets --output json",
                "aws iam list-server-certificates --output json",
                "aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --output json",
                "aws config describe-config-rules --output json",
                "aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=CreateKey --output json",
                "aws organizations describe-organization --output json"
            ]
        },

        "KSI_SVC_07": {
            "title": "Use consistent, risk-informed approach for security patches",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF SSM patch baselines exist:
                ✅ Award patch management points
            IF SSM agent coverage exists:
                ✅ Award automated patching points
            IF Patch groups configured:
                ✅ Award risk-informed segmentation points
            IF Maintenance windows defined:
                ✅ Award controlled deployment points
            IF Inspector scanning enabled:
                ✅ Award vulnerability-driven patching points
            """,
            "passing_criteria": "Patch baselines + SSM coverage + risk-informed scheduling + vulnerability scanning",
            "cli_commands": [
                "aws ssm describe-patch-baselines --output json",
                "aws ssm describe-instance-information --output json",
                "aws ssm describe-patch-groups --output json",
                "aws ssm list-documents --document-filter-list key=DocumentType,value=Command --output json",
                "aws ssm describe-maintenance-windows --output json",
                "aws inspector2 get-configuration --output json",
                "aws ecr describe-repositories --output json",
                "aws lambda list-layers --output json",
                "aws config describe-config-rules --output json",
                "aws organizations describe-organization --output json"
            ]
        },

        # ===== IDENTITY & ACCESS MANAGEMENT (IAM) - 6 KSIs =====
        "KSI_IAM_01": {
            "title": "Enforce phishing-resistant MFA for all user authentication",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF AWS Identity Center active:
                ✅ Award modern identity platform points
            IF ≥80% users via SCIM provisioning AND ≥80% Okta IDs:
                ✅ Award full federated MFA points (external IdP enforces MFA)
            ELIF Identity Center users from external IdP:
                ✅ Award partial federated MFA points
            ELIF Traditional IAM users with MFA devices:
                ✅ Award traditional MFA points
            ELSE:
                ❌ No MFA enforcement detected
            """,
            "passing_criteria": "Identity Center + external IdP (Okta) federation OR traditional MFA devices",
            "cli_commands": [
                "aws iam list-users --output json",
                "aws iam list-mfa-devices --output json",
                "aws sso-admin list-instances --output json",
                "aws identitystore list-users --identity-store-id <ID> --output json"
            ]
        },

        "KSI_IAM_02": {
            "title": "Use secure passwordless methods or strong passwords with MFA",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF SAML providers exist (federated authentication):
                ✅ Award passwordless authentication points
            IF Virtual MFA devices configured:
                ✅ Award MFA enforcement points
            IF Strong password policy exists:
                ✅ Award password security points
            IF STS temporary credentials in use:
                ✅ Award secure authentication method points
            """,
            "passing_criteria": "Federated authentication OR strong passwords + MFA",
            "cli_commands": [
                "aws iam list-saml-providers --output json",
                "aws iam list-virtual-mfa-devices --output json",
                "aws iam get-account-password-policy --output json",
                "aws iam list-users --output json",
                "aws sts get-caller-identity --output json"
            ]
        },

        "KSI_IAM_03": {
            "title": "Enforce secure authentication for non-user accounts and services",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF IAM roles exist for service authentication:
                ✅ Award secure service authentication points
            IF EC2 instances use instance profiles:
                ✅ Award secure EC2 authentication points
            IF Few long-term access keys exist:
                ✅ Award secure credential management points
            IF Service users minimize use of access keys:
                ✅ Award best practice points
            """,
            "passing_criteria": "IAM roles + instance profiles + minimal long-term keys",
            "cli_commands": [
                "aws iam list-roles --output json",
                "aws iam list-users --output json",
                "aws iam list-access-keys --output json",
                "aws ec2 describe-instances --query 'Reservations[*].Instances[*].IamInstanceProfile' --output json"
            ]
        },

        "KSI_IAM_04": {
            "title": "Use least-privileged, role-based, just-in-time authorization model",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF Identity Center active AND permission sets deployed:
                ✅ Award modern authorization points (highest score)
            IF SSO session detected (assumed-role with AWSReservedSSO):
                ✅ Award just-in-time access points
            IF More roles than users:
                ✅ Award role-based access points
            IF Low user count (≤5) AND low policy count:
                ✅ Award least privilege points
            IF ARN redacted but SSO configured:
                ✅ Infer SSO session from context
            """,
            "passing_criteria": "Identity Center permission sets + SSO sessions + role-based access",
            "cli_commands": [
                "aws sso-admin list-instances --output json",
                "aws sso-admin list-permission-sets --instance-arn <ARN> --output json",
                "aws iam list-roles --output json",
                "aws iam list-users --output json",
                "aws sts get-caller-identity --output json",
                "aws iam get-account-summary --output json"
            ]
        },

        "KSI_IAM_05": {
            "title": "Apply zero trust design principles",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF Identity Center for modern access patterns:
                ✅ Award zero trust identity points
            IF CloudTrail actively logging (continuous monitoring):
                ✅ Award continuous verification points
            IF Security Groups follow micro-segmentation:
                ✅ Award network zero trust points
            IF VPC endpoints for private communications:
                ✅ Award secure communications points
            IF MFA devices enforced:
                ✅ Award explicit verification points
            IF Temporary credentials in use:
                ✅ Award zero trust session points
            """,
            "passing_criteria": "Continuous monitoring + micro-segmentation + explicit verification + private communications",
            "cli_commands": [
                "aws sso-admin list-instances --output json",
                "aws cloudtrail describe-trails --output json",
                "aws cloudtrail get-trail-status --output json",
                "aws ec2 describe-security-groups --output json",
                "aws ec2 describe-vpc-endpoints --output json",
                "aws iam list-virtual-mfa-devices --output json",
                "aws sts get-caller-identity --output json"
            ]
        },

        "KSI_IAM_06": {
            "title": "Automatically disable accounts with privileged access on suspicious activity",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF EventBridge rules exist for automated responses:
                ✅ Award automation capability points
            IF GuardDuty detectors active for threat detection:
                ✅ Award threat detection points
            IF Security Hub configured for centralized findings:
                ✅ Award security orchestration points
            IF Lambda functions for automated responses:
                ✅ Award response automation points
            IF CloudWatch alarms for suspicious activity:
                ✅ Award monitoring points
            """,
            "passing_criteria": "EventBridge automation + GuardDuty + Security Hub + automated response functions",
            "cli_commands": [
                "aws events list-rules --output json",
                "aws guardduty list-detectors --output json",
                "aws securityhub describe-hub --output json",
                "aws sso-admin list-instances --output json",
                "aws config describe-config-rules --output json",
                "aws lambda list-functions --output json",
                "aws cloudwatch describe-alarms --output json"
            ]
        },

        # ===== MONITORING, LOGGING & ANALYSIS (MLA) - 6 KSIs =====
        "KSI_MLA_01": {
            "title": "Operate a SIEM or similar system for centralized, tamper-resistant logging",
            "evidence_type": "AWS CLI Commands + Cross-Account Data",
            "logic": """
            IF CloudTrail trails with LogFileValidationEnabled=true:
                ✅ Award tamper-resistant logging points
            IF CloudWatch log groups exist:
                ✅ Award centralized collection points
            IF CloudWatch alarms for log patterns:
                ✅ Award analysis and alerting points
            IF Config delivery channels to S3:
                ✅ Award compliance log delivery points
            IF Cross-account data available:
                ✅ Award enterprise governance bonus
            """,
            "passing_criteria": "CloudTrail validation + log groups + analysis capability",
            "cli_commands": [
                "aws cloudtrail describe-trails --output json",
                "aws cloudtrail get-trail-status --output json",
                "aws logs describe-log-groups --output json",
                "aws cloudwatch describe-alarms --output json",
                "aws config describe-delivery-channels --output json"
            ]
        },

        "KSI_MLA_02": {
            "title": "Review logs for anomalies and security events regularly",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF CloudWatch Insights queries configured:
                ✅ Award log analysis points
            IF CloudWatch alarms configured for security events:
                ✅ Award automated monitoring points
            IF EventBridge rules for log-based triggers:
                ✅ Award automated response points
            IF GuardDuty findings reviewed regularly:
                ✅ Award threat analysis points
            """,
            "passing_criteria": "Log analysis + automated monitoring + regular review processes",
            "cli_commands": [
                "aws logs describe-log-groups --output json",
                "aws cloudwatch describe-alarms --output json",
                "aws events list-rules --output json",
                "aws guardduty list-findings --output json"
            ]
        },

        "KSI_MLA_03": {
            "title": "Rapidly detect and remediate vulnerabilities",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF Security Hub standards enabled (≥1 active):
                ✅ Award detection foundation points
            IF Inspector EC2/ECR scanning enabled:
                ✅ Award automated scanning points
            IF Patch baselines exist:
                ✅ Award remediation points
            IF Lambda functions for security automation:
                ✅ Award response automation points
            IF CloudWatch alarms for security events:
                ✅ Award real-time detection points
            """,
            "passing_criteria": "Security Hub standards + Inspector scanning + remediation capability",
            "cli_commands": [
                "aws securityhub describe-hub --output json",
                "aws inspector2 get-configuration --output json",
                "aws ssm describe-patch-baselines --output json",
                "aws lambda list-functions --output json",
                "aws cloudwatch describe-alarms --output json"
            ]
        },

        "KSI_MLA_04": {
            "title": "Implement authenticated vulnerability scanning",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF Inspector scanning configured:
                ✅ Award authenticated scanning points
            IF SSM patch compliance data available:
                ✅ Award system-level scanning points
            IF Security Hub findings aggregated:
                ✅ Award vulnerability aggregation points
            IF ECR container scanning enabled:
                ✅ Award container vulnerability scanning points
            """,
            "passing_criteria": "Inspector + patch compliance + vulnerability aggregation",
            "cli_commands": [
                "aws inspector2 get-configuration --output json",
                "aws ssm describe-instance-patch-states --output json",
                "aws securityhub get-findings --output json",
                "aws ecr describe-repositories --output json"
            ]
        },

        "KSI_MLA_05": {
            "title": "Test Infrastructure as Code for security and compliance",
            "evidence_type": "Evidence Files + AWS CLI Commands",
            "logic": """
            IF Evidence files contain Checkov scan results:
                ✅ Award IaC security scanning points
            IF SARIF metadata exists:
                ✅ Award standardized reporting points
            IF Terraform plan validation exists:
                ✅ Award infrastructure validation points
            IF Policy as Code files exist:
                ✅ Award policy automation points
            IF CodeBuild projects for security testing:
                ✅ Award CI/CD security integration points
            """,
            "passing_criteria": "IaC security scanning + policy validation + CI/CD integration",
            "cli_commands": [
                "aws codebuild list-projects --output json",
                "aws cloudformation validate-template --output json",
                "evidence_check"
            ]
        },

        "KSI_MLA_06": {
            "title": "Centrally track and manage security findings",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF Security Hub configured as central dashboard:
                ✅ Award centralized tracking points
            IF Multiple security services integrated:
                ✅ Award comprehensive coverage points
            IF Custom insights and dashboards:
                ✅ Award advanced management points
            IF Automated findings workflow:
                ✅ Award workflow automation points
            """,
            "passing_criteria": "Security Hub + integrated services + automated workflow",
            "cli_commands": [
                "aws securityhub describe-hub --output json",
                "aws securityhub get-findings --output json",
                "aws securityhub list-insights --output json",
                "aws events list-rules --output json"
            ]
        },

        # ===== CONFIGURATION MANAGEMENT & TESTING (CMT) - 5 KSIs =====
        "KSI_CMT_01": {
            "title": "Establish and maintain configuration baselines",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF CloudTrail trails logging (IsLogging=true OR configured):
                ✅ Award modification tracking points (REQUIRED)
            IF Config recorders active:
                ✅ Award baseline recording points
            IF Config rules active:
                ✅ Award compliance monitoring points
            IF CloudFormation stacks successful:
                ✅ Award IaC baseline points
            ELSE without CloudTrail:
                ❌ No modification tracking (FAIL)
            """,
            "passing_criteria": "CloudTrail modification tracking (REQUIRED) + Config recording",
            "cli_commands": [
                "aws cloudtrail describe-trails --output json",
                "aws cloudtrail get-trail-status --output json",
                "aws config describe-configuration-recorders --output json",
                "aws config describe-config-rules --output json",
                "aws cloudformation list-stacks --output json"
            ]
        },

        "KSI_CMT_02": {
            "title": "Execute changes through redeployment rather than direct modification",
            "evidence_type": "AWS CLI Commands + Cross-Account Data",
            "logic": """
            IF CloudFormation stacks successful:
                ✅ Award AWS-managed IaC points
            IF Instances with consistent naming/Terraform patterns:
                ✅ Award Terraform-managed IaC points
            IF Lambda functions exist:
                ✅ Award immutable serverless points
            IF Both CloudFormation AND Terraform patterns:
                ✅ Award comprehensive immutable deployment
            IF Cross-account data available:
                ✅ Award enterprise governance bonus
            """,
            "passing_criteria": "CloudFormation + Terraform patterns OR comprehensive IaC approach",
            "cli_commands": [
                "aws cloudformation list-stacks --output json",
                "aws ec2 describe-instances --output json",
                "aws lambda list-functions --output json",
                "aws autoscaling describe-auto-scaling-groups --output json"
            ]
        },

        "KSI_CMT_03": {
            "title": "Implement automated testing and validation prior to deployment",
            "evidence_type": "Evidence Files (evidence_v2/KSI-CMT-03/)",
            "logic": """
            IF automated_testing_proof.json exists:
                ✅ Award testing foundation points
            IF checkov_scan_summary.json exists:
                ✅ Award security validation points
            IF sarif_metadata.json exists:
                ✅ Award standardized reporting points
            IF terraform_plan_validation.json exists:
                ✅ Award infrastructure change validation points
            IF policy_as_code.json exists:
                ✅ Award policy automation points
            """,
            "passing_criteria": "Automated testing proof + Checkov scanning + additional validation",
            "evidence_files": [
                "evidence_v2/KSI-CMT-03/automated_testing_proof.json",
                "evidence_v2/KSI-CMT-03/checkov_scan_summary.json",
                "evidence_v2/KSI-CMT-03/sarif_metadata.json",
                "evidence_v2/KSI-CMT-03/terraform_plan_validation.json",
                "evidence_v2/KSI-CMT-03/policy_as_code.json"
            ]
        },

        "KSI_CMT_04": {
            "title": "Document and follow change management procedures",
            "evidence_type": "Evidence Files + AWS CLI Commands",
            "logic": """
            IF Change management policy documents exist:
                ✅ Award procedure documentation points
            IF CloudTrail logging active for change tracking:
                ✅ Award change tracking points
            IF Config rules for change compliance:
                ✅ Award automated compliance points
            IF Maintenance windows defined:
                ✅ Award controlled change points
            """,
            "passing_criteria": "Change procedures + tracking + compliance + controlled deployment",
            "cli_commands": [
                "aws cloudtrail describe-trails --output json",
                "aws config describe-config-rules --output json",
                "aws ssm describe-maintenance-windows --output json"
            ]
        },

        "KSI_CMT_05": {
            "title": "Evaluate risk and potential impact of changes",
            "evidence_type": "Evidence Files + AWS CLI Commands",
            "logic": """
            IF Risk assessment procedures documented:
                ✅ Award risk evaluation points
            IF Change approval workflows exist:
                ✅ Award governance points
            IF Impact analysis procedures defined:
                ✅ Award impact assessment points
            IF Rollback procedures documented:
                ✅ Award risk mitigation points
            """,
            "passing_criteria": "Risk procedures + approval workflows + impact analysis + rollback capability",
            "evidence_files": [
                "evidence_v2/KSI-CMT-05/risk_assessment_procedures.pdf",
                "evidence_v2/KSI-CMT-05/change_approval_workflow.pdf",
                "evidence_v2/KSI-CMT-05/impact_analysis_procedures.pdf"
            ]
        },

        # ===== PERSONNEL & INFORMATION (PIY) - 7 KSIs =====
        "KSI_PIY_01": {
            "title": "Have up-to-date information resource inventory",
            "evidence_type": "AWS CLI Commands + Evidence Files",
            "logic": """
            IF AWS Resource Groups tagged resources exist:
                ✅ Award AWS resource inventory points
            IF Manual inventory files exist in evidence_v2/KSI-PIY-01/:
                ✅ Award documented inventory points
            IF Both AWS discovery AND manual documentation:
                ✅ Award comprehensive inventory
            ELSE:
                ❌ No comprehensive inventory
            """,
            "passing_criteria": "AWS resource discovery + manual inventory documentation",
            "cli_commands": [
                "aws resource-groups list-groups --output json",
                "aws config describe-configuration-recorders --output json",
                "aws ec2 describe-instances --output json"
            ]
        },

        "KSI_PIY_02": {
            "title": "Have policies outlining security objectives",
            "evidence_type": "Evidence Files",
            "logic": """
            IF Security policy documents exist:
                ✅ Award policy documentation points
            IF Information security objectives defined:
                ✅ Award objectives definition points
            IF Resource security standards documented:
                ✅ Award standards documentation points
            """,
            "passing_criteria": "Security policies + objectives + standards documentation",
            "evidence_files": [
                "evidence_v2/KSI-PIY-02/information_security_policy.pdf",
                "evidence_v2/KSI-PIY-02/security_objectives.pdf",
                "evidence_v2/KSI-PIY-02/resource_security_standards.pdf"
            ]
        },

        "KSI_PIY_03": {
            "title": "Maintain a vulnerability disclosure program",
            "evidence_type": "Evidence Files",
            "logic": """
            IF Vulnerability disclosure policy exists:
                ✅ Award policy points
            IF Responsible disclosure program documented:
                ✅ Award program points
            """,
            "passing_criteria": "Vulnerability disclosure policy + responsible disclosure program",
            "evidence_files": [
                "evidence_v2/KSI-PIY-03/vulnerability_disclosure_policy.pdf",
                "evidence_v2/KSI-PIY-03/responsible_disclosure_program.pdf"
            ]
        },

        "KSI_PIY_04": {
            "title": "Build security into SDLC and align with CISA Secure By Design",
            "evidence_type": "AWS CLI Commands + Evidence Files",
            "logic": """
            IF CodeCommit repositories exist:
                ✅ Award secure development infrastructure points
            IF SDLC security procedures documented:
                ✅ Award secure development process points
            IF CISA Secure By Design alignment documented:
                ✅ Award framework alignment points
            """,
            "passing_criteria": "Secure development infrastructure + SDLC procedures + CISA alignment",
            "cli_commands": [
                "aws codecommit list-repositories --output json"
            ]
        },

        "KSI_PIY_05": {
            "title": "Document methods for evaluating information resource implementations",
            "evidence_type": "Evidence Files",
            "logic": """
            IF Evaluation methodology documented:
                ✅ Award methodology points
            IF Security assessment procedures exist:
                ✅ Award assessment points
            IF Implementation review process defined:
                ✅ Award review process points
            """,
            "passing_criteria": "Evaluation methodology + assessment procedures + review process",
            "evidence_files": [
                "evidence_v2/KSI-PIY-05/evaluation_methodology.pdf",
                "evidence_v2/KSI-PIY-05/security_assessment_procedures.pdf",
                "evidence_v2/KSI-PIY-05/implementation_review_process.pdf"
            ]
        },

        "KSI_PIY_06": {
            "title": "Have dedicated security staff and budget with executive support",
            "evidence_type": "Evidence Files",
            "logic": """
            IF Security organizational chart exists:
                ✅ Award organizational structure points
            IF Security budget allocation documented:
                ✅ Award budget points
            IF Executive security charter exists:
                ✅ Award executive support points
            """,
            "passing_criteria": "Organizational structure + budget allocation + executive endorsement",
            "evidence_files": [
                "evidence_v2/KSI-PIY-06/security_org_chart.pdf",
                "evidence_v2/KSI-PIY-06/security_budget_allocation.pdf",
                "evidence_v2/KSI-PIY-06/executive_security_charter.pdf"
            ]
        },

        "KSI_PIY_07": {
            "title": "Document risk management decisions for supply chain security",
            "evidence_type": "Evidence Files",
            "logic": """
            IF Supply chain risk management documented:
                ✅ Award risk management points
            IF Vendor security assessments exist:
                ✅ Award vendor assessment points
            IF Software supply chain policy exists:
                ✅ Award policy points
            """,
            "passing_criteria": "Supply chain risk management + vendor assessments + policy documentation",
            "evidence_files": [
                "evidence_v2/KSI-PIY-07/supply_chain_risk_management.pdf",
                "evidence_v2/KSI-PIY-07/vendor_security_assessments.pdf",
                "evidence_v2/KSI-PIY-07/software_supply_chain_policy.pdf"
            ]
        },

        # ===== THIRD PARTY RESOURCES (TPR) - 4 KSIs =====
        "KSI_TPR_01": {
            "title": "Identify all third-party information resources",
            "evidence_type": "AWS CLI Commands + Evidence Files",
            "logic": """
            IF Cross-account IAM roles exist:
                ✅ Award third-party integration detection points
            IF External service integrations documented:
                ✅ Award documentation points
            IF Third-party inventory exists:
                ✅ Award inventory points
            """,
            "passing_criteria": "Third-party resource identification + documentation + inventory",
            "cli_commands": [
                "aws iam list-roles --output json",
                "aws iam list-saml-providers --output json"
            ]
        },

        "KSI_TPR_02": {
            "title": "Confirm services handling federal information are FedRAMP authorized",
            "evidence_type": "Evidence Files (evidence_v2/KSI-TPR-02/)",
            "logic": """
            IF Federal Information Mapping document exists:
                ✅ Award comprehensive mapping (FULL CREDIT for all requirements)
            ELSE:
                IF service inventory exists:
                    ✅ Award inventory points
                IF FedRAMP verification docs exist:
                    ✅ Award authorization verification points
                IF configuration compliance docs exist:
                    ✅ Award compliance verification points
                IF verification process docs exist:
                    ✅ Award process documentation points
            """,
            "passing_criteria": "Comprehensive federal information mapping OR separate inventory + verification docs",
            "evidence_files": [
                "evidence_v2/KSI-TPR-02/federal_information_mapping.pdf",
                "evidence_v2/KSI-TPR-02/service_inventory.pdf",
                "evidence_v2/KSI-TPR-02/fedramp_verification.pdf"
            ]
        },

        "KSI_TPR_03": {
            "title": "Implement risk mitigation for non-FedRAMP third-party resources",
            "evidence_type": "Evidence Files",
            "logic": """
            IF Risk mitigation strategies documented:
                ✅ Award mitigation points
            IF Compensating controls defined:
                ✅ Award controls points
            IF Risk acceptance documentation exists:
                ✅ Award governance points
            """,
            "passing_criteria": "Risk mitigation + compensating controls + documented acceptance",
            "evidence_files": [
                "evidence_v2/KSI-TPR-03/risk_mitigation_strategies.pdf",
                "evidence_v2/KSI-TPR-03/compensating_controls.pdf",
                "evidence_v2/KSI-TPR-03/risk_acceptance_documentation.pdf"
            ]
        },

        "KSI_TPR_04": {
            "title": "Monitor third-party resources for vulnerabilities",
            "evidence_type": "AWS CLI Commands + Evidence Files",
            "logic": """
            IF Security Hub monitoring configured:
                ✅ Award automated monitoring points
            IF Third-party monitoring procedures documented:
                ✅ Award process points
            IF Vulnerability tracking for third parties exists:
                ✅ Award tracking points
            """,
            "passing_criteria": "Automated monitoring + documented procedures + vulnerability tracking",
            "cli_commands": [
                "aws securityhub describe-hub --output json",
                "aws inspector2 get-configuration --output json"
            ]
        },

        # ===== CYBERSECURITY EDUCATION (CED) - 2 KSIs =====
        "KSI_CED_01": {
            "title": "Provide security awareness training",
            "evidence_type": "Evidence Files",
            "logic": """
            IF Security awareness training program documented:
                ✅ Award training program points
            IF Training records exist:
                ✅ Award implementation points
            IF Training effectiveness measurement exists:
                ✅ Award effectiveness points
            """,
            "passing_criteria": "Training program + records + effectiveness measurement",
            "evidence_files": [
                "evidence_v2/KSI-CED-01/security_awareness_training.pdf",
                "evidence_v2/KSI-CED-01/training_records.pdf",
                "evidence_v2/KSI-CED-01/training_effectiveness.pdf"
            ]
        },

        "KSI_CED_02": {
            "title": "Provide role-specific security training",
            "evidence_type": "Evidence Files",
            "logic": """
            IF Role-specific training programs documented:
                ✅ Award role-specific training points
            IF Training customization by role exists:
                ✅ Award customization points
            IF Specialized training records exist:
                ✅ Award specialized training points
            """,
            "passing_criteria": "Role-specific programs + customization + specialized records",
            "evidence_files": [
                "evidence_v2/KSI-CED-02/role_specific_training.pdf",
                "evidence_v2/KSI-CED-02/training_customization.pdf",
                "evidence_v2/KSI-CED-02/specialized_training_records.pdf"
            ]
        },

        # ===== RECOVERY & RESILIENCE (RPL) - 4 KSIs =====
        "KSI_RPL_01": {
            "title": "Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO)",
            "evidence_type": "Evidence Files + AWS CLI Commands",
            "logic": """
            IF RTO/RPO definition documents exist:
                ✅ Award documentation points
            IF RDS instances with BackupRetentionPeriod > 0:
                ✅ Award technical validation points (supports RPO)
            IF Point-in-time recovery capability exists:
                ✅ Award RPO validation points
            IF Backup plans exist:
                ✅ Award infrastructure alignment points
            """,
            "passing_criteria": "RTO/RPO documentation + RDS backup retention + recovery capability",
            "cli_commands": [
                "aws rds describe-db-instances --output json",
                "aws backup list-backup-plans --output json"
            ]
        },

        "KSI_RPL_02": {
            "title": "Develop and maintain recovery procedures",
            "evidence_type": "Evidence Files",
            "logic": """
            IF Recovery procedures documented:
                ✅ Award procedure points
            IF Recovery testing procedures exist:
                ✅ Award testing points
            IF Recovery playbooks exist:
                ✅ Award playbook points
            """,
            "passing_criteria": "Recovery procedures + testing + playbooks",
            "evidence_files": [
                "evidence_v2/KSI-RPL-02/recovery_procedures.pdf",
                "evidence_v2/KSI-RPL-02/recovery_testing.pdf",
                "evidence_v2/KSI-RPL-02/recovery_playbooks.pdf"
            ]
        },

        "KSI_RPL_03": {
            "title": "Perform system backups aligned with recovery objectives",
            "evidence_type": "AWS CLI Commands",
            "logic": """
            IF Backup plans exist:
                ✅ Award backup infrastructure points
            IF Backup plan rules have retention ≥30 days:
                ✅ Award retention compliance points
            IF Completed backup jobs exist OR LastExecutionDate recent:
                ✅ Award backup operation validation points (CRITICAL FIX)
            IF RDS instances with BackupRetentionPeriod > 0:
                ✅ Award database backup points
            IF EBS snapshots exist:
                ✅ Award additional backup coverage points
            """,
            "passing_criteria": "Backup plans + compliant retention + validated operations + RDS backups",
            "cli_commands": [
                "aws backup list-backup-plans --output json",
                "aws backup list-backup-jobs --output json",
                "aws rds describe-db-instances --output json",
                "aws ec2 describe-snapshots --owner-ids self --output json"
            ]
        },

        "KSI_RPL_04": {
            "title": "Test recovery procedures regularly",
            "evidence_type": "Evidence Files + AWS CLI Commands",
            "logic": """
            IF Recovery testing schedule documented:
                ✅ Award testing schedule points
            IF Testing results documented:
                ✅ Award results documentation points
            IF Recovery automation exists:
                ✅ Award automation points
            """,
            "passing_criteria": "Testing schedule + results documentation + recovery automation",
            "evidence_files": [
                "evidence_v2/KSI-RPL-04/recovery_testing_schedule.pdf",
                "evidence_v2/KSI-RPL-04/testing_results.pdf"
            ]
        },

        # ===== INCIDENT & NON-COMPLIANCE RESPONSE (INR) - 3 KSIs =====
        "KSI_INR_01": {
            "title": "Report incidents according to FedRAMP requirements",
            "evidence_type": "Evidence Files (evidence_v2/KSI-INR-01/)",
            "logic": """
            IF Core reporting procedure documents exist:
                ✅ Award procedure points per document
            IF FedRAMP compliance procedures specifically mentioned:
                ✅ Award compliance points
            ELSE IF no FedRAMP compliance found:
                ❌ Subtract points (regulatory requirement)
            IF Enhanced compliance procedures exist:
                ✅ Award bonus points
            """,
            "passing_criteria": "Core reporting procedures + specific FedRAMP compliance documentation",
            "evidence_files": [
                "evidence_v2/KSI-INR-01/incident_reporting_procedures.pdf",
                "evidence_v2/KSI-INR-01/fedramp_reporting_compliance.pdf"
            ]
        },

        "KSI_INR_02": {
            "title": "Maintain incident response log",
            "evidence_type": "Evidence Files + AWS CLI Commands",
            "logic": """
            IF Incident logging procedures documented:
                ✅ Award logging procedure points
            IF CloudTrail logging active for incident tracking:
                ✅ Award technical logging points
            IF Incident response log templates exist:
                ✅ Award documentation structure points
            """,
            "passing_criteria": "Logging procedures + technical logging + structured documentation",
            "cli_commands": [
                "aws cloudtrail describe-trails --output json",
                "aws logs describe-log-groups --output json"
            ]
        },

        "KSI_INR_03": {
            "title": "Document lessons learned from incidents",
            "evidence_type": "Evidence Files",
            "logic": """
            IF Lessons learned procedures documented:
                ✅ Award procedure points
            IF Post-incident review process exists:
                ✅ Award review process points
            IF Improvement implementation tracking exists:
                ✅ Award improvement tracking points
            """,
            "passing_criteria": "Lessons learned procedures + review process + improvement tracking",
            "evidence_files": [
                "evidence_v2/KSI-INR-03/lessons_learned_procedures.pdf",
                "evidence_v2/KSI-INR-03/post_incident_review.pdf",
                "evidence_v2/KSI-INR-03/improvement_tracking.pdf"
            ]
        }
    }
    
    return ksi_explanations

def generate_assessment_summary():
    """
    Provides a high-level summary of the assessment logic patterns.
    """
    return """
    FEDRAM KSI ASSESSMENT LOGIC PATTERNS - COMPLETE EDITION
    =======================================================
    
    TOTAL KSIs: 51 across 10 categories + MAS
    - CNA (Cloud Native Architecture): 7 KSIs
    - SVC (Service Configuration): 7 KSIs  
    - IAM (Identity & Access Management): 6 KSIs
    - MLA (Monitoring, Logging & Analysis): 6 KSIs
    - CMT (Configuration Management & Testing): 5 KSIs
    - PIY (Personnel & Information): 7 KSIs
    - TPR (Third Party Resources): 4 KSIs
    - CED (Cybersecurity Education): 2 KSIs
    - RPL (Recovery & Resilience): 4 KSIs
    - INR (Incident & Non-Compliance Response): 3 KSIs
    
    1. EVIDENCE COLLECTION:
       - AWS CLI Commands: Real-time infrastructure assessment (automated)
       - Evidence Files: Manual documentation in evidence_v2/ directories
       - Cross-Account Data: Management account data files for enterprise setups
    
    2. SCORING PATTERNS:
       - Foundation Score: Basic requirement (REQUIRED for pass)
       - Enhancement Score: Production features (bonus points)
       - Enterprise Score: Organization-wide governance (bonus points)
       - Penalty Logic: Subtract points for missing regulatory requirements
    
    3. PASSING CRITERIA TIERS:
       - ✅ EXCELLENT (≥90%): Comprehensive + enterprise features
       - ✅ STRONG (≥75%): Good coverage + some enhancements  
       - ✅ BASIC (≥60%): Foundation met + minimal enhancements
       - ⚠️ LIMITED (≥40%): Foundation met but gaps exist
       - ❌ INSUFFICIENT (<40%): Foundation requirements not met
    
    4. SPECIAL LOGIC:
       - Federated Identity: Recognizes external IdP (Okta) MFA enforcement
       - Terraform Detection: Identifies Infrastructure as Code via naming patterns
       - Cross-Account: Combines member + management account data
       - Evidence-Based: Some KSIs rely purely on manual documentation
       - Serverless-Friendly: Credits appropriate architectures without penalizing
    
    5. REGULATORY FOCUS:
       - FedRAMP Low Impact: Reasonable thresholds for pilot environments
       - Enterprise Scaling: Bonus points for organization-wide governance
       - Cost-Conscious: Credits excellent configuration even if not actively used
       - Risk-Appropriate: Different expectations for different impact levels
    
    6. AUTOMATION LEVELS:
       - Fully Automated: CLI-based assessment (majority of KSIs)
       - Partially Automated: CLI + evidence file validation
       - Manual: Evidence file review only (PIY, TPR, CED, some RPL/INR)
    """

def show_ksis_by_category():
    """Show KSIs organized by category with complete coverage"""
    categories = {
        "Cloud Networking & Architecture (CNA)": [
            "KSI_CNA_01", "KSI_CNA_02", "KSI_CNA_03", "KSI_CNA_04", 
            "KSI_CNA_05", "KSI_CNA_06", "KSI_CNA_07"
        ],
        "Services (SVC)": [
            "KSI_SVC_01", "KSI_SVC_02", "KSI_SVC_03", "KSI_SVC_04", 
            "KSI_SVC_05", "KSI_SVC_06", "KSI_SVC_07"
        ],
        "Identity & Access Management (IAM)": [
            "KSI_IAM_01", "KSI_IAM_02", "KSI_IAM_03", "KSI_IAM_04", 
            "KSI_IAM_05", "KSI_IAM_06"
        ],
        "Monitoring, Logging & Analysis (MLA)": [
            "KSI_MLA_01", "KSI_MLA_02", "KSI_MLA_03", "KSI_MLA_04", 
            "KSI_MLA_05", "KSI_MLA_06"
        ],
        "Configuration Management & Testing (CMT)": [
            "KSI_CMT_01", "KSI_CMT_02", "KSI_CMT_03", "KSI_CMT_04", "KSI_CMT_05"
        ],
        "Personnel & Information (PIY)": [
            "KSI_PIY_01", "KSI_PIY_02", "KSI_PIY_03", "KSI_PIY_04", 
            "KSI_PIY_05", "KSI_PIY_06", "KSI_PIY_07"
        ],
        "Third Party Resources (TPR)": [
            "KSI_TPR_01", "KSI_TPR_02", "KSI_TPR_03", "KSI_TPR_04"
        ],
        "Recovery & Resilience (RPL)": [
            "KSI_RPL_01", "KSI_RPL_02", "KSI_RPL_03", "KSI_RPL_04"
        ],
        "Incident & Non-Compliance Response (INR)": [
            "KSI_INR_01", "KSI_INR_02", "KSI_INR_03"
        ],
        "Cybersecurity Education (CED)": [
            "KSI_CED_01", "KSI_CED_02"
        ]
    }
    
    explanations = explain_ksi_logic()
    
    total_ksis = 0
    for category, ksi_list in categories.items():
        print(f"\n{category}")
        print("-" * len(category))
        for ksi_code in ksi_list:
            total_ksis += 1
            if ksi_code in explanations:
                print(f"  {ksi_code}: {explanations[ksi_code]['title']}")
            else:
                print(f"  {ksi_code}: [Logic definition needed]")
    
    print(f"\nTOTAL: {total_ksis} KSIs across {len(categories)} categories")
    print("\nCoverage Status:")
    implemented = len([k for k in explanations.keys() if k.startswith('KSI_')])
    print(f"✅ Implemented: {implemented}/{total_ksis} KSIs ({implemented/total_ksis*100:.1f}%)")

def explain_specific_ksi(ksi_code):
    """
    Explains the logic for a specific KSI.
    
    Args:
        ksi_code (str): The KSI code (e.g., 'KSI_CNA_01')
    
    Returns:
        str: Human-readable explanation of the KSI logic
    """
    explanations = explain_ksi_logic()
    
    if ksi_code in explanations:
        ksi = explanations[ksi_code]
        
        # Format CLI commands if they exist
        cli_commands_str = ""
        if 'cli_commands' in ksi:
            cli_commands_str = "\n        CLI Commands:\n"
            for cmd in ksi['cli_commands']:
                cli_commands_str += f"        - {cmd}\n"
        
        # Format evidence files if they exist
        evidence_files_str = ""
        if 'evidence_files' in ksi:
            evidence_files_str = "\n        Evidence Files:\n"
            for file in ksi['evidence_files']:
                evidence_files_str += f"        - {file}\n"
        
        return f"""
        {ksi['title']}
        {'='*80}
        Evidence Type: {ksi['evidence_type']}
        {cli_commands_str}{evidence_files_str}
        
        Logic Flow:
        {ksi['logic']}
        
        Passing Criteria: {ksi['passing_criteria']}
        """
    else:
        available_ksis = [k for k in explanations.keys() if k.startswith('KSI_')]
        return f"KSI {ksi_code} not found. Available KSIs: {available_ksis}"

# Interactive mode and other functions remain the same...
def interactive_mode():
    """Interactive mode for exploring KSI logic"""
    explanations = explain_ksi_logic()
    
    while True:
        print("\n" + "="*80)
        print("FedRAMP KSI Logic Explainer - COMPLETE EDITION - Interactive Mode")
        print("="*80)
        print("Options:")
        print("1. List all KSIs (51 total)")
        print("2. Explain specific KSI")
        print("3. Show assessment summary")
        print("4. Search by keyword")
        print("5. Show KSIs by category")
        print("6. Show coverage statistics")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            print("\nAll 51 Available KSIs:")
            ksi_list = [k for k in explanations.keys() if k.startswith('KSI_')]
            for i, (ksi_code, ksi_info) in enumerate([(k, explanations[k]) for k in sorted(ksi_list)], 1):
                print(f"{i:2d}. {ksi_code}: {ksi_info['title']}")
        
        elif choice == "2":
            ksi_code = input("\nEnter KSI code (e.g., KSI_CNA_01): ").strip().upper()
            print(explain_specific_ksi(ksi_code))
        
        elif choice == "3":
            print(generate_assessment_summary())
        
        elif choice == "4":
            keyword = input("\nEnter keyword to search for: ").strip().lower()
            found = False
            for ksi_code, ksi_info in explanations.items():
                if keyword in ksi_info['title'].lower() or keyword in ksi_info['logic'].lower():
                    print(f"\n{ksi_code}: {ksi_info['title']}")
                    found = True
            if not found:
                print(f"No KSIs found containing '{keyword}'")
        
        elif choice == "5":
            show_ksis_by_category()
        
        elif choice == "6":
            show_ksis_by_category()
        
        elif choice == "7":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1-7.")

# Keep existing generate_report function...
def generate_report(ksi_codes=None):
    """Generate a comprehensive report for specified KSIs or all KSIs"""
    explanations = explain_ksi_logic()
    
    if ksi_codes is None:
        ksi_codes = sorted([k for k in explanations.keys() if k.startswith('KSI_')])
    
    print("FedRAMP KSI Logic Assessment Report - COMPLETE EDITION")
    print("=" * 70)
    print(f"Generated for {len(ksi_codes)} KSIs")
    print(f"Based on: Meridian FedRAMP 20x Phase One SRTM v06.24.2025")
    print(f"Updated: June 27, 2025\n")
    
    for ksi_code in ksi_codes:
        if ksi_code in explanations:
            ksi = explanations[ksi_code]
            print(f"\n{ksi_code}: {ksi['title']}")
            print("-" * 70)
            print(f"Evidence Type: {ksi['evidence_type']}")
            print(f"Passing Criteria: {ksi['passing_criteria']}")
            print("\nLogic Flow:")
            print(ksi['logic'])
            
            if 'cli_commands' in ksi:
                print(f"\nCLI Commands ({len(ksi['cli_commands'])}):")
                for cmd in ksi['cli_commands']:
                    print(f"  • {cmd}")
            
            if 'evidence_files' in ksi:
                print(f"\nEvidence Files ({len(ksi['evidence_files'])}):")
                for file in ksi['evidence_files']:
                    print(f"  • {file}")
            
            print("\n" + "="*70)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Command line mode
        if sys.argv[1] == "--interactive" or sys.argv[1] == "-i":
            interactive_mode()
        elif sys.argv[1] == "--summary" or sys.argv[1] == "-s":
            print(generate_assessment_summary())
        elif sys.argv[1] == "--report" or sys.argv[1] == "-r":
            if len(sys.argv) > 2:
                ksi_codes = sys.argv[2:]
                generate_report(ksi_codes)
            else:
                generate_report()
        elif sys.argv[1] == "--categories" or sys.argv[1] == "-c":
            show_ksis_by_category()
        elif sys.argv[1].startswith("KSI_"):
            print(explain_specific_ksi(sys.argv[1]))
        else:
            print("Usage:")
            print("  python complete_ksi_explainer.py --interactive     # Interactive mode")
            print("  python complete_ksi_explainer.py --summary         # Show assessment summary")
            print("  python complete_ksi_explainer.py --categories      # Show KSIs by category")
            print("  python complete_ksi_explainer.py --report          # Generate full report")
            print("  python complete_ksi_explainer.py KSI_CNA_01        # Explain specific KSI")
            print("  python complete_ksi_explainer.py --report KSI_CNA_01 KSI_IAM_01  # Report for specific KSIs")
    else:
        # Default: Interactive mode
        interactive_mode()
