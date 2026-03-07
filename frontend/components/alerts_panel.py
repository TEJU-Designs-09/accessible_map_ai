"""Alerts panel component for displaying system alerts"""

import streamlit as st
from datetime import datetime

def render_alerts_panel(alerts):
    """
    Render alerts panel with different alert types
    
    Args:
        alerts: List of alert dictionaries with type, message, and timestamp
    """
    
    st.markdown("### 🔔 Active Alerts")
    
    if not alerts:
        st.info("No active alerts at this time")
        return
    
    for alert in alerts:
        alert_type = alert.get('type', 'info')
        message = alert.get('message', '')
        timestamp = alert.get('timestamp', datetime.now().strftime('%H:%M'))
        
        if alert_type == 'error':
            st.error(f"🚨 {message} - {timestamp}")
        elif alert_type == 'warning':
            st.warning(f"⚠️ {message} - {timestamp}")
        elif alert_type == 'success':
            st.success(f"✅ {message} - {timestamp}")
        else:
            st.info(f"ℹ️ {message} - {timestamp}")
