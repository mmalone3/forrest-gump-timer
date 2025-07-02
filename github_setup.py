"""
GitHub Setup Script for Forrest Gump Timer
Helps you upload your project to GitHub
"""

import subprocess
import os
import sys

def run_command(command, description):
    """Run a command and show result"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed!")
            if result.stdout.strip():
                print(f"   Output: {result.stdout.strip()}")
        else:
            print(f"❌ {description} failed!")
            print(f"   Error: {result.stderr.strip()}")
            return False
        return True
    except Exception as e:
        print(f"❌ {description} failed with exception: {e}")
        return False

def check_git_installed():
    """Check if Git is installed"""
    print("🔍 Checking if Git is installed...")
    result = subprocess.run("git --version", shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ Git is installed: {result.stdout.strip()}")
        return True
    else:
        print("❌ Git is not installed!")
        print("📥 Please install Git from: https://git-scm.com/download/win")
        return False

def setup_git_repo():
    """Initialize Git repository and prepare for GitHub"""
    print("\n🚀 Setting up Git repository for Forrest Gump Timer...")
    
    # Check if Git is installed
    if not check_git_installed():
        return False
    
    # Initialize Git repo
    if not run_command("git init", "Initializing Git repository"):
        return False
    
    # Create .gitignore if it doesn't exist
    if not os.path.exists(".gitignore"):
        print("📝 Creating .gitignore file...")
        # .gitignore is already created above
    
    # Add all files
    if not run_command("git add .", "Adding files to Git"):
        return False
    
    # Initial commit
    if not run_command('git commit -m "Initial commit: Forrest Gump Timer v1.0"', "Creating initial commit"):
        return False
    
    # Set main branch
    if not run_command("git branch -M main", "Setting main branch"):
        return False
    
    return True

def main():
    """Main setup function"""
    print("🏃‍♂️ Forrest Gump Timer - GitHub Setup")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("forrest_timer.py"):
        print("❌ Please run this script from the ForrestGumpTimer directory!")
        return
    
    # Setup Git repository
    if setup_git_repo():
        print("\n✅ Git repository setup complete!")
        print("\n📋 Next Steps:")
        print("1. Go to GitHub.com and create a new repository")
        print("2. Name it: 'forrest-gump-timer'")
        print("3. Don't initialize with README (we already have one)")
        print("4. Copy the repository URL")
        print("5. Run these commands:")
        print(f"   git remote add origin https://github.com/YourUsername/forrest-gump-timer.git")
        print(f"   git push -u origin main")
        print("\n🎉 Your Forrest Gump Timer will be on GitHub!")
        print("🏃‍♂️ \"Run, Forrest, Run!\" to the cloud!")
    else:
        print("\n❌ Setup failed. Please check the errors above.")

if __name__ == "__main__":
    main()
