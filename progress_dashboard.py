"""
Forrest Gump Timer - Progress Dashboard
Beautiful visualization dashboard with monthly graphs using Dash/Plotly
"""

import dash
from dash import dcc, html, Input, Output, callback
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import calendar
from forrest_timer import timer

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.title = "Forrest Gump Progress Dashboard"

# Custom CSS styling
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 20px;
                min-height: 100vh;
            }
            .dash-container {
                background: rgba(255, 255, 255, 0.95);
                border-radius: 15px;
                padding: 20px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(10px);
            }
            .header {
                text-align: center;
                color: #2c3e50;
                margin-bottom: 30px;
            }
            .header h1 {
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            .stat-card {
                background: linear-gradient(135deg, #3498db, #2980b9);
                border-radius: 10px;
                padding: 20px;
                margin: 10px;
                color: white;
                text-align: center;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            }
            .stat-value {
                font-size: 2em;
                font-weight: bold;
                margin-bottom: 5px;
            }
            .stat-label {
                font-size: 0.9em;
                opacity: 0.9;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

def get_progress_data():
    """Get comprehensive progress data"""
    progress = timer.get_overall_progress()
    sessions = timer.load_all_sessions()
    
    # Create DataFrame for easier manipulation
    if sessions:
        df = pd.DataFrame(sessions)
        df['start_time'] = pd.to_datetime(df['start_time'])
        df['date'] = df['start_time'].dt.date
        df['month'] = df['start_time'].dt.to_period('M')
    else:
        df = pd.DataFrame()
    
    return progress, df

def create_monthly_chart(df):
    """Create monthly progress chart"""
    if df.empty:
        return go.Figure().add_annotation(
            text="No data yet - Start your first session!",
            xref="paper", yref="paper",
            x=0.5, y=0.5, xanchor='center', yanchor='middle',
            showarrow=False, font=dict(size=16)
        )
    
    # Group by month
    monthly_data = df.groupby('month').agg({
        'distance_miles': 'sum',
        'running_time': 'sum',
        'calories': 'sum'
    }).reset_index()
    
    monthly_data['month_str'] = monthly_data['month'].astype(str)
    monthly_data['running_hours'] = monthly_data['running_time'] / 3600
    
    # Create subplots
    fig = go.Figure()
    
    # Distance bars
    fig.add_trace(go.Bar(
        x=monthly_data['month_str'],
        y=monthly_data['distance_miles'],
        name='Distance (miles)',
        marker_color='#3498db',
        text=monthly_data['distance_miles'].round(2),
        textposition='auto',
    ))
    
    fig.update_layout(
        title={
            'text': '📊 Monthly Distance Progress',
            'x': 0.5,
            'font': {'size': 20, 'color': '#2c3e50'}
        },
        xaxis_title='Month',
        yaxis_title='Distance (miles)',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2c3e50'),
        showlegend=False
    )
    
    return fig

def create_daily_heatmap(df):
    """Create daily activity heatmap"""
    if df.empty:
        return go.Figure().add_annotation(
            text="No data yet - Start your first session!",
            xref="paper", yref="paper",
            x=0.5, y=0.5, xanchor='center', yanchor='middle',
            showarrow=False, font=dict(size=16)
        )
    
    # Create daily aggregation
    daily_data = df.groupby('date').agg({
        'distance_miles': 'sum',
        'running_time': 'sum'
    }).reset_index()
    
    # Convert to datetime for easier manipulation
    daily_data['date'] = pd.to_datetime(daily_data['date'])
    daily_data['day_of_week'] = daily_data['date'].dt.day_name()
    daily_data['week'] = daily_data['date'].dt.isocalendar().week
    
    # Create heatmap data
    heatmap_data = daily_data.pivot_table(
        values='distance_miles', 
        index='day_of_week', 
        columns='week', 
        fill_value=0
    )
    
    # Reorder days
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    heatmap_data = heatmap_data.reindex(day_order)
    
    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data.values,
        x=[f'Week {w}' for w in heatmap_data.columns],
        y=heatmap_data.index,
        colorscale='Blues',
        showscale=True,
        colorbar=dict(title="Miles"),
        text=heatmap_data.values.round(2),
        texttemplate="%{text}",
        textfont={"size": 10},
    ))
    
    fig.update_layout(
        title={
            'text': '🔥 Daily Activity Heatmap',
            'x': 0.5,
            'font': {'size': 20, 'color': '#2c3e50'}
        },
        xaxis_title='Week',
        yaxis_title='Day of Week',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2c3e50')
    )
    
    return fig

def create_progress_gauge(progress):
    """Create progress gauge chart"""
    percentage = progress['distance_progress_percent']
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = percentage,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "🎯 Journey Progress", 'font': {'size': 20, 'color': '#2c3e50'}},
        delta = {'reference': 0, 'increasing': {'color': "#27ae60"}},
        gauge = {
            'axis': {'range': [None, 100], 'tickcolor': "#2c3e50"},
            'bar': {'color': "#e74c3c"},
            'steps': [
                {'range': [0, 25], 'color': "#ecf0f1"},
                {'range': [25, 50], 'color': "#bdc3c7"},
                {'range': [50, 75], 'color': "#95a5a6"},
                {'range': [75, 100], 'color': "#7f8c8d"}
            ],
            'threshold': {
                'line': {'color': "#27ae60", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2c3e50'),
        height=400
    )
    
    return fig

def create_cumulative_chart(df):
    """Create cumulative distance chart"""
    if df.empty:
        return go.Figure().add_annotation(
            text="No data yet - Start your first session!",
            xref="paper", yref="paper",
            x=0.5, y=0.5, xanchor='center', yanchor='middle',
            showarrow=False, font=dict(size=16)
        )
    
    # Sort by date and calculate cumulative distance
    daily_data = df.groupby('date').agg({
        'distance_miles': 'sum'
    }).reset_index()
    
    daily_data = daily_data.sort_values('date')
    daily_data['cumulative_distance'] = daily_data['distance_miles'].cumsum()
    
    # Target line (Forrest's total distance)
    target_distance = timer.total_target_miles
    
    fig = go.Figure()
    
    # Actual progress line
    fig.add_trace(go.Scatter(
        x=daily_data['date'],
        y=daily_data['cumulative_distance'],
        mode='lines+markers',
        name='Your Progress',
        line=dict(color='#3498db', width=3),
        marker=dict(size=6)
    ))
    
    # Target line
    fig.add_hline(
        y=target_distance,
        line_dash="dash",
        line_color="#e74c3c",
        annotation_text=f"Forrest's Goal: {target_distance:,.0f} miles",
        annotation_position="top left"
    )
    
    fig.update_layout(
        title={
            'text': '📈 Cumulative Distance Progress',
            'x': 0.5,
            'font': {'size': 20, 'color': '#2c3e50'}
        },
        xaxis_title='Date',
        yaxis_title='Cumulative Distance (miles)',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2c3e50'),
        showlegend=True
    )
    
    return fig

# App layout
app.layout = html.Div([
    html.Div([
        html.H1("🏃‍♂️ Forrest Gump Progress Dashboard", className="header"),
        html.P("\"Run, Forrest, Run!\" - Track your epic journey to complete Forrest's 3+ year run", 
               style={'textAlign': 'center', 'color': '#7f8c8d', 'fontSize': '1.2em'})
    ], className="header"),
    
    # Auto-refresh component
    dcc.Interval(
        id='interval-component',
        interval=30*1000,  # Update every 30 seconds
        n_intervals=0
    ),
    
    # Statistics cards
    html.Div(id='stats-cards', style={'marginBottom': '30px'}),
    
    # Charts
    html.Div([
        html.Div([
            dcc.Graph(id='progress-gauge')
        ], style={'width': '50%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Graph(id='monthly-chart')
        ], style={'width': '50%', 'display': 'inline-block'})
    ]),
    
    html.Div([
        dcc.Graph(id='cumulative-chart')
    ], style={'marginBottom': '20px'}),
    
    html.Div([
        dcc.Graph(id='daily-heatmap')
    ]),
    
    # Footer
    html.Div([
        html.P("💡 Data updates automatically every 30 seconds", 
               style={'textAlign': 'center', 'color': '#7f8c8d', 'marginTop': '30px'}),
        html.P("🔄 Close and reopen to see latest session data", 
               style={'textAlign': 'center', 'color': '#7f8c8d'})
    ])
], className="dash-container")

@callback(
    [Output('stats-cards', 'children'),
     Output('progress-gauge', 'figure'),
     Output('monthly-chart', 'figure'),
     Output('cumulative-chart', 'figure'),
     Output('daily-heatmap', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_dashboard(n):
    """Update all dashboard components"""
    progress, df = get_progress_data()
    
    # Create statistics cards
    stats_cards = html.Div([
        html.Div([
            html.Div(f"{progress['total_distance']:.1f}", className="stat-value"),
            html.Div("Miles Completed", className="stat-label")
        ], className="stat-card", style={'width': '18%', 'display': 'inline-block'}),
        
        html.Div([
            html.Div(timer.format_duration(int(progress['total_running_time'])), className="stat-value"),
            html.Div("Time Running", className="stat-label")
        ], className="stat-card", style={'width': '18%', 'display': 'inline-block'}),
        
        html.Div([
            html.Div(f"{progress['distance_progress_percent']:.3f}%", className="stat-value"),
            html.Div("Journey Complete", className="stat-label")
        ], className="stat-card", style={'width': '18%', 'display': 'inline-block'}),
        
        html.Div([
            html.Div(f"{progress['distance_remaining']:.0f}", className="stat-value"),
            html.Div("Miles Remaining", className="stat-label")
        ], className="stat-card", style={'width': '18%', 'display': 'inline-block'}),
        
        html.Div([
            html.Div(str(progress['total_sessions']), className="stat-value"),
            html.Div("Total Sessions", className="stat-label")
        ], className="stat-card", style={'width': '18%', 'display': 'inline-block'})
    ], style={'textAlign': 'center'})
    
    return (
        stats_cards,
        create_progress_gauge(progress),
        create_monthly_chart(df),
        create_cumulative_chart(df),
        create_daily_heatmap(df)
    )

if __name__ == '__main__':
    print("🚀 Starting Forrest Gump Progress Dashboard...")
    print("📊 Open your browser to: http://localhost:8050")
    print("🔄 Dashboard updates automatically every 30 seconds")
    print("🏃‍♂️ Run, Forrest, Run!")
    
    app.run_server(debug=False, host='localhost', port=8050)
