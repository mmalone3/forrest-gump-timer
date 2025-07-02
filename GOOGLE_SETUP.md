# Forrest Gump Timer - Google Drive Setup Guide

## 🚀 Setting Up Google Drive Sync

To enable automatic synchronization with Google Drive:

### 1. Enable Google Drive API
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable the Google Drive API
4. Go to "Credentials" → "Create Credentials" → "Desktop Application"
5. Download the credentials JSON file

### 2. Setup Credentials
1. Rename downloaded file to `google_credentials.json`
2. Place in your project directory: `D:\ForrestGumpTimer\`
3. Run the sync script to test: `python google_drive_sync.py`

### 3. Features Available
- ✅ Automatic session data backup
- ✅ Cross-device synchronization
- ✅ Real-time cloud storage
- ✅ Data recovery capabilities

### 4. Privacy & Security
- Your data stays in your personal Google Drive
- No third-party access to your running data
- Local backup always maintained

### 5. Usage
```bash
# Manual sync
python google_drive_sync.py

# Automatic sync (run with timer)
python forrest_gump_gui.py  # Includes auto-sync
```

## 📱 Mobile Access

Once Google Drive sync is setup:
1. Access your data from Google Sheets on mobile
2. Use the web interface from any device
3. Real-time progress tracking anywhere

Your 2TB Google Drive is perfect for storing all your Forrest Gump journey data! 🏃‍♂️
