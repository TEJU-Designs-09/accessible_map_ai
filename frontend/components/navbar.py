"""Navigation bar component"""

import streamlit as st

def render_navbar():
    """Render the navigation bar with accessibility info"""

    # Navbar container styling
    st.markdown("""
    <style>
    .navbar {
        background: #FFFFFF;
        padding: 0.6rem 1rem;
        border-radius: 12px;
        border: 1px solid #E6EAF1;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        margin-bottom: 0.5rem;
    }
    .nav-title {
        font-weight: 700;
        font-size: 1.25rem;
    }
    .status-badge {
        display: inline-block;
        padding: 0.25rem 0.55rem;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 600;
        background-color: #EEF6FF;
        color: #2F80ED;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="navbar">', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

    with col1:
        st.markdown('<div class="nav-title">♿ Accessible Map AI</div>', unsafe_allow_html=True)

    with col2:
        profile = st.session_state.get('user_profile', 'Standard')
        st.markdown(f'Profile<br><span class="status-badge">{profile}</span>', unsafe_allow_html=True)

    with col3:
        st.markdown('Location<br><span class="status-badge">Active</span>', unsafe_allow_html=True)

    with col4:
        st.markdown('Alerts<br><span class="status-badge">2 New</span>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)