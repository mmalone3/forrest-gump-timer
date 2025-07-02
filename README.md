# 🏃‍♂️ Forrest Gump Timer - Local Desktop Edition

A comprehensive treadmill timer system that tracks your journey to complete Forrest Gump's epic 3+ year run at 2.4 mph with automatic Google Drive sync and beautiful progress visualization.

## 🎯 The Challenge

**Complete Forrest's Journey:**
- **Duration:** 3 years, 2 months, 14 days, 16 hours
- **Distance:** ~15,248 miles
- **Speed:** 2.4 mph (Forrest's constant pace)
- **Total Time:** ~6,353 hours of running

## ✨ Features

### 🖥️ **Desktop Application**
- Beautiful tkinter GUI with real-time statistics
- Automatic break timer (start/stop with one click)
- Session management and progress tracking
- Export capabilities and data backup

### 🌐 **Web Interface**
- Mobile-friendly Flask web server
- Access from any device on your network
- Touch-optimized controls for phones/tablets
- Real-time synchronization with desktop app

### 📊 **Progress Dashboard**
- Monthly progress graphs starting July 2025
- Daily activity heatmaps
- Cumulative distance tracking
- Progress gauges and statistics
- Auto-updating visualizations

### ☁️ **Google Drive Sync**
- Automatic cloud backup of all sessions
- Cross-device synchronization
- Data recovery capabilities
- Works with your existing 2TB Google Drive

## 🚀 Quick Start

### 1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 2. **Choose Your Interface**
```bash
# Launch main menu
python launcher.py

# Or directly start specific interface:
python forrest_gump_gui.py      # Desktop GUI
python app.py                   # Web interface
python progress_dashboard.py    # Progress graphs
```

### 3. **Start Running!**
1. Set your treadmill to 2.4 mph
2. Click "Start Session" 
3. Use automatic break timer for water breaks
4. Watch your progress toward Forrest's goal!

## 📱 Mobile Access

1. Start the web interface: `python app.py`
2. Open browser on your phone
3. Navigate to: `http://[YOUR_PC_IP]:5000`
4. Bookmark for quick access
5. Add to home screen for app-like experience

## 📊 Progress Tracking

### **Real-Time Stats:**
- Session time and running time
- Distance at 2.4 mph
- Calories burned
- Break time tracking
- Progress percentage

### **Monthly Graphs:**
- Distance progress by month
- Daily activity heatmaps
- Cumulative progress charts
- Goal achievement tracking

## 🔧 File Structure

```
D:\ForrestGumpTimer\
├── launcher.py              # Main launcher menu
├── forrest_gump_gui.py      # Desktop GUI application
├── app.py                   # Flask web server
├── progress_dashboard.py    # Progress visualization
├── forrest_timer.py         # Core timer logic
├── google_drive_sync.py     # Cloud synchronization
├── templates/
│   └── index.html          # Web interface
├── data/
│   └── sessions.json       # Local session data
├── requirements.txt         # Python dependencies
└── GOOGLE_SETUP.md         # Google Drive setup guide
```

## ☁️ Google Drive Setup

1. Follow instructions in `GOOGLE_SETUP.md`
2. Enable Google Drive API in Google Cloud Console
3. Download credentials as `google_credentials.json`
4. Run `python google_drive_sync.py` to test

## 💾 Data Management

### **Local Storage:**
- Sessions saved to `data/sessions.json`
- Automatic backup on each session
- Export capabilities built-in

### **Cloud Sync:**
- Automatic upload to Google Drive
- Cross-device synchronization
- Data recovery from cloud

### **Export Options:**
- JSON format with all session data
- Import/export between devices
- Compatible with spreadsheet apps

## 🎮 How to Use

### **Desktop GUI:**
1. Launch: `python forrest_gump_gui.py`
2. Click "Start Session" when you begin running
3. Use "Start Break" for water/rest breaks
4. Click "Resume Running" when ready
5. Click "Stop Session" when finished

### **Automatic Break Timer:**
- ✅ **Start Break:** Pauses distance calculation
- ✅ **Resume Running:** Automatically adds break time
- ✅ **Manual Entry:** Still available for estimated breaks
- ✅ **Real-Time Display:** Shows break duration

### **Web Interface:**
- Perfect for mobile devices
- All desktop features available
- Touch-friendly controls
- Real-time updates

## 📈 Progress Visualization

Access beautiful graphs at: `http://localhost:8050`

### **Available Charts:**
- 📊 Monthly distance progress
- 🔥 Daily activity heatmap
- 📈 Cumulative distance tracking
- 🎯 Progress gauge (percentage complete)
- 📅 Monthly statistics cards

## 🎯 Target Milestones

- **Daily Goal:** ~7.4 miles (3 hours of running)
- **Weekly Goal:** ~52 miles (21 hours)
- **Monthly Goal:** ~224 miles (93 hours)
- **Yearly Goal:** ~2,688 miles (1,120 hours)

## 🛠️ Technical Requirements

- **Python 3.8+**
- **Windows, macOS, or Linux**
- **2GB RAM minimum**
- **Internet connection** (for Google Drive sync)
- **Web browser** (for progress dashboard)

## 🏃‍♂️ Tips for Success

1. **Consistency is key** - aim for regular sessions
2. **Use the break timer** - stay hydrated!
3. **Track your progress** - watch the graphs grow
4. **Mobile access** - monitor from your phone
5. **Cloud backup** - never lose your data

## 🎉 Achievement System

- 🥉 **First Mile:** Complete your first session
- 🥈 **Marathon:** Reach 26.2 miles total
- 🥇 **Century:** Complete 100 miles
- 🏆 **Forrest Status:** Complete the full journey!

## 📞 Support

- **Setup Issues:** Check `GOOGLE_SETUP.md`
- **Data Problems:** Use export/import features
- **Mobile Access:** Ensure PC and phone on same network
- **Performance:** Close unused applications

---

**"Run, Forrest, Run!"** 🏃‍♂️

*Start your epic journey today and join Forrest on his legendary cross-country run!*
