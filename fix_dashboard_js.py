#!/usr/bin/env python3
"""
Dashboard JavaScript Diagnostic and Fix Script
Fixes JavaScript issues after Trust Center integration
"""

import re
import shutil
from pathlib import Path

def diagnose_and_fix_javascript():
    """Diagnose and fix JavaScript issues in index.html"""
    
    html_file = Path("index.html")
    
    if not html_file.exists():
        print("❌ index.html not found")
        return False
    
    print("🔍 Diagnosing JavaScript issues...")
    
    # Backup current file
    backup_path = f"{html_file}.js-fix-backup"
    shutil.copy2(html_file, backup_path)
    print(f"✅ Backup created: {backup_path}")
    
    # Read content
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🔍 Checking for common JavaScript issues...")
    
    issues_found = []
    fixes_applied = []
    
    # 1. Check for duplicate script tags
    script_tags = re.findall(r'<script[^>]*>', content)
    if len(script_tags) > 3:  # Assuming normal is 1-2 script tags
        issues_found.append(f"Found {len(script_tags)} script tags (possible duplicates)")
    
    # 2. Check for malformed JavaScript strings
    if re.search(r'\\n\\n', content):
        issues_found.append("Found malformed newline escapes")
        content = re.sub(r'\\n', '\n', content)
        fixes_applied.append("Fixed newline escaping")
    
    # 3. Check for missing essential functions
    essential_functions = ['toggleTheme', 'showTab', 'loadQuarterlyReportData']
    missing_functions = []
    
    for func in essential_functions:
        if f'function {func}' not in content and f'{func} =' not in content:
            missing_functions.append(func)
    
    if missing_functions:
        issues_found.append(f"Missing functions: {', '.join(missing_functions)}")
    
    # 4. Fix duplicate quarterly reports JavaScript
    quarterly_js_pattern = r'// Quarterly Reports JavaScript Functions.*?(?=// Load data when the page loads|document\.addEventListener|</script>)'
    quarterly_matches = re.findall(quarterly_js_pattern, content, re.DOTALL)
    
    if len(quarterly_matches) > 1:
        issues_found.append("Duplicate quarterly reports JavaScript found")
        # Remove all but the first occurrence
        content = re.sub(quarterly_js_pattern, '', content, count=len(quarterly_matches)-1, flags=re.DOTALL)
        fixes_applied.append("Removed duplicate quarterly reports JavaScript")
    
    # 5. Check for broken script closure
    if content.count('<script>') != content.count('</script>'):
        issues_found.append("Mismatched script tags")
    
    # 6. Fix common quote escaping issues in JavaScript
    if re.search(r'\\n\\nOpen ', content):
        content = re.sub(r'\\n\\n', '\\n\\n', content)
        fixes_applied.append("Fixed quote escaping in JavaScript strings")
    
    # 7. Ensure essential functions exist - add minimal versions if missing
    if 'toggleTheme' in missing_functions:
        print("🔧 Adding missing toggleTheme function...")
        theme_function = '''
function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
}'''
        
        # Find a good place to insert it
        script_pattern = r'(<script[^>]*>)'
        if re.search(script_pattern, content):
            content = re.sub(script_pattern, r'\1' + theme_function, content, count=1)
            fixes_applied.append("Added missing toggleTheme function")
    
    if 'showTab' in missing_functions:
        print("🔧 Adding missing showTab function...")
        tab_function = '''
function showTab(tabName) {
    // Hide all tabs
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.style.display = 'none');
    
    // Remove active class from all buttons
    const buttons = document.querySelectorAll('.tab-btn');
    buttons.forEach(btn => btn.classList.remove('active'));
    
    // Show selected tab
    const selectedTab = document.getElementById(tabName + '-tab');
    if (selectedTab) {
        selectedTab.style.display = 'block';
    }
    
    // Add active class to clicked button
    const selectedBtn = document.querySelector(`[onclick*="${tabName}"]`);
    if (selectedBtn) {
        selectedBtn.classList.add('active');
    }
}'''
        
        # Insert after the toggleTheme function or at start of script
        if 'function toggleTheme' in content:
            content = content.replace('function toggleTheme', tab_function + '\n\nfunction toggleTheme')
        else:
            script_pattern = r'(<script[^>]*>)'
            content = re.sub(script_pattern, r'\1' + tab_function, content, count=1)
        fixes_applied.append("Added missing showTab function")
    
    # 8. Ensure proper script initialization
    if 'DOMContentLoaded' not in content:
        print("🔧 Adding DOMContentLoaded initialization...")
        init_script = '''
// Initialize dashboard when page loads
document.addEventListener('DOMContentLoaded', function() {
    // Show first tab by default
    showTab('ksi-dashboard');
    
    // Load quarterly report data if function exists
    if (typeof loadQuarterlyReportData === 'function') {
        setTimeout(loadQuarterlyReportData, 500);
    }
    
    // Apply saved theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
});'''
        
        # Add before closing script tag
        content = content.replace('</script>', init_script + '\n</script>')
        fixes_applied.append("Added DOMContentLoaded initialization")
    
    # Write fixed content
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Print diagnosis results
    print("\n🔍 Diagnosis Results:")
    if issues_found:
        for issue in issues_found:
            print(f"   ❌ {issue}")
    else:
        print("   ✅ No major issues detected")
    
    print("\n🔧 Fixes Applied:")
    if fixes_applied:
        for fix in fixes_applied:
            print(f"   ✅ {fix}")
    else:
        print("   ℹ️ No automatic fixes needed")
    
    # Final validation
    print("\n🧪 Final Validation:")
    script_count = content.count('<script>')
    print(f"   📊 Script tags: {script_count}")
    print(f"   🔧 toggleTheme: {'✅' if 'toggleTheme' in content else '❌'}")
    print(f"   🔧 showTab: {'✅' if 'showTab' in content else '❌'}")
    print(f"   🔧 DOMContentLoaded: {'✅' if 'DOMContentLoaded' in content else '❌'}")
    
    return True

