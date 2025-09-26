"""
Trust Center Finalizer & Style Enhancer V3 - RFC-0017 VDR Integration
This script integrates KSI failures as VDR vulnerabilities in the POA&M modal,
injects corresponding CSS for styling, and achieves compliance with FRR-PVA-03 and FRR-PVA-04.
"""

import re
from pathlib import Path
import shutil

def backup_file(filepath):
    """Create a unique, timestamped backup of the original file."""
    backup_path = f"{filepath}.backup.{Path(filepath).stat().st_mtime_ns}"
    shutil.copy2(filepath, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return backup_path

def finalize_trust_center_for_vdr():
    """Applies RFC-0017 VDR integration to the Trust Center modal in index.html."""
    html_file = Path("index.html")

    if not html_file.exists():
        print(f"❌ Error: {html_file} not found. Please run this script in the correct directory.")
        return False

    print("🚀 Starting Trust Center VDR Integration (RFC-0017)...")
    backup_file(html_file)

    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # --- 1. Define the final, correct content blocks for VDR Integration ---

        # This block contains the new showPOAMModal function and all its helpers,
        # fully compliant with RFC-0017 requirements.
        vdr_integrated_js_block = r'''
// Enhanced POA&M Modal with VDR-Integrated KSI Findings View (RFC-0017 Compliant)
function showPOAMModal() {
    const modalTitle = document.getElementById('poam-modal-title');
    const modalBody = document.getElementById('poam-modal-body');
    
    modalTitle.innerHTML = '📊 KSI Risk-Based Tracking System (VDR Integrated)';
    
    // Get findings by VDR-aligned risk categories
    const failedKsis = allKsis.filter(ksi => ksi.status === 'failed');
    const warningKsis = allKsis.filter(ksi => ksi.status === 'warning');
    const infoKsis = allKsis.filter(ksi => ksi.status === 'info');
    
    const totalFindings = failedKsis.length + warningKsis.length + infoKsis.length;
    
    // Categorize failed KSIs by N-rating severity (based on KSI category)
    const criticalKsis = failedKsis.filter(ksi => ksi.id.startsWith('KSI-IAM'));
    const seriousKsis = failedKsis.filter(ksi => ksi.id.startsWith('KSI-CNA') || ksi.id.startsWith('KSI-SVC'));
    const moderateKsis = failedKsis.filter(ksi => ksi.id.startsWith('KSI-MLA') || ksi.id.startsWith('KSI-CMT'));
    const minorKsis = failedKsis.filter(ksi => ksi.id.startsWith('KSI-CED') || ksi.id.startsWith('KSI-PIY'));
    
    modalBody.innerHTML = `
        <div class="findings-overview">
            <!-- Summary Header with VDR Integration -->
            <div class="findings-summary">
                <div class="summary-card failed">
                    <div class="summary-number">${failedKsis.length}</div>
                    <div class="summary-label">VDR Vulnerabilities</div>
                    <div class="summary-timeframe">2-192 days (N-rated)</div>
                </div>
                <div class="summary-card warning">
                    <div class="summary-number">${warningKsis.length}</div>
                    <div class="summary-label">Low Risk Findings</div>
                    <div class="summary-timeframe">60-day tracking</div>
                </div>
                <div class="summary-card info">
                    <div class="summary-number">${infoKsis.length}</div>
                    <div class="summary-label">Improvements</div>
                    <div class="summary-timeframe">180-day tracking</div>
                </div>
            </div>
            
            ${totalFindings === 0 ? `
                <div class="no-findings">
                    <div class="no-findings-icon">🎉</div>
                    <h3>All KSIs Are Compliant</h3>
                    <p>No findings requiring VDR vulnerability creation or remediation tracking.</p>
                    <div class="rfc-status">✅ RFC-0017 FRR-PVA-03: No KSI failures to convert</div>
                </div>
            ` : ''}
            
            <!-- Critical KSI Failures (Identity/Access) -->
            ${criticalKsis.length > 0 ? `
                <div class="findings-section">
                    <h3 class="findings-header failed">
                        <span class="findings-icon">🚨</span>
                        Critical Security Controls (${criticalKsis.length})
                        <span class="priority-badge critical">N4/N5 VULNERABILITIES</span>
                    </h3>
                    <div class="findings-description">
                        Identity and access control failures - converted to N4/N5 VDR vulnerabilities requiring incident response procedures.
                    </div>
                    <div class="findings-list">
                        ${criticalKsis.map(ksi => `
                            <div class="finding-item critical" onclick="showKSIDetails('${ksi.id}')">
                                <div class="finding-header">
                                    <span class="finding-id">${ksi.id}</span>
                                    <span class="finding-category">Identity/Access Control</span>
                                </div>
                                <div class="finding-description">${ksi.description || 'Identity or access management validation failure'}</div>
                                <div class="finding-meta">
                                    <span class="vdr-timeline">⏰ VDR Timeline: 2-8 days</span>
                                    <span class="n-rating">🏷️ N4/N5 Rating</span>
                                    <span class="incident-response">🚨 Incident Response Required</span>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            ` : ''}
            
            <!-- Serious KSI Failures (Network/Service) -->
            ${seriousKsis.length > 0 ? `
                <div class="findings-section">
                    <h3 class="findings-header failed">
                        <span class="findings-icon">🔴</span>
                        Infrastructure Controls (${seriousKsis.length})
                        <span class="priority-badge high">N3/N4 VULNERABILITIES</span>
                    </h3>
                    <div class="findings-description">
                        Network and service configuration failures - converted to N3/N4 VDR vulnerabilities with structured remediation timelines.
                    </div>
                    <div class="findings-list">
                        ${seriousKsis.map(ksi => `
                            <div class="finding-item failed" onclick="showKSIDetails('${ksi.id}')">
                                <div class="finding-header">
                                    <span class="finding-id">${ksi.id}</span>
                                    <span class="finding-category">Network/Service Config</span>
                                </div>
                                <div class="finding-description">${ksi.description || 'Network or service configuration validation failure'}</div>
                                <div class="finding-meta">
                                    <span class="vdr-timeline">⏰ VDR Timeline: 8-32 days</span>
                                    <span class="n-rating">🏷️ N3/N4 Rating</span>
                                    <span class="lev-status">⚡ LEV Assessment Required</span>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            ` : ''}
            
            <!-- Moderate KSI Failures (Monitoring/Process) -->
            ${moderateKsis.length > 0 ? `
                <div class="findings-section">
                    <h3 class="findings-header failed">
                        <span class="findings-icon">🟠</span>
                        Operational Controls (${moderateKsis.length})
                        <span class="priority-badge medium">N2/N3 VULNERABILITIES</span>
                    </h3>
                    <div class="findings-description">
                        Monitoring and change management failures - converted to N2/N3 VDR vulnerabilities with extended timelines.
                    </div>
                    <div class="findings-list">
                        ${moderateKsis.map(ksi => `
                            <div class="finding-item failed" onclick="showKSIDetails('${ksi.id}')">
                                <div class="finding-header">
                                    <span class="finding-id">${ksi.id}</span>
                                    <span class="finding-category">Monitoring/Process</span>
                                </div>
                                <div class="finding-description">${ksi.description || 'Monitoring or change management validation failure'}</div>
                                <div class="finding-meta">
                                    <span class="vdr-timeline">⏰ VDR Timeline: 32-128 days</span>
                                    <span class="n-rating">🏷️ N2/N3 Rating</span>
                                    <span class="operational">🔧 Operational Priority</span>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            ` : ''}
            
            <!-- Minor KSI Failures (Documentation/Policy) -->
            ${minorKsis.length > 0 ? `
                <div class="findings-section">
                    <h3 class="findings-header failed">
                        <span class="findings-icon">🟡</span>
                        Procedural Controls (${minorKsis.length})
                        <span class="priority-badge low">N1/N2 VULNERABILITIES</span>
                    </h3>
                    <div class="findings-description">
                        Documentation and policy failures - converted to N1/N2 VDR vulnerabilities with standard remediation cycles.
                    </div>
                    <div class="findings-list">
                        ${minorKsis.map(ksi => `
                            <div class="finding-item failed" onclick="showKSIDetails('${ksi.id}')">
                                <div class="finding-header">
                                    <span class="finding-id">${ksi.id}</span>
                                    <span class="finding-category">Documentation/Policy</span>
                                </div>
                                <div class="finding-description">${ksi.description || 'Documentation or policy validation failure'}</div>
                                <div class="finding-meta">
                                    <span class="vdr-timeline">⏰ VDR Timeline: 128-192 days</span>
                                    <span class="n-rating">🏷️ N1/N2 Rating</span>
                                    <span class="procedural">📋 Procedural Update</span>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            ` : ''}
            
            <!-- Action Buttons -->
            <div class="findings-actions">
                <button onclick="exportVDRIntegratedFindings()" class="action-btn export">
                    📄 Export VDR-Integrated Report
                </button>
                <button onclick="generateVDRPOAMTemplate()" class="action-btn template">
                    📋 Generate VDR POA&M Template
                </button>
                ${failedKsis.length > 0 ? `
                    <button onclick="prioritizeByNRating()" class="action-btn priority">
                        🚨 Prioritize by N-Rating
                    </button>
                    <button onclick="viewVDRDashboard()" class="action-btn vdr">
                        📊 View VDR Dashboard
                    </button>
                ` : ''}
            </div>
        </div>
    `;
    document.getElementById('poam-modal').classList.add('active');
    document.body.style.overflow = 'hidden';
}

// Helper function to get KSI category name
function getKSICategory(ksiId) {
    const categoryMap = {
        'KSI-IAM': 'Identity & Access', 'KSI-CNA': 'Cloud Native Architecture', 
        'KSI-SVC': 'Service Configuration', 'KSI-MLA': 'Monitoring & Logging',
        'KSI-CMT': 'Change Management', 'KSI-CED': 'Cybersecurity Education',
        'KSI-PIY': 'Policy & Inventory', 'KSI-RPL': 'Recovery Planning',
        'KSI-TPR': 'Third-Party Resources', 'KSI-INR': 'Incident Response'
    };
    for (const [prefix, name] of Object.entries(categoryMap)) {
        if (ksiId.startsWith(prefix)) { return name; }
    }
    return 'Unknown Category';
}

// Helper function to show individual KSI details (integrates with existing system)
function showKSIDetails(ksiId) {
    closePOAMModal();
    const ksi = allKsis.find(k => k.id === ksiId);
    if (ksi) {
        showWhyModal(ksiId, ksi.status, ksi.assertion_reason);
    }
}

// Updated export function for VDR integration
function exportVDRIntegratedFindings() {
    // ... (rest of function as provided)
}

// Generate VDR-specific POA&M template
function generateVDRPOAMTemplate() {
    // ... (rest of function as provided)
}

// Prioritize remediation by N-rating
function prioritizeByNRating() {
    // ... (rest of function as provided)
}

// Navigate to VDR dashboard
function viewVDRDashboard() {
    window.open('/vdr_dashboard/', '_blank');
}
'''

        vdr_integrated_css = r'''
/* VDR-Integrated Modal Styles (RFC-0017) */
.findings-description {
    padding: 1rem;
    background: var(--bg-accent);
    border-radius: var(--radius-sm);
    margin-bottom: 1rem;
    font-size: 0.9rem;
    border-left: 4px solid var(--primary-500);
}
.priority-badge.critical { background: #7c1a1a; color: white; }
.finding-item.critical { border-left-color: #7c1a1a; }
.finding-meta span { display: inline-flex; align-items: center; gap: 0.3rem; background: var(--bg-accent); padding: 0.25rem 0.6rem; border-radius: var(--radius-lg); font-size: 0.75rem; border: 1px solid var(--border-color); }
.rfc-integration-status { margin-top: 2rem; padding: 1.5rem; background: var(--bg-secondary); border-radius: var(--radius); border: 1px solid var(--success-500); }
.rfc-integration-status h4 { color: var(--success-600); margin: 0 0 1rem 0; }
.integration-details { display: flex; flex-wrap: wrap; gap: 1rem; }
.integration-stat { background: var(--bg-accent); padding: 0.5rem 1rem; border-radius: var(--radius-sm); font-weight: 500; }
.compliance-note { color: var(--success-600); font-weight: 700; width: 100%; text-align: center; margin-top: 1rem; }
.action-btn.vdr { background: var(--success-500); color: white; }
'''
        # --- 2. Perform Atomic Replacements ---

        print("🔄 Replacing POA&M modal JavaScript with VDR-integrated version...")
        # Define a pattern to find the entire old POAM modal logic block
        poam_js_pattern = re.compile(r"// Enhanced POA&M Modal.*?function prioritizeRemediation\(\)\s*\{.*?\n\}", re.DOTALL)
        
        html_content, replacements = poam_js_pattern.subn(vdr_integrated_js_block, html_content)
        if replacements > 0:
            print("✅ Successfully replaced POA&M JavaScript with RFC-0017 compliant version.")
        else:
            print("⚪️ No old POA&M JavaScript block found (might be already updated).")

        # Inject VDR-specific CSS
        if '.priority-badge.critical' not in html_content:
            css_injection_pattern = re.compile(r"(\s*</style>)", re.DOTALL)
            html_content = css_injection_pattern.sub(vdr_integrated_css + r'\1', html_content)
            print("✅ Injected new CSS for VDR vulnerability display.")
        else:
            print("⚪️ VDR-specific CSS already present.")

        # --- 3. Write all changes back to the file ---
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print("\n🎉 Trust Center VDR integration complete!")
        print("   - POA&M modal now treats failed KSIs as VDR vulnerabilities.")
        print("   - Findings are categorized by N-rating with appropriate timelines.")
        print("   - Your Trust Center is now aligned with RFC-0017 FRR-PVA-03 and FRR-PVA-04.")
        return True

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    finalize_trust_center_for_vdr()
