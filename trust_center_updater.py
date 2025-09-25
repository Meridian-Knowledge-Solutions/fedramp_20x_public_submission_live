"""
Trust Center Finalizer & Style Enhancer
This script reverts the JavaScript to fetch dates from the canonical JSON source,
injects professional styling for form elements and buttons, replaces alerts with
custom modals, and cleans up the page layout for a better user experience.
"""

import re
from pathlib import Path
import shutil

def backup_file(filepath):
    """Create a backup of the original file to prevent data loss."""
    backup_path = f"{filepath}.backup.{Path(filepath).stat().st_mtime_ns}"
    shutil.copy2(filepath, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return backup_path

def finalize_trust_center():
    """Applies final JavaScript corrections and visual enhancements to index.html."""
    html_file = Path("index.html")

    if not html_file.exists():
        print(f"❌ Error: {html_file} not found. Please run this script in the correct directory.")
        return False

    print("🚀 Starting Trust Center finalization process...")
    backup_file(html_file)

    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # --- 1. Correct the JavaScript to fetch from JSON ---
        print("🔄 Restoring JavaScript to fetch dates from JSON...")
        correct_js_function = r'''async function loadQuarterlyReportData() {
    try {
        // Load the next report dates from the JSON file created by the Python script
        const response = await fetch('./trust_center/next_report_date.json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();

        // Update the display elements using the data from the file
        if (data.next_ongoing_report) {
            const reportDate = new Date(data.next_ongoing_report + 'T00:00:00Z'); // Assume UTC midnight
            document.getElementById('next-report-date').textContent =
                reportDate.toLocaleDateString('en-US', {
                    year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC'
                });
        }

        if (data.next_quarterly_review) {
            document.getElementById('next-quarterly-review').textContent = data.next_quarterly_review + ' at 2:00 PM ET';
        }

        // Update current quarter display
        const now = new Date();
        const quarter = Math.floor((now.getMonth() + 3) / 3);
        const year = now.getFullYear();
        document.getElementById('current-quarter-report').textContent =
            `Q${quarter} ${year} - Available`;

    } catch (error) {
        console.error('Could not load quarterly report schedule from JSON:', error);
        document.getElementById('next-report-date').textContent = 'Check back soon';
        document.getElementById('next-quarterly-review').textContent = 'Schedule pending';
    }
}'''
        js_pattern = re.compile(r"async function loadQuarterlyReportData\(\) \{.*?\n\}", re.DOTALL)
        if js_pattern.search(html_content):
            html_content = js_pattern.sub(correct_js_function, html_content)
            print("✅ JavaScript date logic has been corrected.")
        else:
            print("⚠️ Warning: Could not find the loadQuarterlyReportData function to replace.")

        # --- 2. Fix the Quick Access Grid Layout ---
        print("🎨 Cleaning up the Quick Access Grid layout...")
        correct_quick_access_grid = r'''<div class="quick-access-grid">
                <div class="access-card">
                    <div class="card-icon">🔧</div>
                    <h3>API Access</h3>
                    <p>Machine-readable authorization data</p>
                    <button onclick="scrollToTrustSection('api-section')" class="access-btn">View API Docs</button>
                </div>
                <div class="access-card">
                    <div class="card-icon">📋</div>
                    <h3>Request Access</h3>
                    <p>Federal agency request workflow</p>
                    <button onclick="scrollToTrustSection('agency-form-section')" class="access-btn">Submit Request</button>
                </div>
                <div class="access-card enhancement-indicator">
                    <div class="card-icon">📊</div>
                    <h3>Risk-Based POA&M</h3>
                    <p>Multi-level risk tracking</p>
                    <button onclick="window.showPOAMModal()" class="access-btn">View POA&M</button>
                </div>
                <div class="access-card">
                    <div class="card-icon">📋</div>
                    <h3>Quarterly Authorization Reports</h3>
                    <p>RFC-0016 Ongoing Authorization Reports</p>
                    <button onclick="scrollToTrustSection('quarterly-reports-section')" class="access-btn">View Reports</button>
                </div>
            </div>'''
        grid_pattern = re.compile(r'<div class="quick-access-grid">.*?</div>', re.DOTALL)
        if grid_pattern.search(html_content):
            html_content = grid_pattern.sub(correct_quick_access_grid, html_content, count=1)
            print("✅ Quick Access Grid has been rebuilt and cleaned.")
        else:
            print("⚠️ Warning: Could not find quick-access-grid to replace.")

        # --- 3. Inject Modals HTML, CSS, and supporting JavaScript ---
        print("✨ Injecting custom modals to replace browser alerts...")

        # HTML for custom modals
        modals_html = r'''
<!-- Custom Registration Modal -->
<div class="custom-modal" id="registration-modal">
    <div class="custom-modal-content">
        <div class="custom-modal-header">
            <h3>📅 Quarterly Review Registration</h3>
            <button class="modal-close-btn" onclick="closeCustomModal('registration-modal')">&times;</button>
        </div>
        <div class="custom-modal-body">
            <div class="registration-info">
                <p><strong>Federal agencies can register for upcoming quarterly reviews.</strong></p>
                <div class="requirements-box">
                    <h4>Registration Requirements:</h4>
                    <ul>
                        <li>Valid .gov or .mil email address</li>
                        <li>Agency security representative</li>
                        <li>Current FedRAMP authorization</li>
                    </ul>
                </div>
                <div class="contact-info">
                    <h4>Contact Information:</h4>
                    <p><strong>Email:</strong> security@meridianks.com</p>
                    <p><strong>Subject:</strong> "Quarterly Review Registration"</p>
                </div>
                <div class="template-box">
                    <h4>Please Include:</h4>
                    <ul>
                        <li>Agency name and component</li>
                        <li>Primary security contact</li>
                        <li>Current authorization details</li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="custom-modal-footer">
            <button onclick="openEmailClient('registration')" class="modal-btn primary">Open Email Client</button>
            <button onclick="closeCustomModal('registration-modal')" class="modal-btn secondary">Cancel</button>
        </div>
    </div>
</div>

<!-- Custom Feedback Modal -->
<div class="custom-modal" id="feedback-modal">
    <div class="custom-modal-content">
        <div class="custom-modal-header">
            <h3>💬 Agency Feedback</h3>
            <button class="modal-close-btn" onclick="closeCustomModal('feedback-modal')">&times;</button>
        </div>
        <div class="custom-modal-body">
            <div class="feedback-info">
                <p><strong>Per RFC-0016 FRR-CCM-04, we maintain an asynchronous mechanism for agency feedback.</strong></p>
                <div class="feedback-types">
                    <h4>Federal agencies may submit:</h4>
                    <ul>
                        <li>Questions about authorization reports</li>
                        <li>Concerns about reported data</li>
                        <li>Requests for clarification</li>
                        <li>Risk tolerance implications</li>
                    </ul>
                </div>
                <div class="privacy-notice">
                    <h4>📋 Privacy Notice:</h4>
                    <p>Per FRR-CCM-05, agency feedback is shared only with FedRAMP and the submitting agency. Responses are not published publicly.</p>
                </div>
                <div class="contact-methods">
                    <h4>Contact Methods:</h4>
                    <ul>
                        <li><strong>Email:</strong> agency-feedback@meridianks.com</li>
                        <li><strong>Secure Portal:</strong> [Agency Access Only]</li>
                        <li><strong>Phone:</strong> [Agency Hotline]</li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="custom-modal-footer">
            <button onclick="openEmailClient('feedback')" class="modal-btn primary">Open Secure Feedback Channel</button>
            <button onclick="closeCustomModal('feedback-modal')" class="modal-btn secondary">Cancel</button>
        </div>
    </div>
</div>
'''
        # Inject modal HTML before the closing body tag
        html_content = html_content.replace('</body>', modals_html + '\n</body>')
        print("✅ Custom modal HTML has been injected.")

        # CSS for modals and layout enhancements
        visual_enhancement_css = r'''
/* --- Injected QoL Visual Styles for Trust Center --- */
.trust-section form {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
}
.trust-section .form-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.25rem;
}
.trust-section .form-field {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}
.trust-section label {
    font-weight: 600;
    color: var(--text-primary);
    font-size: 0.875rem;
}
.trust-section input[type="text"],
.trust-section input[type="email"],
.trust-section select,
.trust-section textarea {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 2px solid var(--border-color);
    border-radius: var(--radius-sm);
    background-color: var(--bg-secondary);
    color: var(--text-primary);
    font-size: 1rem;
    transition: all 0.2s ease-in-out;
    box-shadow: var(--shadow-sm);
}
.trust-section input[type="text"]:focus,
.trust-section input[type="email"]:focus,
.trust-section select:focus,
.trust-section textarea:focus {
    outline: none;
    border-color: var(--primary-500);
    box-shadow: 0 0 0 3px rgba(30, 64, 175, 0.2);
}
.trust-section .checkbox-field {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    font-size: 0.875rem;
}
.trust-section input[type="checkbox"] {
    width: 1.25em;
    height: 1.25em;
    accent-color: var(--primary-500);
}
.trust-section .form-submit-btn {
    background: var(--gradient-enhancement);
    color: white;
    font-weight: 700;
    font-size: 1rem;
    border: none;
    padding: 0.875rem 1.5rem;
    border-radius: var(--radius-sm);
    cursor: pointer;
    transition: all 0.2s ease-in-out;
    box-shadow: var(--shadow);
    align-self: flex-start;
}
.trust-section .form-submit-btn:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}
.schedule-btn, .method-button {
    background: var(--gradient-enhancement);
    color: white;
    font-weight: 600;
    font-size: 0.875rem;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: var(--radius-sm);
    cursor: pointer;
    transition: all 0.2s ease-in-out;
    box-shadow: var(--shadow);
    text-decoration: none;
    display: inline-block;
}
.schedule-btn:hover, .method-button:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}
.schedule-item {
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    transition: all 0.2s ease;
}
.schedule-item:hover {
    border-color: var(--primary-500);
    transform: scale(1.01);
}
.schedule-status {
    background: rgba(16, 185, 129, 0.1);
    color: var(--success-600);
    border: 1px solid rgba(16, 185, 129, 0.2);
    font-weight: 700;
    padding: 0.25rem 0.75rem;
    border-radius: var(--radius-lg);
}
.access-method {
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    padding: 1.5rem;
    transition: all 0.2s ease;
    border-radius: var(--radius-lg);
}
.access-method:hover {
    border-color: var(--primary-500);
    box-shadow: var(--shadow-lg);
}
.method-link {
    color: var(--primary-500);
    text-decoration: none;
    font-weight: 600;
    transition: all 0.2s ease;
    padding: 0.25rem 0.5rem;
    border-radius: var(--radius-sm);
}
.method-link:hover {
    color: var(--primary-600);
    background-color: var(--bg-accent);
    text-decoration: underline;
}
[data-theme="dark"] .method-link { color: #60a5fa; }
[data-theme="dark"] .method-link:hover { color: #93c5fd; }

/* Custom Modal Styles */
.custom-modal { display: none; position: fixed; z-index: 10000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.7); backdrop-filter: blur(5px); }
.custom-modal.active { display: flex; align-items: center; justify-content: center; padding: 2rem; }
.custom-modal-content { background: var(--bg-primary); border-radius: var(--radius-lg); width: 100%; max-width: 600px; max-height: 80vh; overflow: hidden; box-shadow: var(--shadow-xl); border: 1px solid var(--border-color); display: flex; flex-direction: column; }
.custom-modal-header { background: var(--gradient-accent); color: white; padding: 1.5rem 2rem; display: flex; justify-content: space-between; align-items: center; }
.custom-modal-header h3 { margin: 0; font-size: 1.25rem; font-weight: 700; }
.modal-close-btn { background: none; border: none; color: white; font-size: 1.5rem; cursor: pointer; padding: 0.25rem; opacity: 0.8; transition: opacity 0.3s ease; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
.modal-close-btn:hover { opacity: 1; background: rgba(255, 255, 255, 0.1); }
.custom-modal-body { padding: 2rem; overflow-y: auto; flex: 1; }
.custom-modal-footer { padding: 1.5rem 2rem; border-top: 1px solid var(--border-color); display: flex; gap: 1rem; justify-content: flex-end; }
.modal-btn { padding: 0.75rem 1.5rem; border: none; border-radius: var(--radius-sm); font-weight: 600; cursor: pointer; transition: all 0.2s ease; font-size: 0.9rem; }
.modal-btn.primary { background: var(--gradient-accent); color: white; box-shadow: var(--shadow-sm); }
.modal-btn.primary:hover { transform: translateY(-2px); box-shadow: var(--shadow); }
.modal-btn.secondary { background: var(--bg-accent); color: var(--text-primary); border: 1px solid var(--border-color); }
.modal-btn.secondary:hover { background: var(--border-color); }
.requirements-box, .contact-info, .template-box, .feedback-types, .privacy-notice, .contact-methods { background: var(--bg-accent); padding: 1.5rem; border-radius: var(--radius-sm); margin: 1rem 0; border: 1px solid var(--border-color); }
.requirements-box h4, .contact-info h4, .template-box h4, .feedback-types h4, .privacy-notice h4, .contact-methods h4 { margin: 0 0 0.75rem 0; color: var(--text-primary); font-size: 1rem; }
.requirements-box ul, .template-box ul, .feedback-types ul, .contact-methods ul { margin: 0; padding-left: 1.25rem; color: var(--text-secondary); }
.requirements-box li, .template-box li, .feedback-types li, .contact-methods li { margin: 0.5rem 0; }
.privacy-notice { background: rgba(245, 158, 11, 0.1); border-color: var(--warning-500); }
.privacy-notice h4 { color: var(--warning-600); }
.access-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: var(--gradient-accent); }
.access-card:hover { transform: translateY(-5px); box-shadow: var(--shadow-xl); border-color: var(--primary-500); }
.access-card .card-icon { font-size: 3rem; margin-bottom: 1rem; display: block; }
.access-card h3 { color: var(--text-primary); margin: 0 0 0.75rem 0; font-size: 1.25rem; }
.access-card p { color: var(--text-secondary); margin: 0 0 1.5rem 0; font-size: 0.9rem; line-height: 1.5; }
.access-btn { background: var(--gradient-accent); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: var(--radius-sm); cursor: pointer; font-weight: 600; transition: all 0.2s ease; box-shadow: var(--shadow-sm); font-size: 0.9rem; }
.access-btn:hover { transform: translateY(-2px); box-shadow: var(--shadow); }
@media (max-width: 768px) { .quick-access-grid { grid-template-columns: 1fr; gap: 1rem; } .custom-modal-content { margin: 1rem; max-width: none; } .custom-modal-footer { flex-direction: column; } .modal-btn { width: 100%; } }
'''
        css_injection_pattern = re.compile(r"(\s*</style>)", re.DOTALL)
        if css_injection_pattern.search(html_content):
            html_content = css_injection_pattern.sub(visual_enhancement_css + r'\1', html_content)
            print("✅ New CSS for modals and layouts has been successfully injected.")
        else:
            print("⚠️ Warning: Could not find closing </style> tag to inject CSS.")

        # JavaScript functions for new modals
        new_js_functions = r'''// --- Injected Functions for Custom Modals ---
function registerForReview() {
    document.getElementById('registration-modal').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function openAgencyFeedback() {
    document.getElementById('feedback-modal').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeCustomModal(modalId) {
    document.getElementById(modalId).classList.remove('active');
    document.body.style.overflow = '';
}

function openEmailClient(type) {
    let subject, body, email;
    if (type === 'registration') {
        email = 'security@meridianks.com';
        subject = encodeURIComponent('Quarterly Review Registration');
        body = encodeURIComponent(`Agency: [Your Agency]\nComponent: [Your Component/Bureau]\nPrimary Contact: [Name and Title]\nEmail: [Contact Email]\nAuthorization: [Current ATO/FedRAMP Details]\n\nPlease register us for the upcoming quarterly review.`);
        closeCustomModal('registration-modal');
    } else if (type === 'feedback') {
        email = 'agency-feedback@meridianks.com';
        subject = encodeURIComponent('Agency Feedback - Ongoing Authorization Report');
        body = encodeURIComponent('Please provide your feedback on the ongoing authorization reports.');
        closeCustomModal('feedback-modal');
    }
    window.location.href = `mailto:${email}?subject=${subject}&body=${body}`;
}

// Global listeners for modals
document.addEventListener('click', function(e) {
    if (e.target.classList.contains('custom-modal')) {
        closeCustomModal(e.target.id);
    }
});
'''
        # Replace old JS functions that used confirm()
        old_js_pattern = re.compile(r"function registerForReview\(\) \{.*?\}", re.DOTALL)
        html_content = old_js_pattern.sub("", html_content)
        old_js_pattern_2 = re.compile(r"function openAgencyFeedback\(\) \{.*?\}", re.DOTALL)
        html_content = old_js_pattern_2.sub("", html_content)

        # Add new functions and listeners to the main script block
        html_content = html_content.replace('// Global functions', new_js_functions + '\n// Global functions')
        print("✅ JavaScript functions updated to use custom modals.")

        # --- 4. Write all changes back to the file ---
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print("\n🎉 Trust Center finalization complete!")
        print("   - JavaScript is now correctly fetching authoritative dates.")
        print("   - Browser alerts have been replaced with professional custom modals.")
        print("   - The Trust Center layout and styling have been significantly improved.")
        print("   - The original file has been backed up for safety.")
        return True

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    finalize_trust_center()
