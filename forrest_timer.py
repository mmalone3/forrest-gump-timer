"""
Forrest Gump Timer - Core Module
Handles timer calculations and data management
"""

import json
import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import os

@dataclass
class Session:
    """Represents a single running session"""
    session_id: str
    start_time: datetime.datetime
    end_time: Optional[datetime.datetime] = None
    breaks: List[Dict] = None
    total_break_time: int = 0  # seconds
    running_time: int = 0  # seconds
    distance_miles: float = 0.0
    calories: int = 0
    
    def __post_init__(self):
        if self.breaks is None:
            self.breaks = []

class ForrestGumpTimer:
    """Main timer class for tracking Forrest Gump's epic journey"""
    
    # Forrest's journey constants
    TOTAL_YEARS = 3
    TOTAL_MONTHS = 2
    TOTAL_DAYS = 14
    TOTAL_HOURS = 16
    SPEED_MPH = 2.4
    
    def __init__(self, data_dir: str = "data"):
        """Initialize the timer with data directory"""
        self.data_dir = data_dir
        self.current_session = None
        self.sessions_file = os.path.join(data_dir, "sessions.json")
        
        # Create data directory if it doesn't exist
        os.makedirs(data_dir, exist_ok=True)
        
        # Calculate total target time and distance
        self.total_target_seconds = self._calculate_total_target_seconds()
        self.total_target_miles = self._calculate_total_target_miles()
        
    def _calculate_total_target_seconds(self) -> int:
        """Calculate total seconds for Forrest's journey"""
        total_days = (self.TOTAL_YEARS * 365) + (self.TOTAL_MONTHS * 30) + self.TOTAL_DAYS
        total_hours = (total_days * 24) + self.TOTAL_HOURS
        return total_hours * 3600
    
    def _calculate_total_target_miles(self) -> float:
        """Calculate total miles for Forrest's journey"""
        total_hours = self.total_target_seconds / 3600
        return total_hours * self.SPEED_MPH
    
    def start_session(self) -> str:
        """Start a new running session"""
        if self.current_session:
            raise ValueError("Session already active")
        
        session_id = datetime.datetime.now().isoformat()
        self.current_session = Session(
            session_id=session_id,
            start_time=datetime.datetime.now()
        )
        return session_id
    
    def add_break(self, minutes: int, seconds: int) -> None:
        """Add break time to current session"""
        if not self.current_session:
            raise ValueError("No active session")
        
        break_seconds = minutes * 60 + seconds
        break_data = {
            "minutes": minutes,
            "seconds": seconds,
            "total_seconds": break_seconds,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        self.current_session.breaks.append(break_data)
        self.current_session.total_break_time += break_seconds
    
    def stop_session(self) -> Dict:
        """Stop current session and calculate final statistics"""
        if not self.current_session:
            raise ValueError("No active session")
        
        # Set end time
        self.current_session.end_time = datetime.datetime.now()
        
        # Calculate session statistics
        total_duration = (self.current_session.end_time - self.current_session.start_time).total_seconds()
        self.current_session.running_time = total_duration - self.current_session.total_break_time
        
        # Calculate distance and calories
        running_hours = self.current_session.running_time / 3600
        self.current_session.distance_miles = running_hours * self.SPEED_MPH
        self.current_session.calories = int(self.current_session.distance_miles * 100)  # ~100 cal/mile
        
        # Save session
        self._save_session(self.current_session)
        
        # Prepare return data
        session_data = {
            "session_id": self.current_session.session_id,
            "total_duration": total_duration,
            "running_time": self.current_session.running_time,
            "break_time": self.current_session.total_break_time,
            "distance_miles": self.current_session.distance_miles,
            "calories": self.current_session.calories,
            "breaks_count": len(self.current_session.breaks)
        }
        
        # Clear current session
        self.current_session = None
        
        return session_data
    
    def get_session_stats(self) -> Dict:
        """Get real-time stats for current session"""
        if not self.current_session:
            return {"error": "No active session"}
        
        current_time = datetime.datetime.now()
        total_duration = (current_time - self.current_session.start_time).total_seconds()
        running_time = total_duration - self.current_session.total_break_time
        
        # Calculate current distance
        running_hours = running_time / 3600
        current_distance = running_hours * self.SPEED_MPH
        current_calories = int(current_distance * 100)
        
        return {
            "session_time": int(total_duration),
            "running_time": int(running_time),
            "break_time": self.current_session.total_break_time,
            "distance_miles": current_distance,
            "calories": current_calories,
            "breaks_count": len(self.current_session.breaks)
        }
    
    def get_overall_progress(self) -> Dict:
        """Get overall progress toward Forrest's goal"""
        sessions = self.load_all_sessions()
        
        total_running_time = sum(session.get("running_time", 0) for session in sessions)
        total_distance = sum(session.get("distance_miles", 0) for session in sessions)
        total_sessions = len(sessions)
        
        # Calculate progress percentages
        time_progress = (total_running_time / self.total_target_seconds) * 100
        distance_progress = (total_distance / self.total_target_miles) * 100
        
        # Calculate estimated completion
        if total_running_time > 0:
            avg_session_time = total_running_time / max(total_sessions, 1)
            remaining_time = self.total_target_seconds - total_running_time
            estimated_sessions_remaining = remaining_time / avg_session_time if avg_session_time > 0 else 0
        else:
            estimated_sessions_remaining = 0
        
        return {
            "total_sessions": total_sessions,
            "total_running_time": total_running_time,
            "total_distance": total_distance,
            "target_time": self.total_target_seconds,
            "target_distance": self.total_target_miles,
            "time_progress_percent": time_progress,
            "distance_progress_percent": distance_progress,
            "estimated_sessions_remaining": estimated_sessions_remaining,
            "time_remaining": self.total_target_seconds - total_running_time,
            "distance_remaining": self.total_target_miles - total_distance
        }
    
    def get_monthly_data(self, year: int, month: int) -> Dict:
        """Get aggregated data for a specific month"""
        sessions = self.load_all_sessions()
        monthly_sessions = []
        
        for session in sessions:
            session_date = datetime.datetime.fromisoformat(session["start_time"])
            if session_date.year == year and session_date.month == month:
                monthly_sessions.append(session)
        
        if not monthly_sessions:
            return {
                "year": year,
                "month": month,
                "sessions": [],
                "total_distance": 0,
                "total_time": 0,
                "total_sessions": 0,
                "daily_averages": {}
            }
        
        # Calculate daily aggregations
        daily_data = {}
        for session in monthly_sessions:
            session_date = datetime.datetime.fromisoformat(session["start_time"]).date()
            day_key = session_date.day
            
            if day_key not in daily_data:
                daily_data[day_key] = {
                    "distance": 0,
                    "time": 0,
                    "sessions": 0,
                    "calories": 0
                }
            
            daily_data[day_key]["distance"] += session.get("distance_miles", 0)
            daily_data[day_key]["time"] += session.get("running_time", 0)
            daily_data[day_key]["sessions"] += 1
            daily_data[day_key]["calories"] += session.get("calories", 0)
        
        total_distance = sum(session.get("distance_miles", 0) for session in monthly_sessions)
        total_time = sum(session.get("running_time", 0) for session in monthly_sessions)
        
        return {
            "year": year,
            "month": month,
            "sessions": monthly_sessions,
            "total_distance": total_distance,
            "total_time": total_time,
            "total_sessions": len(monthly_sessions),
            "daily_data": daily_data
        }
    
    def _save_session(self, session: Session) -> None:
        """Save session to JSON file"""
        sessions = self.load_all_sessions()
        
        # Convert session to dict
        session_dict = {
            "session_id": session.session_id,
            "start_time": session.start_time.isoformat(),
            "end_time": session.end_time.isoformat() if session.end_time else None,
            "breaks": session.breaks,
            "total_break_time": session.total_break_time,
            "running_time": session.running_time,
            "distance_miles": session.distance_miles,
            "calories": session.calories
        }
        
        sessions.append(session_dict)
        
        # Save to file
        with open(self.sessions_file, 'w') as f:
            json.dump(sessions, f, indent=2)
    
    def load_all_sessions(self) -> List[Dict]:
        """Load all sessions from JSON file"""
        if not os.path.exists(self.sessions_file):
            return []
        
        try:
            with open(self.sessions_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def format_time(self, seconds: int) -> str:
        """Format seconds into HH:MM:SS"""
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    
    def format_duration(self, seconds: int) -> str:
        """Format seconds into human-readable duration"""
        if seconds < 60:
            return f"{seconds} seconds"
        elif seconds < 3600:
            minutes = seconds // 60
            return f"{minutes} minutes"
        else:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            return f"{hours} hours, {minutes} minutes"

# Global timer instance
timer = ForrestGumpTimer()
