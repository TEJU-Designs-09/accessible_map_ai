"""Route card component for displaying route information"""

import streamlit as st

def render_route_card(route_name, accessibility_score, duration, distance, alerts=None, features=None):
    """
    Render a route card with accessibility information
    
    Args:
        route_name: Name of the route
        accessibility_score: Score from 0-100
        duration: Estimated time
        distance: Route distance
        alerts: List of alerts
        features: List of accessibility features
    """
    
    with st.container():
        # Card styling
        card_style = f"""
        <div style='
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 12px;
            color: white;
            margin: 1rem 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        '>
        """
        
        # Score color
        if accessibility_score >= 90:
            score_color = "#4CAF50"
            score_emoji = "✅"
        elif accessibility_score >= 70:
            score_color = "#FFC107"
            score_emoji = "⚠️"
        else:
            score_color = "#F44336"
            score_emoji = "❌"
        
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            st.markdown(f"### 🗺️ {route_name}")
            if features:
                st.markdown(" • ".join(features))
        
        with col2:
            st.metric("Accessibility", f"{accessibility_score}%", delta=None)
            st.markdown(f"**Duration:** {duration}")
        
        with col3:
            st.markdown(f"**Distance:** {distance}")
            st.button("Select Route", key=f"route_{route_name}", use_container_width=True)
        
        # Alerts section
        if alerts:
            with st.expander("⚠️ View Alerts"):
                for alert in alerts:
                    st.warning(alert)
