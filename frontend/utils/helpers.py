"""Helper functions for the application"""

import random
from datetime import datetime, timedelta

def calculate_accessibility_score(features):
    """
    Calculate accessibility score based on features
    
    Args:
        features: Dictionary of accessibility features
    
    Returns:
        Score from 0-100
    """
    base_score = 50
    
    if features.get('wheelchair_accessible'):
        base_score += 20
    if features.get('elevator_available'):
        base_score += 10
    if features.get('audio_signals'):
        base_score += 10
    if features.get('braille_signs'):
        base_score += 5
    if features.get('wide_pathways'):
        base_score += 5
    
    return min(100, base_score)

def format_duration(minutes):
    """Format duration in minutes to human readable format"""
    if minutes < 60:
        return f"{minutes} min"
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}h {mins}min"

def generate_mock_coordinates():
    """Generate mock GPS coordinates"""
    lat = 40.7128 + random.uniform(-0.1, 0.1)
    lon = -74.0060 + random.uniform(-0.1, 0.1)
    return lat, lon

def generate_timestamp(hours_ago=0):
    """Generate timestamp for mock data"""
    time = datetime.now() - timedelta(hours=hours_ago)
    return time.strftime("%Y-%m-%d %H:%M:%S")

def get_mock_traffic():
    return {
        "congestion_level": "Medium",
        "average_speed": 32,
        "incidents": 4,
        "estimated_delay": 12
    }