def quick_minimal_fix():
    """Apply a quick minimal fix for essential functions"""
    print("\n🚑 Applying quick minimal JavaScript fix...")
    
    html_file = Path("index.html")
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Quick fix script - add essential functions if missing
    quick_fix = '''
<script>
// Essential Dashboard Functions - Quick Fix
function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
}

function showTab(tabName) {
    // Hide all tab contents
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.style.display = 'none';
    });
    
    // Remove active class from tab buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    const targetTab = document.getElementById(tabName + '-tab');
    if (targetTab) {
        targetTab.style.display = 'block';
    }
    
    // Add active class to corresponding button
    const targetBtn = document.querySelector(`[onclick*="${tabName}"]`);
    if (targetBtn) {
        targetBtn.classList.add('active');
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    // Set default theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    
    // Show default tab
    setTimeout(() => showTab('ksi-dashboard'), 100);
    
    // Load quarterly data if function exists
    if (typeof loadQuarterlyReportData === 'function') {
        setTimeout(loadQuarterlyReportData, 500);
    }
});
</script>'''
    
    # Add the quick fix before closing body tag if functions are missing
    if 'function toggleTheme' not in content or 'function showTab' not in content:
        content = content.replace('</body>', quick_fix + '\n</body>')
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Quick fix applied - essential functions added")
        return True
    
    print("ℹ️ Functions already exist - no quick fix needed")
    return False

if __name__ == "__main__":
    print("🔧 Dashboard JavaScript Fix Tool")
    print("=" * 40)
    
    # Run diagnosis and fix
    success = diagnose_and_fix_javascript()
    
    if success:
        print("\n" + "=" * 40)
        print("✅ Diagnosis complete!")
        print("\n💡 Next steps:")
        print("1. Refresh your browser and test the dashboard")
        print("2. Check browser console for any remaining errors")
        print("3. If issues persist, run quick_minimal_fix()")
        print("\nIf problems continue, restore from backup and re-run Trust Center integration")
    else:
        print("❌ Could not complete diagnosis")
