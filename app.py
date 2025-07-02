"""
Forrest Gump Timer - Web Application
Flask web server for mobile access and local hosting
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime
from forrest_timer import timer
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Main timer page"""
    return render_template('index.html')

@app.route('/api/start_session', methods=['POST'])
def start_session():
    """Start a new session"""
    try:
        session_id = timer.start_session()
        return jsonify({
            'success': True,
            'session_id': session_id,
            'message': 'Session started successfully!'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/stop_session', methods=['POST'])
def stop_session():
    """Stop current session"""
    try:
        session_data = timer.stop_session()
        return jsonify({
            'success': True,
            'data': session_data
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/add_break', methods=['POST'])
def add_break():
    """Add break time to current session"""
    try:
        data = request.get_json()
        minutes = int(data.get('minutes', 0))
        seconds = int(data.get('seconds', 0))
        
        timer.add_break(minutes, seconds)
        return jsonify({
            'success': True,
            'message': f'Break added: {minutes:02d}:{seconds:02d}'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/session_stats')
def session_stats():
    """Get current session statistics"""
    try:
        stats = timer.get_session_stats()
        return jsonify({
            'success': True,
            'data': stats
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/overall_progress')
def overall_progress():
    """Get overall progress statistics"""
    try:
        progress = timer.get_overall_progress()
        return jsonify({
            'success': True,
            'data': progress
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/monthly_data/<int:year>/<int:month>')
def monthly_data(year, month):
    """Get monthly data for graphs"""
    try:
        data = timer.get_monthly_data(year, month)
        return jsonify({
            'success': True,
            'data': data
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/export_data')
def export_data():
    """Export all session data"""
    try:
        sessions = timer.load_all_sessions()
        progress = timer.get_overall_progress()
        
        export_data = {
            'export_date': datetime.now().isoformat(),
            'total_sessions': len(sessions),
            'overall_progress': progress,
            'sessions': sessions
        }
        
        return jsonify({
            'success': True,
            'data': export_data
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/progress')
def progress_page():
    """Progress visualization page"""
    return render_template('progress.html')

if __name__ == '__main__':
    print("🚀 Starting Forrest Gump Timer Web Server...")
    print("🌐 Open your browser to: http://localhost:5000")
    print("📱 Access from your phone using your computer's IP address")
    print("🏃‍♂️ Run, Forrest, Run!")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
