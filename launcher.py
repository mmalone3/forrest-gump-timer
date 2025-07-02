"""
Forrest Gump Timer - Main Launcher
Choose your preferred interface
"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os
import webbrowser
import threading

class LauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🏃‍♂️ Forrest Gump Timer Launcher")
        self.root.geometry("500x400")
        self.root.configure(bg='#2c3e50')
        
        self.create_widgets()
        
    def create_widgets(self):
        """Create the launcher interface"""
        # Title
        title_frame = tk.Frame(self.root, bg='#2c3e50', pady=20)
        title_frame.pack(fill='x')
        
        title_label = tk.Label(title_frame, 
                              text="🏃‍♂️ Forrest Gump Timer",
                              font=('Arial', 24, 'bold'),
                              bg='#2c3e50',
                              fg='#ecf0f1')
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame,
                                 text="\"Run, Forrest, Run!\" - Choose your interface",
                                 font=('Arial', 12),
                                 bg='#2c3e50',
                                 fg='#bdc3c7')
        subtitle_label.pack()
        
        # Main buttons frame
        buttons_frame = tk.Frame(self.root, bg='#2c3e50')
        buttons_frame.pack(expand=True, fill='both', padx=40, pady=20)
        
        # Desktop GUI button
        desktop_btn = tk.Button(buttons_frame,
                               text="🖥️ Desktop Application\n(Recommended for PC)",
                               font=('Arial', 14, 'bold'),
                               bg='#3498db',
                               fg='white',
                               pady=15,
                               command=self.launch_desktop_gui,
                               relief='flat',
                               cursor='hand2')
        desktop_btn.pack(fill='x', pady=10)
        
        # Web interface button
        web_btn = tk.Button(buttons_frame,
                           text="🌐 Web Interface\n(For mobile access)",
                           font=('Arial', 14, 'bold'),
                           bg='#27ae60',
                           fg='white',
                           pady=15,
                           command=self.launch_web_interface,
                           relief='flat',
                           cursor='hand2')
        web_btn.pack(fill='x', pady=10)
        
        # Progress dashboard button
        progress_btn = tk.Button(buttons_frame,
                                text="📊 Progress Dashboard\n(Graphs and statistics)",
                                font=('Arial', 14, 'bold'),
                                bg='#9b59b6',
                                fg='white',
                                pady=15,
                                command=self.launch_progress_dashboard,
                                relief='flat',
                                cursor='hand2')
        progress_btn.pack(fill='x', pady=10)
        
        # Utilities frame
        utils_frame = tk.Frame(self.root, bg='#2c3e50')
        utils_frame.pack(fill='x', padx=40, pady=10)
        
        utils_label = tk.Label(utils_frame,
                              text="🔧 Utilities:",
                              font=('Arial', 12, 'bold'),
                              bg='#2c3e50',
                              fg='#ecf0f1')
        utils_label.pack(anchor='w')
        
        utils_buttons_frame = tk.Frame(utils_frame, bg='#2c3e50')
        utils_buttons_frame.pack(fill='x', pady=5)
        
        sync_btn = tk.Button(utils_buttons_frame,
                            text="☁️ Google Drive Sync",
                            font=('Arial', 10),
                            bg='#f39c12',
                            fg='white',
                            command=self.launch_google_sync,
                            relief='flat',
                            cursor='hand2')
        sync_btn.pack(side='left', padx=5)
        
        export_btn = tk.Button(utils_buttons_frame,
                              text="💾 Export Data",
                              font=('Arial', 10),
                              bg='#e74c3c',
                              fg='white',
                              command=self.export_data,
                              relief='flat',
                              cursor='hand2')
        export_btn.pack(side='left', padx=5)
        
        help_btn = tk.Button(utils_buttons_frame,
                            text="❓ Setup Guide",
                            font=('Arial', 10),
                            bg='#34495e',
                            fg='white',
                            command=self.show_help,
                            relief='flat',
                            cursor='hand2')
        help_btn.pack(side='left', padx=5)
        
        # Status frame
        status_frame = tk.Frame(self.root, bg='#34495e', pady=10)
        status_frame.pack(fill='x')
        
        status_label = tk.Label(status_frame,
                               text="Ready to start your Forrest Gump journey! 🏃‍♂️",
                               font=('Arial', 10),
                               bg='#34495e',
                               fg='#ecf0f1')
        status_label.pack()
        
    def launch_desktop_gui(self):
        """Launch the desktop GUI application"""
        try:
            subprocess.Popen([sys.executable, 'forrest_gump_gui.py'])
            messagebox.showinfo("Desktop App", "Desktop application starting...\n\nThe GUI window should open shortly!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start desktop app: {str(e)}")
    
    def launch_web_interface(self):
        """Launch the web interface"""
        try:
            # Start Flask server in background
            subprocess.Popen([sys.executable, 'app.py'])
            
            # Wait a moment then open browser
            def open_browser():
                import time
                time.sleep(2)
                webbrowser.open('http://localhost:5000')
            
            threading.Thread(target=open_browser, daemon=True).start()
            
            messagebox.showinfo("Web Interface", 
                              "Web server starting...\n\n" +
                              "🌐 Opening browser to: http://localhost:5000\n" +
                              "📱 Access from mobile using your PC's IP address\n\n" +
                              "Note: Keep this launcher open to maintain the server.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start web interface: {str(e)}")
    
    def launch_progress_dashboard(self):
        """Launch the progress dashboard"""
        try:
            subprocess.Popen([sys.executable, 'progress_dashboard.py'])
            
            # Wait a moment then open browser
            def open_dashboard():
                import time
                time.sleep(3)
                webbrowser.open('http://localhost:8050')
            
            threading.Thread(target=open_dashboard, daemon=True).start()
            
            messagebox.showinfo("Progress Dashboard", 
                              "Progress dashboard starting...\n\n" +
                              "📊 Opening browser to: http://localhost:8050\n" +
                              "🔄 Dashboard updates automatically\n\n" +
                              "Note: Keep this launcher open to maintain the server.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start progress dashboard: {str(e)}")
    
    def launch_google_sync(self):
        """Launch Google Drive sync"""
        try:
            subprocess.Popen([sys.executable, 'google_drive_sync.py'])
            messagebox.showinfo("Google Drive Sync", 
                              "Google Drive sync starting...\n\n" +
                              "📤 Check console window for sync status\n" +
                              "📋 See GOOGLE_SETUP.md for setup instructions")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start Google sync: {str(e)}")
    
    def export_data(self):
        """Export session data"""
        try:
            from forrest_timer import timer
            from datetime import datetime
            sessions = timer.load_all_sessions()
            
            if not sessions:
                messagebox.showinfo("Export Data", "No session data found to export.")
                return
            
            filename = f"forrest_gump_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            export_data = {
                'export_date': datetime.now().isoformat(),
                'total_sessions': len(sessions),
                'sessions': sessions,
                'overall_progress': timer.get_overall_progress()
            }
            
            with open(filename, 'w') as f:
                import json
                json.dump(export_data, f, indent=2)
            
            messagebox.showinfo("Export Complete", 
                              f"✅ Data exported successfully!\n\n" +
                              f"📄 File: {filename}\n" +
                              f"📊 Sessions: {len(sessions)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export data: {str(e)}")
    
    def show_help(self):
        """Show help and setup information"""
        help_text = """🏃‍♂️ Forrest Gump Timer Setup Guide

📖 QUICK START:
1. Click "Desktop Application" for the main timer
2. Use "Web Interface" for mobile access
3. View "Progress Dashboard" for graphs and stats

🔧 FEATURES:
• Track your journey to complete Forrest's epic run
• Automatic break timer with one-click start/stop
• Real-time progress toward 15,248 mile goal
• Beautiful monthly progress graphs
• Google Drive sync for cloud backup
• Mobile-friendly web interface

📱 MOBILE ACCESS:
• Start "Web Interface" on your PC
• Access from phone using your PC's IP address
• All features work on mobile devices

☁️ GOOGLE DRIVE SYNC:
• See GOOGLE_SETUP.md for detailed instructions
• Automatic backup of all your session data
• Access data from any device

🎯 TARGET:
• Distance: 15,248 miles
• Time: 6,353 hours
• Speed: 2.4 mph (Forrest's pace)
• Duration: 3 years, 2 months, 14 days, 16 hours

"Run, Forrest, Run!" 🏃‍♂️"""
        
        messagebox.showinfo("Setup Guide", help_text)

def main():
    from datetime import datetime
    
    root = tk.Tk()
    app = LauncherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
