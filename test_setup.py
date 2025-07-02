"""
Demo script to test the Forrest Gump Timer setup
"""

import sys
import os
from datetime import datetime

def test_imports():
    """Test that all required modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        import tkinter
        print("✅ tkinter - OK")
    except ImportError:
        print("❌ tkinter - FAILED")
        return False
    
    try:
        import flask
        print("✅ Flask - OK")
    except ImportError:
        print("❌ Flask - FAILED")
        return False
    
    try:
        import matplotlib
        print("✅ matplotlib - OK")
    except ImportError:
        print("❌ matplotlib - FAILED")
        return False
    
    try:
        import plotly
        print("✅ plotly - OK")
    except ImportError:
        print("❌ plotly - FAILED")
        return False
    
    try:
        import pandas
        print("✅ pandas - OK")
    except ImportError:
        print("❌ pandas - FAILED")
        return False
    
    try:
        import dash
        print("✅ dash - OK")
    except ImportError:
        print("❌ dash - FAILED")
        return False
    
    return True

def test_core_timer():
    """Test the core timer functionality"""
    print("\n🏃‍♂️ Testing core timer...")
    
    try:
        from forrest_timer import timer
        
        # Test basic functionality
        print("✅ Timer import - OK")
        
        # Check data directory
        if os.path.exists("data"):
            print("✅ Data directory - OK")
        else:
            print("📁 Creating data directory...")
            os.makedirs("data", exist_ok=True)
            print("✅ Data directory created")
        
        # Test progress calculation
        progress = timer.get_overall_progress()
        print(f"✅ Progress calculation - OK")
        print(f"   📊 Total sessions: {progress['total_sessions']}")
        print(f"   📏 Total distance: {progress['total_distance']:.3f} miles")
        print(f"   🎯 Target distance: {progress['target_distance']:,.0f} miles")
        
        return True
        
    except Exception as e:
        print(f"❌ Core timer test failed: {e}")
        return False

def test_file_structure():
    """Test that all required files exist"""
    print("\n📁 Testing file structure...")
    
    required_files = [
        "launcher.py",
        "forrest_gump_gui.py", 
        "app.py",
        "progress_dashboard.py",
        "forrest_timer.py",
        "google_drive_sync.py",
        "templates/index.html",
        "requirements.txt",
        "README.md",
        "GOOGLE_SETUP.md",
        ".github/copilot-instructions.md",
        ".vscode/tasks.json"
    ]
    
    all_good = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MISSING")
            all_good = False
    
    return all_good

def create_demo_session():
    """Create a demo session for testing"""
    print("\n🎮 Creating demo session...")
    
    try:
        from forrest_timer import timer
        
        # Start a demo session
        session_id = timer.start_session()
        print(f"✅ Demo session started: {session_id}")
        
        # Add a demo break
        timer.add_break(2, 30)  # 2 minutes 30 seconds
        print("✅ Demo break added: 02:30")
        
        # Stop the session
        session_data = timer.stop_session()
        print("✅ Demo session completed")
        
        print(f"   📏 Distance: {session_data['distance_miles']:.6f} miles")
        print(f"   ⏱️ Running time: {session_data['running_time']:.1f} seconds")
        print(f"   ☕ Break time: {session_data['break_time']} seconds")
        
        return True
        
    except Exception as e:
        print(f"❌ Demo session failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Forrest Gump Timer - Setup Test")
    print("=" * 50)
    print(f"📅 Test date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📁 Working directory: {os.getcwd()}")
    print(f"🐍 Python version: {sys.version}")
    
    # Run tests
    tests = [
        ("Import Test", test_imports),
        ("File Structure Test", test_file_structure), 
        ("Core Timer Test", test_core_timer),
        ("Demo Session Test", create_demo_session)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        result = test_func()
        results.append((test_name, result))
    
    # Summary
    print("\n" + "="*50)
    print("📋 TEST SUMMARY:")
    print("="*50)
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False
    
    print("\n" + "="*50)
    if all_passed:
        print("🎉 ALL TESTS PASSED!")
        print("🏃‍♂️ Your Forrest Gump Timer is ready!")
        print("\n📋 Next Steps:")
        print("1. Run: python launcher.py")
        print("2. Choose your preferred interface")
        print("3. Start your epic journey!")
        print("\n\"Run, Forrest, Run!\" 🏃‍♂️")
    else:
        print("⚠️ SOME TESTS FAILED")
        print("🔧 Please check the errors above and fix any issues")
        print("📖 See README.md for setup instructions")
    
    print("="*50)

if __name__ == "__main__":
    main()
