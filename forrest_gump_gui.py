"""
Forrest Gump Timer - Desktop GUI Application
Beautiful tkinter interface with progress tracking
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from datetime import datetime, timedelta
from forrest_timer import timer
import subprocess
import os

class ForrestGumpGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🏃‍♂️ Forrest Gump Timer")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        
        # Session state
        self.session_active = False
        self.update_thread = None
        self.stop_updates = False
        
        # Break timer state
        self.on_break = False
        self.break_start_time = None
        self.break_seconds = 0
        
        self.setup_styles()
        self.create_widgets()
        self.update_overall_stats()
        
    def setup_styles(self):
        """Configure ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        style.configure('Title.TLabel', 
                       font=('Arial', 20, 'bold'),
                       background='#2c3e50',
                       foreground='#ecf0f1')
        
        style.configure('Stat.TLabel',
                       font=('Arial', 12),
                       background='#34495e',
                       foreground='#ecf0f1',
                       padding=10)
        
        style.configure('Big.TLabel',
                       font=('Arial', 16, 'bold'),
                       background='#34495e',
                       foreground='#e74c3c')
        
        style.configure('Start.TButton',
                       font=('Arial', 14, 'bold'),
                       padding=10)
        
        style.configure('Stop.TButton',
                       font=('Arial', 14, 'bold'),
                       padding=10)
        
        style.configure('Break.TButton',
                       font=('Arial', 12, 'bold'),
                       padding=8)
    
    def create_widgets(self):
        """Create the main interface"""
        # Title
        title_frame = tk.Frame(self.root, bg='#2c3e50', pady=20)
        title_frame.pack(fill='x')
        
        title_label = ttk.Label(title_frame, 
                               text="🏃‍♂️ Forrest Gump Timer",
                               style='Title.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(title_frame,
                                  text="\"Run, Forrest, Run!\" - Track your epic journey at 2.4 mph",
                                  font=('Arial', 10),
                                  background='#2c3e50',
                                  foreground='#bdc3c7')
        subtitle_label.pack()
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Left panel - Session controls
        left_panel = tk.LabelFrame(main_frame, 
                                  text="Session Control",
                                  bg='#34495e',
                                  fg='#ecf0f1',
                                  font=('Arial', 12, 'bold'),
                                  padx=15, pady=15)
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        # Session buttons
        button_frame = tk.Frame(left_panel, bg='#34495e')
        button_frame.pack(pady=10)
        
        self.start_btn = ttk.Button(button_frame,
                                   text="▶ Start Session",
                                   style='Start.TButton',
                                   command=self.start_session)
        self.start_btn.pack(side='left', padx=5)
        
        self.stop_btn = ttk.Button(button_frame,
                                  text="⏹ Stop Session",
                                  style='Stop.TButton',
                                  command=self.stop_session,
                                  state='disabled')
        self.stop_btn.pack(side='left', padx=5)
        
        # Break controls
        break_frame = tk.LabelFrame(left_panel,
                                   text="Break Timer",
                                   bg='#34495e',
                                   fg='#ecf0f1',
                                   font=('Arial', 10, 'bold'),
                                   padx=10, pady=10)
        break_frame.pack(fill='x', pady=10)
        
        # Auto break buttons
        auto_break_frame = tk.Frame(break_frame, bg='#34495e')
        auto_break_frame.pack(fill='x', pady=5)
        
        self.break_start_btn = ttk.Button(auto_break_frame,
                                         text="🛑 Start Break",
                                         style='Break.TButton',
                                         command=self.start_break,
                                         state='disabled')
        self.break_start_btn.pack(side='left', padx=5)
        
        self.break_end_btn = ttk.Button(auto_break_frame,
                                       text="▶️ Resume Running",
                                       style='Break.TButton',
                                       command=self.end_break,
                                       state='disabled')
        self.break_end_btn.pack(side='left', padx=5)
        
        # Break timer display
        self.break_timer_label = ttk.Label(break_frame,
                                          text="Break Time: 00:00",
                                          font=('Arial', 11, 'bold'),
                                          background='#34495e',
                                          foreground='#e74c3c')
        self.break_timer_label.pack(pady=5)
        
        # Manual break entry
        manual_frame = tk.Frame(break_frame, bg='#34495e')
        manual_frame.pack(fill='x', pady=5)
        
        tk.Label(manual_frame, text="Manual Entry:", 
                bg='#34495e', fg='#ecf0f1', font=('Arial', 9)).pack()
        
        entry_frame = tk.Frame(manual_frame, bg='#34495e')
        entry_frame.pack()
        
        tk.Label(entry_frame, text="Min:", bg='#34495e', fg='#ecf0f1').pack(side='left')
        self.minutes_var = tk.StringVar(value="0")
        minutes_spin = tk.Spinbox(entry_frame, from_=0, to=59, width=5, textvariable=self.minutes_var)
        minutes_spin.pack(side='left', padx=2)
        
        tk.Label(entry_frame, text="Sec:", bg='#34495e', fg='#ecf0f1').pack(side='left')
        self.seconds_var = tk.StringVar(value="0")
        seconds_spin = tk.Spinbox(entry_frame, from_=0, to=59, width=5, textvariable=self.seconds_var)
        seconds_spin.pack(side='left', padx=2)
        
        ttk.Button(entry_frame,
                  text="☕ Add Break",
                  command=self.add_manual_break).pack(side='left', padx=5)
        
        # Current session stats
        session_stats_frame = tk.LabelFrame(left_panel,
                                           text="Current Session",
                                           bg='#34495e',
                                           fg='#ecf0f1',
                                           font=('Arial', 10, 'bold'),
                                           padx=10, pady=10)
        session_stats_frame.pack(fill='x', pady=10)
        
        self.session_time_label = ttk.Label(session_stats_frame, text="Session Time: 00:00:00", style='Stat.TLabel')
        self.session_time_label.pack(anchor='w')
        
        self.running_time_label = ttk.Label(session_stats_frame, text="Running Time: 00:00:00", style='Stat.TLabel')
        self.running_time_label.pack(anchor='w')
        
        self.session_distance_label = ttk.Label(session_stats_frame, text="Distance: 0.000 miles", style='Stat.TLabel')
        self.session_distance_label.pack(anchor='w')
        
        self.session_calories_label = ttk.Label(session_stats_frame, text="Calories: 0", style='Stat.TLabel')
        self.session_calories_label.pack(anchor='w')
        
        # Right panel - Overall progress
        right_panel = tk.LabelFrame(main_frame,
                                   text="Forrest's Journey Progress",
                                   bg='#34495e',
                                   fg='#ecf0f1',
                                   font=('Arial', 12, 'bold'),
                                   padx=15, pady=15)
        right_panel.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        # Progress stats
        progress_frame = tk.Frame(right_panel, bg='#34495e')
        progress_frame.pack(fill='x', pady=10)
        
        self.total_distance_label = ttk.Label(progress_frame, text="Total Distance: 0.000 miles", style='Big.TLabel')
        self.total_distance_label.pack(anchor='w', pady=2)
        
        self.total_time_label = ttk.Label(progress_frame, text="Total Time: 00:00:00", style='Big.TLabel')
        self.total_time_label.pack(anchor='w', pady=2)
        
        self.progress_label = ttk.Label(progress_frame, text="Progress: 0.000%", style='Big.TLabel')
        self.progress_label.pack(anchor='w', pady=2)
        
        self.remaining_label = ttk.Label(progress_frame, text="Distance Remaining: 15,248 miles", style='Stat.TLabel')
        self.remaining_label.pack(anchor='w', pady=2)
        
        self.sessions_label = ttk.Label(progress_frame, text="Total Sessions: 0", style='Stat.TLabel')
        self.sessions_label.pack(anchor='w', pady=2)
        
        # Progress bar
        progress_bar_frame = tk.Frame(right_panel, bg='#34495e')
        progress_bar_frame.pack(fill='x', pady=10)
        
        tk.Label(progress_bar_frame, text="Journey Progress:", 
                bg='#34495e', fg='#ecf0f1', font=('Arial', 10, 'bold')).pack(anchor='w')
        
        self.progress_bar = ttk.Progressbar(progress_bar_frame, 
                                           length=300, 
                                           mode='determinate')
        self.progress_bar.pack(fill='x', pady=5)
        
        # Buttons
        button_bottom_frame = tk.Frame(right_panel, bg='#34495e')
        button_bottom_frame.pack(fill='x', pady=10)
        
        ttk.Button(button_bottom_frame,
                  text="📊 View Progress Graphs",
                  command=self.open_progress_page).pack(side='left', padx=5)
        
        ttk.Button(button_bottom_frame,
                  text="🌐 Open Web Interface",
                  command=self.open_web_interface).pack(side='left', padx=5)
        
        ttk.Button(button_bottom_frame,
                  text="💾 Export Data",
                  command=self.export_data).pack(side='left', padx=5)
    
    def start_session(self):
        """Start a new running session"""
        try:
            timer.start_session()
            self.session_active = True
            
            # Update UI
            self.start_btn.config(state='disabled')
            self.stop_btn.config(state='normal')
            self.break_start_btn.config(state='normal')
            
            # Start update thread
            self.stop_updates = False
            self.update_thread = threading.Thread(target=self.update_session_stats, daemon=True)
            self.update_thread.start()
            
            messagebox.showinfo("Session Started", "Good luck on your run, Forrest! 🏃‍♂️")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start session: {str(e)}")
    
    def stop_session(self):
        """Stop the current session"""
        try:
            # End any active break
            if self.on_break:
                self.end_break()
            
            session_data = timer.stop_session()
            self.session_active = False
            self.stop_updates = True
            
            # Update UI
            self.start_btn.config(state='normal')
            self.stop_btn.config(state='disabled')
            self.break_start_btn.config(state='disabled')
            self.break_end_btn.config(state='disabled')
            
            # Reset session displays
            self.session_time_label.config(text="Session Time: 00:00:00")
            self.running_time_label.config(text="Running Time: 00:00:00")
            self.session_distance_label.config(text="Distance: 0.000 miles")
            self.session_calories_label.config(text="Calories: 0")
            self.break_timer_label.config(text="Break Time: 00:00")
            
            # Update overall stats
            self.update_overall_stats()
            
            # Show session summary
            summary = f"""Session Complete! 🏁
            
Distance: {session_data['distance_miles']:.3f} miles
Running Time: {timer.format_time(int(session_data['running_time']))}
Break Time: {timer.format_time(int(session_data['break_time']))}
Calories: {session_data['calories']}
Breaks: {session_data['breaks_count']}

Great job, Forrest! Keep running! 🏃‍♂️"""
            
            messagebox.showinfo("Session Complete", summary)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop session: {str(e)}")
    
    def start_break(self):
        """Start automatic break timer"""
        if not self.session_active or self.on_break:
            return
        
        self.on_break = True
        self.break_start_time = time.time()
        self.break_seconds = 0
        
        # Update UI
        self.break_start_btn.config(state='disabled')
        self.break_end_btn.config(state='normal')
        
        # Start break timer
        self.update_break_timer()
    
    def end_break(self):
        """End automatic break timer and add to session"""
        if not self.on_break:
            return
        
        # Calculate break duration
        break_duration = int(time.time() - self.break_start_time)
        minutes = break_duration // 60
        seconds = break_duration % 60
        
        try:
            # Add break to session
            timer.add_break(minutes, seconds)
            
            # Reset break state
            self.on_break = False
            self.break_start_time = None
            self.break_seconds = 0
            
            # Update UI
            self.break_start_btn.config(state='normal')
            self.break_end_btn.config(state='disabled')
            self.break_timer_label.config(text="Break Time: 00:00")
            
            messagebox.showinfo("Break Added", f"Break time added: {minutes:02d}:{seconds:02d}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add break: {str(e)}")
    
    def add_manual_break(self):
        """Add manual break time"""
        try:
            minutes = int(self.minutes_var.get())
            seconds = int(self.seconds_var.get())
            
            if minutes == 0 and seconds == 0:
                messagebox.showwarning("Invalid Input", "Please enter break time")
                return
            
            timer.add_break(minutes, seconds)
            
            # Reset inputs
            self.minutes_var.set("0")
            self.seconds_var.set("0")
            
            messagebox.showinfo("Break Added", f"Break time added: {minutes:02d}:{seconds:02d}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add break: {str(e)}")
    
    def update_break_timer(self):
        """Update break timer display"""
        if self.on_break and self.break_start_time:
            self.break_seconds = int(time.time() - self.break_start_time)
            minutes = self.break_seconds // 60
            seconds = self.break_seconds % 60
            
            self.break_timer_label.config(text=f"⏸️ Break Time: {minutes:02d}:{seconds:02d}")
            
            # Schedule next update
            self.root.after(1000, self.update_break_timer)
    
    def update_session_stats(self):
        """Update session statistics in real-time"""
        while self.session_active and not self.stop_updates:
            try:
                stats = timer.get_session_stats()
                
                if "error" not in stats:
                    # Update UI in main thread
                    self.root.after(0, self.update_session_display, stats)
                
                time.sleep(1)
                
            except Exception as e:
                print(f"Error updating stats: {e}")
                time.sleep(1)
    
    def update_session_display(self, stats):
        """Update session display labels"""
        try:
            self.session_time_label.config(text=f"Session Time: {timer.format_time(stats['session_time'])}")
            self.running_time_label.config(text=f"Running Time: {timer.format_time(stats['running_time'])}")
            self.session_distance_label.config(text=f"Distance: {stats['distance_miles']:.3f} miles")
            self.session_calories_label.config(text=f"Calories: {stats['calories']}")
        except Exception as e:
            print(f"Error updating display: {e}")
    
    def update_overall_stats(self):
        """Update overall progress statistics"""
        try:
            progress = timer.get_overall_progress()
            
            self.total_distance_label.config(text=f"Total Distance: {progress['total_distance']:.3f} miles")
            self.total_time_label.config(text=f"Total Time: {timer.format_time(int(progress['total_running_time']))}")
            self.progress_label.config(text=f"Progress: {progress['distance_progress_percent']:.3f}%")
            self.remaining_label.config(text=f"Distance Remaining: {progress['distance_remaining']:.0f} miles")
            self.sessions_label.config(text=f"Total Sessions: {progress['total_sessions']}")
            
            # Update progress bar
            self.progress_bar['value'] = progress['distance_progress_percent']
            
        except Exception as e:
            print(f"Error updating overall stats: {e}")
    
    def open_progress_page(self):
        """Open the progress visualization page"""
        try:
            subprocess.Popen(['python', 'progress_dashboard.py'], shell=True)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open progress page: {str(e)}")
    
    def open_web_interface(self):
        """Open the web interface"""
        try:
            subprocess.Popen(['python', 'app.py'], shell=True)
            import webbrowser
            webbrowser.open('http://localhost:5000')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open web interface: {str(e)}")
    
    def export_data(self):
        """Export session data"""
        try:
            sessions = timer.load_all_sessions()
            filename = f"forrest_gump_data_{datetime.now().strftime('%Y-%m-%d')}.json"
            
            with open(filename, 'w') as f:
                import json
                json.dump({
                    "export_date": datetime.now().isoformat(),
                    "total_sessions": len(sessions),
                    "sessions": sessions
                }, f, indent=2)
            
            messagebox.showinfo("Export Complete", f"Data exported to {filename}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export data: {str(e)}")

def main():
    root = tk.Tk()
    app = ForrestGumpGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
