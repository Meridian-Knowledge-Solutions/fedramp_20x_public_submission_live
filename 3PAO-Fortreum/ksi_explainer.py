#!/usr/bin/env python3
"""
FedRAMP KSI Evaluation Logic Explainer
======================================
This tool explains the evaluation logic for each Key Security Implementation (KSI) 
in human-readable terms for 3PAO assessors and FedRAMP stakeholders.
"""

def explain_ksi_logic():
    """
    Explains the evaluation logic for each KSI in the assessment script.
    Each KSI follows a pattern: Parse inputs → Check evidence → Score → Return result
    """
    
    ksi_explanations = {
        # ===== CLOUD NETWORKING & ARCHITECTURE (CNA) =====
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
            ELSE:
                ❌ Insufficient traffic controls
            """,
            "passing_criteria": "≥80% restrictive security groups + some egress controls + network segmentation"
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
            ELSE:
                ❌ High attack surface
            """,
            "passing_criteria": "Private subnet placement + multi-AZ + restrictive security groups"
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
            IF Single VPC setup:
                ✅ Award full points (appropriate design)
            IF Multi-VPC but no Transit Gateway:
                ⚠️ Consider centralized control
            """,
            "passing_criteria": "Functional routing + access controls + appropriate architecture"
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
            ELSE:
                ❌ No immutable patterns detected
            """,
            "passing_criteria": "CloudFormation + Terraform patterns OR serverless + standardized deployment"
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
            IF Multi-AZ Load Balancers exist:
                ✅ Award service resilience points
            IF Route 53 hosted zones exist:
                ✅ Award DNS protection points
            """,
            "passing_criteria": "Shield Standard + Regional WAF + Multi-AZ ALB + Route 53"
        },

        # ===== SERVICES (SVC) =====
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
            """,
            "passing_criteria": "Restrictive security groups + system management + compliance rules"
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
            IF No storage resources:
                ✅ Nothing to encrypt (acceptable)
            """,
            "passing_criteria": "Encrypted EBS volumes OR encrypted RDS OR no storage resources"
        },

        # ===== IDENTITY & ACCESS MANAGEMENT (IAM) =====
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
            "passing_criteria": "Identity Center + external IdP (Okta) federation OR traditional MFA devices"
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
            "passing_criteria": "Identity Center permission sets + SSO sessions + role-based access"
        },

        # ===== MONITORING, LOGGING & ANALYSIS (MLA) =====
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
            "passing_criteria": "CloudTrail validation + log groups + analysis capability"
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
            "passing_criteria": "Security Hub standards + Inspector scanning + remediation capability"
        },

        # ===== CONFIGURATION MANAGEMENT & TESTING (CMT) =====
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
            "passing_criteria": "CloudTrail modification tracking (REQUIRED) + Config recording"
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
            "passing_criteria": "CloudFormation + Terraform patterns OR comprehensive IaC approach"
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
            "passing_criteria": "Automated testing proof + Checkov scanning + additional validation"
        },

        # ===== PERSONNEL & INFORMATION YAML (PIY) =====
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
            "passing_criteria": "AWS resource discovery + manual inventory documentation"
        },

        # ===== THIRD PARTY RESOURCES (TPR) =====
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
            "passing_criteria": "Comprehensive federal information mapping OR separate inventory + verification docs"
        },

        # ===== RECOVERY & RESILIENCE (RPL) =====
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
            "passing_criteria": "RTO/RPO documentation + RDS backup retention + recovery capability"
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
            "passing_criteria": "Backup plans + compliant retention + validated operations + RDS backups"
        },

        # ===== INCIDENT & NON-COMPLIANCE RESPONSE (INR) =====
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
            "passing_criteria": "Core reporting procedures + specific FedRAMP compliance documentation"
        }
    }
    
    return ksi_explanations

def generate_assessment_summary():
    """
    Provides a high-level summary of the assessment logic patterns.
    """
    return """
    FEDRAM KSI ASSESSMENT LOGIC PATTERNS
    ====================================
    
    1. EVIDENCE COLLECTION:
       - AWS CLI Commands: Real-time infrastructure assessment
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
    """

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
        return f"""
        {ksi['title']}
        {'='*60}
        Evidence Type: {ksi['evidence_type']}
        
        Logic Flow:
        {ksi['logic']}
        
        Passing Criteria: {ksi['passing_criteria']}
        """
    else:
        return f"KSI {ksi_code} not found. Available KSIs: {list(explanations.keys())}"

# Example usage and interactive features
def interactive_mode():
    """Interactive mode for exploring KSI logic"""
    explanations = explain_ksi_logic()
    
    while True:
        print("\n" + "="*60)
        print("FedRAMP KSI Logic Explainer - Interactive Mode")
        print("="*60)
        print("Options:")
        print("1. List all KSIs")
        print("2. Explain specific KSI")
        print("3. Show assessment summary")
        print("4. Search by keyword")
        print("5. Show KSIs by category")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            print("\nAvailable KSIs:")
            for i, (ksi_code, ksi_info) in enumerate(explanations.items(), 1):
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
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1-6.")

def show_ksis_by_category():
    """Show KSIs organized by category"""
    categories = {
        "Cloud Networking & Architecture (CNA)": ["KSI_CNA_01", "KSI_CNA_02", "KSI_CNA_03", "KSI_CNA_04", "KSI_CNA_05"],
        "Services (SVC)": ["KSI_SVC_01", "KSI_SVC_02", "KSI_SVC_03", "KSI_SVC_04", "KSI_SVC_05", "KSI_SVC_06", "KSI_SVC_07"],
        "Identity & Access Management (IAM)": ["KSI_IAM_01", "KSI_IAM_02", "KSI_IAM_03", "KSI_IAM_04", "KSI_IAM_05", "KSI_IAM_06"],
        "Monitoring, Logging & Analysis (MLA)": ["KSI_MLA_01", "KSI_MLA_02", "KSI_MLA_03", "KSI_MLA_04", "KSI_MLA_05", "KSI_MLA_06"],
        "Configuration Management & Testing (CMT)": ["KSI_CMT_01", "KSI_CMT_02", "KSI_CMT_03", "KSI_CMT_04", "KSI_CMT_05"],
        "Personnel & Information (PIY)": ["KSI_PIY_01", "KSI_PIY_02", "KSI_PIY_03", "KSI_PIY_04", "KSI_PIY_05", "KSI_PIY_06", "KSI_PIY_07"],
        "Third Party Resources (TPR)": ["KSI_TPR_01", "KSI_TPR_02", "KSI_TPR_03", "KSI_TPR_04"],
        "Recovery & Resilience (RPL)": ["KSI_RPL_01", "KSI_RPL_02", "KSI_RPL_03", "KSI_RPL_04"],
        "Incident & Non-Compliance Response (INR)": ["KSI_INR_01", "KSI_INR_02", "KSI_INR_03"],
        "Cybersecurity Education (CED)": ["KSI_CED_01", "KSI_CED_02"]
    }
    
    explanations = explain_ksi_logic()
    
    for category, ksi_list in categories.items():
        print(f"\n{category}")
        print("-" * len(category))
        for ksi_code in ksi_list:
            if ksi_code in explanations:
                print(f"  {ksi_code}: {explanations[ksi_code]['title']}")

def generate_report(ksi_codes=None):
    """Generate a comprehensive report for specified KSIs or all KSIs"""
    explanations = explain_ksi_logic()
    
    if ksi_codes is None:
        ksi_codes = list(explanations.keys())
    
    print("FedRAMP KSI Logic Assessment Report")
    print("=" * 50)
    print(f"Generated for {len(ksi_codes)} KSIs\n")
    
    for ksi_code in ksi_codes:
        if ksi_code in explanations:
            ksi = explanations[ksi_code]
            print(f"\n{ksi_code}: {ksi['title']}")
            print("-" * 60)
            print(f"Evidence Type: {ksi['evidence_type']}")
            print(f"Passing Criteria: {ksi['passing_criteria']}")
            print("\nLogic Flow:")
            print(ksi['logic'])
            print("\n" + "="*60)

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
            print("  python ksi_explainer.py --interactive     # Interactive mode")
            print("  python ksi_explainer.py --summary         # Show assessment summary")
            print("  python ksi_explainer.py --categories      # Show KSIs by category")
            print("  python ksi_explainer.py --report          # Generate full report")
            print("  python ksi_explainer.py KSI_CNA_01        # Explain specific KSI")
            print("  python ksi_explainer.py --report KSI_CNA_01 KSI_IAM_01  # Report for specific KSIs")
    else:
        # Default: Interactive mode
        interactive_mode()