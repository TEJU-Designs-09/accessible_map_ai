"""Score badges component for displaying various scores"""

import streamlit as st

def render_score_badge(label, value, delta=None, badge_type="default"):
    """
    Render a score badge with optional delta
    
    Args:
        label: Badge label
        value: Score value
        delta: Change in score
        badge_type: Type of badge (success, warning, danger, default)
    """
    
    colors = {
        "success": "#4CAF50",
        "warning": "#FFC107",
        "danger": "#F44336",
        "default": "#2196F3"
    }
    
    color = colors.get(badge_type, colors["default"])
    
    badge_html = f"""
    <div style='
        background: {color};
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-block;
        margin: 0.25rem;
        font-weight: bold;
    '>
        {label}: {value}
        {f' ({delta})' if delta else ''}
    </div>
    """
    
    st.markdown(badge_html, unsafe_allow_html=True)
