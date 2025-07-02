"""
Create GitHub Upload Package for Forrest Gump Timer
Creates a ZIP file with all essential files for easy GitHub upload
"""

import zipfile
import os
from datetime import datetime

def create_github_package():
    """Create ZIP package for GitHub upload"""
    
    # Files to include in the GitHub package
    files_to_include = [
        # Main application files
        'launcher.py',
        'forrest_gump_gui.py', 
        'app.py',
        'forrest_timer.py',
        'progress_dashboard.py',
        
        # Configuration and requirements
        'requirements.txt',
        '.gitignore',
        
        # Documentation
        'README.md',
        'GOOGLE_SETUP.md',
        'LICENSE',
        
        # Web interface
        'templates/index.html',
        
        # Setup and sync scripts
        'google_drive_sync.py',
        'github_setup.py',
        
        # VS Code configuration
        '.vscode/tasks.json',
        
        # GitHub specific
        '.github/copilot-instructions.md'
    ]
    
    # Create package filename
    package_name = f"forrest-gump-timer-github-upload_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    
    print("🏃‍♂️ Creating Forrest Gump Timer GitHub Package...")
    print("=" * 60)
    
    # Create ZIP file
    with zipfile.ZipFile(package_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        files_added = 0
        files_missing = 0
        
        for file_path in files_to_include:
            if os.path.exists(file_path):
                # Add file to ZIP
                zipf.write(file_path, file_path)
                print(f"✅ Added: {file_path}")
                files_added += 1
            else:
                print(f"⚠️ Missing: {file_path}")
                files_missing += 1
    
    print("\n" + "=" * 60)
    print(f"📦 Package created: {package_name}")
    print(f"✅ Files included: {files_added}")
    
    if files_missing > 0:
        print(f"⚠️ Files missing: {files_missing}")
    
    print("\n🚀 How to Upload to GitHub:")
    print("1. Go to: https://github.com/mmalone3/forrest-gump-timer")
    print("2. Click 'Add file' → 'Upload files'")
    print(f"3. Drag and drop: {package_name}")
    print("4. Add commit message: 'Initial upload: Forrest Gump Timer v1.0 🏃‍♂️'")
    print("5. Click 'Commit changes'")
    
    print("\n📋 Or Upload Individual Files:")
    print("Just drag these files from your folder to GitHub:")
    for file_path in files_to_include:
        if os.path.exists(file_path):
            print(f"   📄 {file_path}")
    
    print(f"\n🎉 Your Forrest Gump Timer is ready for GitHub!")
    print("🏃‍♂️ \"Run, Forrest, Run!\" to the cloud!")
    
    return package_name

if __name__ == "__main__":
    package_file = create_github_package()
    print(f"\n💾 Package saved as: {package_file}")
    print("🌐 Ready to upload to GitHub!")
