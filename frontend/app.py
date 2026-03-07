import streamlit as st
import json
from pathlib import Path

# ================= PAGE CONFIGURATION =================
st.set_page_config(
    page_title="Accessible Map AI",
    page_icon="♿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= GLOBAL STYLES =================
st.markdown("""
<style>
.main { padding: 0rem 1rem; }

.stButton button {
    background: linear-gradient(135deg, #2F80ED, #56CCF2);
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.55rem 1rem;
    font-weight: 600;
    transition: 0.2s ease;
}
.stButton button:hover { transform: translateY(-2px); opacity: 0.95; }

.metric-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 1.5rem;
    border-radius: 12px;
    color: white;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.alert-box {
    background-color: #FFF3CD;
    border-left: 4px solid #FFC107;
    padding: 1rem;
    border-radius: 4px;
    margin: 1rem 0;
}

.card {
    background: #FFFFFF;
    padding: 1.4rem;
    border-radius: 14px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.06);
    border: 1px solid #F0F2F6;
}

.hero {
    text-align: center;
    padding: 2rem;
    border-radius: 12px;
}

.badge {
    display: inline-block;
    padding: 0.25rem 0.6rem;
    border-radius: 8px;
    font-size: 0.75rem;
    font-weight: 600;
    background-color: #E8F3FF;
    color: #2F80ED;
}
</style>
""", unsafe_allow_html=True)


def main():

    # SIDEBAR
    with st.sidebar:
        st.markdown("# ♿ Accessible Map AI")
        st.markdown("---")

        st.markdown("### Navigation")
        st.info("👈 Select a page from the sidebar")

        st.markdown("---")
        st.markdown("### 👤 User Profile")

        profile = st.selectbox(
            "Accessibility Mode",
            ["Standard", "Wheelchair User", "Visually Impaired", "Elderly", "Hearing Impaired"]
        )
        st.session_state['user_profile'] = profile

        st.markdown("---")

        col1, col2 = st.columns(2)
        col1.metric("Today's Routes", "12", "3")
        col2.metric("Safety Score", "92%", "5%")
        st.metric("Active Alerts", "2", "-1")

    # HEADER
    st.title("🗺️ Welcome to Accessible Map AI")
    st.markdown("### Your Smart Navigation Companion for Inclusive Travel")

    # HERO SECTION
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='hero' style='background:#F0F8FF;'>
            <h1>♿</h1>
            <h3>Wheelchair Accessible</h3>
            <p>Find barrier-free routes with ramp locations and elevator access</p>
            <span class="badge">Core Feature</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='hero' style='background:#F5FFFA;'>
            <h1>👁️</h1>
            <h3>Vision Assistance</h3>
            <p>Audio navigation and obstacle detection for safe travel</p>
            <span class="badge">AI Powered</span>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='hero' style='background:#FFF8DC;'>
            <h1>🏃</h1>
            <h3>Mobility Support</h3>
            <p>Optimized routes for elderly and mobility-impaired users</p>
            <span class="badge">Inclusive Design</span>
        </div>
        """, unsafe_allow_html=True)

    # QUICK ACTIONS
    st.markdown("---")
    st.markdown("### 🚀 Quick Actions")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🗺️ Plan Route", use_container_width=True):
            st.switch_page("pages/Route_planner.py")

    with col2:
        if st.button("👁️ Virtual Vision", use_container_width=True):
            st.switch_page("pages/Virtual_vision.py")

    with col3:
        if st.button("🆘 Emergency", use_container_width=True):
            st.switch_page("pages/Emergency.py")

    with col4:
        if st.button("⚙️ Settings", use_container_width=True):
            st.switch_page("pages/Settings.py")

    # PLATFORM HIGHLIGHTS
    st.markdown("---")
    st.markdown("### ⭐ Platform Highlights")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### ♿ Accessibility First")
        st.write("Personalized routes tailored to mobility and vision needs.")
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🤖 AI Assistance")
        st.write("Real-time alerts, predictions, and safety insights.")
        st.markdown('</div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🌐 Community Powered")
        st.write("Crowdsourced accessibility updates and reports.")
        st.markdown('</div>', unsafe_allow_html=True)

    # RECENT ACTIVITY
    st.markdown("---")
    st.markdown("### 📊 Recent Activity")

    tab1, tab2, tab3 = st.tabs(["Recent Routes", "Community Reports", "Alerts"])

    with tab1:
        st.info("🗺️ Museum District → Central Park - 92% Accessible")
        st.info("🗺️ Home → Medical Center - 88% Accessible")
        st.info("🗺️ Library → Shopping Mall - 95% Accessible")

    with tab2:
        st.warning("⚠️ Broken elevator at Station Square - Reported 2h ago")
        st.success("✅ New ramp installed at City Hall - Verified")

    with tab3:
        st.error("🚨 High traffic on Main Street - Consider alternate route")
        st.warning("⚠️ Construction on 5th Avenue - Limited accessibility")


if __name__ == "__main__":
    main()