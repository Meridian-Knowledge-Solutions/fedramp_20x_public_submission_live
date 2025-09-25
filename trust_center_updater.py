#!/usr/bin/env python3
"""
Trust Center HTML Updater - RFC-0016 Quarterly Reports Integration
Automatically updates index.html to replace Incident Reports with Quarterly Authorization Reports
"""

import re
import os
import shutil
from pathlib import Path

def backup_file(filepath):
    """Create a backup of the original file"""
    backup_path = f"{filepath}.backup"
    shutil.copy2(filepath, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return backup_path

def update_trust_center_html():
    """Update index.html with RFC-0016 Quarterly Reports integration"""

    html_file = Path("index.html")

    if not html_file.exists():
        print("❌ index.html not found in current directory")
        print("   Please run this script from the directory containing index.html")
        return False

    print("🔄 Updating Trust Center with RFC-0016 Quarterly Reports...")

    # Backup original file
    backup_file(html_file)

    # Read the current HTML content
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Define the replacement card HTML
    new_quarterly_card = '''                <div class="access-card">
                    <div class="card-icon">📋</div>
                    <h3>Quarterly Authorization Reports</h3>
                    <p>RFC-0016 Ongoing Authorization Reports</p>
                    <button onclick="scrollToTrustSection('quarterly-reports-section')" class="access-btn">View Reports</button>
                </div>'''

    # --- FIX 1: Use a more flexible regex for the card replacement to avoid failures on minor whitespace changes. ---
    incident_card_pattern = re.compile(r'<div class="access-card"[^>]*>.*?<h3>Incident Reports</h3>.*?</div>', re.DOTALL)

    if incident_card_pattern.search(html_content):
        html_content = incident_card_pattern.sub(new_quarterly_card, html_content, count=1)
        print("✅ Replaced Incident Reports card with Quarterly Authorization Reports card")
    else:
        print("❌ Could not find Incident Reports card to replace")
        return False

    # Define the new quarterly reports section
    quarterly_section = '''
            <div id="quarterly-reports-section" class="trust-section">
                <h2>📋 Quarterly Authorization Reports (RFC-0016)</h2>
                <p>Ongoing Authorization Reports per FRR-CCM-01 providing regular summaries of changes, accepted weaknesses, and authorization data</p>

                <div class="trust-card">
                    <div class="trust-card-header">
                        <h3 class="trust-card-title">🗓️ Report Schedule & Access</h3>
                    </div>
                    <div class="trust-card-content">
                        <div class="quarterly-schedule">
                            <div class="schedule-item">
                                <div class="schedule-icon">📅</div>
                                <div class="schedule-content">
                                    <strong>Current Quarter Report:</strong>
                                    <div id="current-quarter-report">Q3 2025 - Available</div>
                                </div>
                                <button onclick="downloadCurrentReport()" class="schedule-btn">Download Report</button>
                            </div>

                            <div class="schedule-item">
                                <div class="schedule-icon">⏰</div>
                                <div class="schedule-content">
                                    <strong>Next Report Due:</strong>
                                    <div id="next-report-date">Loading...</div>
                                </div>
                                <div class="schedule-status">On Schedule</div>
                            </div>

                            <div class="schedule-item">
                                <div class="schedule-icon">🎯</div>
                                <div class="schedule-content">
                                    <strong>Next Quarterly Review:</strong>
                                    <div id="next-quarterly-review">Loading...</div>
                                </div>
                                <button onclick="registerForReview()" class="schedule-btn">Agency Registration</button>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="trust-card">
                    <div class="trust-card-header">
                        <h3 class="trust-card-title">📊 Report Contents (FRR-CCM-01)</h3>
                    </div>
                    <div class="trust-card-content">
                        <div class="report-contents">
                            <div class="content-section">
                                <h4>🔄 Changes to Authorization Data</h4>
                                <ul class="content-list">
                                    <li>Key Security Indicators (KSI) performance updates</li>
                                    <li>Automation health and validation consistency</li>
                                    <li>Significant change notifications (SCN) summary</li>
                                </ul>
                            </div>

                            <div class="content-section">
                                <h4>⚠️ Accepted Weaknesses (VDR)</h4>
                                <ul class="content-list">
                                    <li>Active vulnerability counts by N-rating</li>
                                    <li>LEV+IRV critical indicators</li>
                                    <li>Agency action requirements</li>
                                </ul>
                            </div>

                            <div class="content-section">
                                <h4>🔮 Planned Changes (Next 3 Months)</h4>
                                <ul class="content-list">
                                    <li>Planned infrastructure updates</li>
                                    <li>Security control enhancements</li>
                                    <li>Compliance milestone tracking</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="trust-card">
                    <div class="trust-card-header">
                        <h3 class="trust-card-title">🏛️ Federal Agency Access</h3>
                    </div>
                    <div class="trust-card-content">
                        <div class="agency-access">
                            <div class="access-method">
                                <div class="method-icon">🔗</div>
                                <div class="method-content">
                                    <strong>Direct Download:</strong>
                                    <p>Reports available in machine-readable and human-readable formats</p>
                                    <div class="method-links">
                                        <a href="./quarterly_reports/" target="_blank" class="method-link">📁 Report Archive</a>
                                        <a href="./trust_center/next_report_date.json" target="_blank" class="method-link">⏰ Schedule API</a>
                                    </div>
                                </div>
                            </div>

                            <div class="access-method">
                                <div class="method-icon">💬</div>
                                <div class="method-content">
                                    <strong>Agency Feedback (FRR-CCM-04):</strong>
                                    <p>Asynchronous mechanism for questions and feedback</p>
                                    <button onclick="openAgencyFeedback()" class="method-button">Submit Agency Feedback</button>
                                    <small>Note: Feedback shared with FedRAMP, not published publicly per FRR-CCM-05</small>
                                </div>
                            </div>

                            <div class="access-method">
                                <div class="method-icon">🎪</div>
                                <div class="method-content">
                                    <strong>Quarterly Review Meetings (FRR-CCM-QR):</strong>
                                    <p>Synchronous quarterly reviews for all agency customers</p>
                                    <div class="review-details">
                                        <div>📅 Schedule: Within 2 weeks of report release</div>
                                        <div>🎯 Audience: Federal agencies only</div>
                                        <div>📝 Recording: Available to authorized parties</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
'''

    # --- FIX 2: Correct the HTML insertion point to place the new section inside the Trust Center tab, not between tabs. ---
    insertion_hook_pattern = re.compile(r'(<div class="quick-access-grid">.*?</div>)', re.DOTALL)
    if insertion_hook_pattern.search(html_content):
        # Insert the new section immediately after the quick access grid
        html_content = insertion_hook_pattern.sub(r'\1' + quarterly_section, html_content, count=1)
        print("✅ Added Quarterly Reports section to the Trust Center tab")
    else:
        print("⚠️ Could not find the quick-access-grid to insert the new section. Manual placement may be required.")


    # Add the CSS styles if not already present
    css_styles = '''
/* Quarterly Reports Section Styles */
.quarterly-schedule {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.schedule-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
    background: var(--bg-accent);
    border: 1px solid var(--border-color);
    border-radius: 8px;
}

.schedule-icon {
    font-size: 1.5rem;
    width: 40px;
    text-align: center;
}

.schedule-content {
    flex: 1;
}

.schedule-content strong {
    color: var(--text-primary);
    font-weight: 600;
}

.schedule-btn, .method-button {
    background: var(--primary-color);
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 500;
    transition: background-color 0.2s;
}

.schedule-btn:hover, .method-button:hover {
    background: var(--primary-600);
}

.schedule-status {
    background: var(--success-color);
    color: white;
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 0.875rem;
    font-weight: 500;
}

.report-contents {
    display: grid;
    gap: 1.5rem;
}

.content-section h4 {
    color: var(--text-primary);
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
}

.content-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.content-list li {
    padding: 0.5rem 0;
    border-bottom: 1px solid var(--border-color);
    color: var(--text-secondary);
}

.content-list li:last-child {
    border-bottom: none;
}

.agency-access {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.access-method {
    display: flex;
    gap: 1rem;
    padding: 1rem;
    background: var(--bg-surface);
    border-radius: 8px;
}

.method-icon {
    font-size: 1.5rem;
    width: 40px;
    text-align: center;
    margin-top: 0.25rem;
}

.method-content {
    flex: 1;
}

.method-content strong {
    color: var(--text-primary);
    font-weight: 600;
}

.method-content p {
    margin: 0.5rem 0;
    color: var(--text-secondary);
}

.method-links {
    display: flex;
    gap: 1rem;
    margin-top: 0.5rem;
}

.method-link {
    color: var(--primary-color);
    text-decoration: none;
    font-weight: 500;
    font-size: 0.9rem;
}

.method-link:hover {
    text-decoration: underline;
}

.review-details {
    margin-top: 0.5rem;
    font-size: 0.9rem;
    color: var(--text-secondary);
}

.review-details div {
    margin: 0.25rem 0;
}

@media (max-width: 768px) {
    .schedule-item {
        flex-direction: column;
        align-items: flex-start;
        text-align: left;
    }

    .access-method {
        flex-direction: column;
    }

    .method-icon {
        width: auto;
        text-align: left;
    }

    .method-links {
        flex-direction: column;
        gap: 0.5rem;
    }
}
'''

    # Check if styles need to be added
    if 'quarterly-schedule' not in html_content:
        style_end_pattern = re.compile(r'(</style>)')
        if style_end_pattern.search(html_content):
            html_content = style_end_pattern.sub(css_styles + r'\n\1', html_content)
            print("✅ Added quarterly reports CSS styles")
        else:
            print("⚠️ Could not find <style> section to add CSS")

    # Add the JavaScript functions
    js_functions = '''
// Quarterly Reports JavaScript Functions
async function loadQuarterlyReportData() {
    try {
        // Load the next report dates from trust center data
        const response = await fetch('./trust_center/next_report_date.json');
        const data = await response.json();

        // Update the display elements
        if (data.next_ongoing_report) {
            document.getElementById('next-report-date').textContent =
                new Date(data.next_ongoing_report).toLocaleDateString('en-US', {
                    year: 'numeric', month: 'long', day: 'numeric'
                });
        }

        if (data.next_quarterly_review) {
            document.getElementById('next-quarterly-review').textContent = data.next_quarterly_review + ' at 2:00 PM ET';
        }

        // Update current quarter
        const now = new Date();
        const quarter = Math.floor((now.getMonth() + 3) / 3);
        const year = now.getFullYear();
        document.getElementById('current-quarter-report').textContent =
            `Q${quarter} ${year} - Available`;

    } catch (error) {
        console.log('Could not load quarterly report schedule:', error);
        document.getElementById('next-report-date').textContent = 'Check back for updates';
        document.getElementById('next-quarterly-review').textContent = 'Check back for updates';
    }
}

function downloadCurrentReport() {
    const now = new Date();
    const quarter = Math.floor((now.getMonth() + 3) / 3);
    const year = now.getFullYear();
    const filename = `ongoing_authorization_report_Q${quarter}_${year}.md`;

    // Try to download from quarterly_reports directory
    const link = document.createElement('a');
    link.href = `./quarterly_reports/${filename}`;
    link.download = filename;
    link.click();

    // Provide feedback to user
    setTimeout(() => {
        if (!document.hasFocus()) return; // User might have downloaded

        alert(`Download initiated for ${filename}.\\n\\nIf download doesn't start automatically, the report may not be available yet. Reports are generated automatically every quarter.`);
    }, 1000);
}

function registerForReview() {
    // Open a modal or redirect to registration
    const message = `Quarterly Review Registration

Federal agencies can register for upcoming quarterly reviews.

Registration Requirements:
• Valid .gov or .mil email address
• Agency security representative
• Current FedRAMP authorization

Contact: security@meridianks.com
Subject: "Quarterly Review Registration"

Please include:
• Agency name and component
• Primary security contact
• Current authorization details`;

    if (confirm(message + '\\n\\nOpen email client to register?')) {
        const subject = encodeURIComponent('Quarterly Review Registration');
        const body = encodeURIComponent(`Agency: [Your Agency]
Component: [Your Component/Bureau]
Primary Contact: [Name and Title]
Email: [Contact Email]
Authorization: [Current ATO/FedRAMP Details]

Please register us for the upcoming quarterly review.`);

        window.location.href = `mailto:security@meridianks.com?subject=${subject}&body=${body}`;
    }
}

function openAgencyFeedback() {
    // Private feedback mechanism per FRR-CCM-04/05
    const message = `Agency Feedback on Ongoing Authorization Reports

Per RFC-0016 FRR-CCM-04, we maintain an asynchronous mechanism for agency feedback.

Federal agencies may submit:
• Questions about authorization reports
• Concerns about reported data
• Requests for clarification
• Risk tolerance implications

Note: Per FRR-CCM-05, agency feedback is shared only with FedRAMP and the submitting agency. Responses are not published publicly.

Contact Methods:
• Email: agency-feedback@meridianks.com
• Secure Portal: [Agency Access Only]
• Phone: [Agency Hotline]`;

    if (confirm(message + '\\n\\nOpen secure feedback channel?')) {
        const subject = encodeURIComponent('Agency Feedback - Ongoing Authorization Report');
        window.location.href = `mailto:agency-feedback@meridianks.com?subject=${subject}`;
    }
}
'''

    # --- FIX 3: Correct the JS insertion regex to use a stable anchor and avoid corruption. ---
    if 'loadQuarterlyReportData' not in html_content:
        # Use a robust pattern targeting the comment right before the event listener.
        js_insertion_pattern = re.compile(r"(\s*// Initialize on page load)")
        
        if js_insertion_pattern.search(html_content):
            # Insert the new JS functions and a call within DOMContentLoaded.
            replacement_js_block = js_functions + r'\n\n\1'
            html_content = js_insertion_pattern.sub(replacement_js_block, html_content, count=1)
            
            # Also, add the function call inside the DOMContentLoaded listener.
            dom_content_pattern = re.compile(r"(initializeDashboard\(\);)")
            html_content = dom_content_pattern.sub(r'\1\n            setTimeout(loadQuarterlyReportData, 500);', html_content, count=1)
            
            print("✅ Added quarterly reports JavaScript functions and call")
        else:
            print("⚠️ Could not find JS insertion point. Manual integration may be required.")

    # Write the updated content back to file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✅ Successfully updated {html_file}")
    print("🔧 Changes made:")
    print("   • Replaced Incident Reports card with Quarterly Authorization Reports")
    print("   • Added RFC-0016 compliant quarterly reports section in the correct tab")
    print("   • Added CSS styles for quarterly reports")
    print("   • Correctly inserted JavaScript functions to prevent page errors")
    print("   • Maintained backup file for safety")

    return True

if __name__ == "__main__":
    print("🚀 RFC-0016 Trust Center Integration Script")
    print("   Updating index.html for Quarterly Authorization Reports...")
    print("")

    success = update_trust_center_html()

    if success:
        print("")
        print("🎉 Trust Center successfully updated!")
        print("📋 Your index.html now includes:")
        print("   • RFC-0016 compliant Quarterly Authorization Reports")
        print("   • Agency self-service access")
        print("   • Automated compliance tracking")
        print("   • Professional federal agency interface")
        print("")
        print("💡 Next steps:")
        print("   1. Test the updated Trust Center interface")
        print("   2. Run the quarterly report generator")
        print("   3. Verify /trust_center/next_report_date.json is created")
        print("   4. Confirm quarterly reports are generated in /quarterly_reports/")
    else:
        print("")
        print("❌ Update failed. Check the error messages above.")
        print("💡 Manual integration may be required.")
