"""Dashboard page - Main overview of accessibility metrics"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from components import render_alerts_panel, render_score_badge
from utils import get_mock_routes, get_mock_reports

st.set_page_config(page_title="Dashboard - Accessible Map AI", layout="wide")

# ---------- PAGE HEADER ----------
st.markdown("""
<style>
.section-card {
    background: #FFFFFF;
    padding: 1.2rem;
    border-radius: 14px;
    border: 1px solid #ECEFF5;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}
</style>
""", unsafe_allow_html=True)


def main():
    st.title("🏠 Dashboard")
    st.markdown("### Your Accessibility Overview")
    st.caption("Track accessibility performance, safety insights, and recent navigation activity")

    # ---------- KEY METRICS ----------
    st.markdown("#### 📊 Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Today's Accessibility Score",
            value="92%",
            delta="+5% from yesterday",
            help="Average accessibility score of your routes today"
        )

    with col2:
        st.metric(
            label="Routes Taken",
            value="8",
            delta="+2 from yesterday",
            help="Number of routes navigated"
        )

    with col3:
        st.metric(
            label="Obstacles Avoided",
            value="15",
            delta="-3 from yesterday",
            help="Obstacles successfully navigated around"
        )

    with col4:
        st.metric(
            label="Community Points",
            value="234",
            delta="+12 this week",
            help="Points earned from community contributions"
        )

    st.markdown("---")

    # ---------- CHARTS ----------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📈 Weekly Accessibility Trends")

        dates = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        scores = [88, 90, 85, 92, 91, 93, 92]

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dates,
            y=scores,
            mode='lines+markers',
            line=dict(width=3),
            marker=dict(size=8),
            fill='tonexty',
            name='Accessibility Score'
        ))

        fig.update_layout(
            title="Weekly Score Trend",
            yaxis_title="Score (%)",
            yaxis=dict(range=[80, 100]),
            height=320,
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### 🧭 Route Categories Used")

        route_types = ["Wheelchair Accessible", "Vision Assisted", "Elderly Friendly", "Standard"]
        values = [35, 25, 20, 20]

        fig = px.pie(
            values=values,
            names=route_types
        )

        fig.update_layout(height=320)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ---------- RECENT ACTIVITY ----------
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("#### 🕒 Recent Routes")

        routes = get_mock_routes("Current Location", "Destination")[:3]

        for route in routes:
            with st.container():
                st.markdown('<div class="section-card">', unsafe_allow_html=True)

                rcol1, rcol2, rcol3 = st.columns([3, 1, 1])

                with rcol1:
                    st.write(f"**{route['name']}**")
                    st.caption(f"Features: {', '.join(route['features'][:3])}")

                with rcol2:
                    render_score_badge(
                        "Score",
                        f"{route['accessibility_score']}%",
                        badge_type="success" if route['accessibility_score'] > 90 else "warning"
                    )

                with rcol3:
                    st.write(f"⏱️ {route['duration']} min")

                st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("#### 🔔 Active Alerts")

        alerts = [
            {"type": "warning", "message": "Construction on Main St", "timestamp": "10:30"},
            {"type": "info", "message": "New ramp at Station", "timestamp": "09:15"},
            {"type": "error", "message": "Elevator outage - Tower B", "timestamp": "08:45"}
        ]

        for alert in alerts:
            if alert['type'] == 'error':
                st.error(alert['message'])
            elif alert['type'] == 'warning':
                st.warning(alert['message'])
            else:
                st.info(alert['message'])

    st.markdown("---")

    # ---------- QUICK ACTIONS ----------
    st.markdown("#### ⚡ Quick Actions")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🗺️ Plan New Route", use_container_width=True):
            st.switch_page("pages/Route_planner.py")

    with col2:
        if st.button("📝 Report Obstacle", use_container_width=True):
            st.switch_page("pages/Community_reports.py")

    with col3:
        if st.button("🅿️ Find Parking", use_container_width=True):
            st.switch_page("pages/Smart_parking.py")

    with col4:
        if st.button("🆘 Emergency Help", use_container_width=True):
            st.switch_page("pages/Emergency.py")


if __name__ == "__main__":
    main()