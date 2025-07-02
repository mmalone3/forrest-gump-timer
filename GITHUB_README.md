# Forrest Gump Timer 🏃‍♂️

A comprehensive treadmill timer system to track your journey completing Forrest Gump's epic 3+ year run at 2.4 mph.

![Forrest Gump Timer](https://img.shields.io/badge/Status-Ready%20to%20Run-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 The Challenge

**Complete Forrest's Epic Journey:**
- 🏃‍♂️ **15,248 miles** total distance
- ⏱️ **6,353 hours** of running time  
- 🎯 **2.4 mph** constant speed
- 📅 **3 years, 2 months, 14 days, 16 hours**

## ✨ Features

- 🖥️ **Desktop GUI** - Beautiful tkinter interface
- 📱 **Mobile Web App** - Access from any device
- 📊 **Progress Dashboard** - Monthly graphs and statistics
- ⏱️ **Automatic Break Timer** - One-click start/stop breaks
- 💾 **Local Data Storage** - All data stays on your computer
- ☁️ **Google Drive Sync** - Optional cloud backup
- 📈 **Real-time Progress** - Track toward Forrest's goal

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/YourUsername/forrest-gump-timer.git
cd forrest-gump-timer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch Application
```bash
python launcher.py
```

## 📱 Interfaces

### 🖥️ Desktop Application
```bash
python forrest_gump_gui.py
```
- Full-featured GUI with break timer
- Real-time session statistics
- Progress tracking and export

### 🌐 Web Interface (Mobile-Friendly)
```bash
python app.py
```
- Access at: `http://localhost:5000`
- Mobile-optimized controls
- Same features as desktop app

### 📊 Progress Dashboard
```bash
python progress_dashboard.py
```
- Monthly progress graphs
- Daily activity heatmaps
- Visual progress tracking

## 🎮 How to Use

1. **Set treadmill to 2.4 mph** (Forrest's pace)
2. **Start session** when you begin running
3. **Use break timer** for water/rest breaks
4. **Resume running** when ready
5. **Stop session** when finished
6. **Watch your progress** toward the goal!

## 📊 Progress Tracking

- **Real-time Stats:** Distance, time, calories, progress %
- **Monthly Graphs:** Visual progress by month
- **Goal Tracking:** See how close you are to completing Forrest's journey
- **Session History:** All your runs saved and tracked

## 💾 Data Storage

- **Local Storage:** All data saved to `data/sessions.json`
- **Cross-Platform:** Desktop and web apps share same data
- **Export Options:** JSON export for backup/analysis
- **Google Drive Sync:** Optional cloud backup

## 🛠️ Technical Details

- **Python 3.8+** required
- **Flask** for web interface
- **Tkinter** for desktop GUI
- **Plotly/Dash** for progress graphs
- **Matplotlib** for visualizations

## 📱 Mobile Access

1. Start web server on your computer
2. Find your computer's IP address
3. Access from phone: `http://[YOUR-IP]:5000`
4. Bookmark for quick access
5. Add to home screen for app-like experience

## 🎯 Milestones

- 🥉 **First Mile** - Complete your first session
- 🥈 **Marathon** - Reach 26.2 miles total
- 🥇 **Century** - Complete 100 miles
- 🏆 **Forrest Status** - Complete the full 15,248 mile journey!

## 📝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by Forrest Gump's legendary cross-country run
- Built for anyone crazy enough to attempt this epic journey
- "Run, Forrest, Run!" 🏃‍♂️

---

**Ready to start your epic journey? Clone this repo and start running!**

*"Life is like a box of chocolates, but running 15,248 miles is exactly what you think it is." - Forrest (probably)*
