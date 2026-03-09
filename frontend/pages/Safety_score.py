"""Safety Score page - Route and area safety analytics"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Safety Score - Accessible Map AI", layout="wide")

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
    st.title("🛡️ Safety Intelligence")
    st.markdown("### Comprehensive safety analysis for routes and surroundings")
    st.caption("Safety scores are derived from infrastructure quality, risk factors, and time-based conditions")

    # ---------- OVERALL METRICS ----------
    st.markdown("#### 📊 Overall Safety Indicators")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Current Area Safety", "87/100", "+3", help="Based on crime data, lighting, and emergency access")

    with col2:
        st.metric("Route Safety", "92/100", "+5", help="Safety score of your current route")

    with col3:
        st.metric("Time-based Risk", "Low", "↓", help="Current time safety assessment")

    with col4:
        st.metric("Emergency Response", "3 min", "-30s", help="Average emergency response time")

    st.markdown("---")

    # ---------- TABS ----------
    tab1, tab2, tab3, tab4 = st.tabs(["🗺️ Area Analysis", "📊 Safety Metrics", "⏰ Time Patterns", "🚨 Alerts"])

    # ===== AREA ANALYSIS =====
    with tab1:
        st.markdown("#### Safety Heatmap by District")

        col1, col2 = st.columns([2, 1])

        with col1:
            districts = ['Downtown', 'Midtown', 'Uptown', 'Suburbs', 'Industrial']
            times = ['Morning', 'Afternoon', 'Evening', 'Night']

            safety_scores = [
                [85, 88, 82, 70],
                [90, 92, 88, 75],
                [88, 90, 85, 72],
                [92, 93, 91, 85],
                [75, 78, 70, 60]
            ]

            fig = go.Figure(data=go.Heatmap(
                z=safety_scores,
                x=times,
                y=districts,
                colorscale='RdYlGn',
                text=safety_scores,
                texttemplate="%{text}",
                textfont={"size": 12},
                colorbar=dict(title="Safety Score")
            ))

            fig.update_layout(
                title="District Safety Scores by Time of Day",
                height=400
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("#### Top Safe Areas")
            st.success("Suburbs — Score: 92/100")
            st.success("Midtown — Score: 90/100")
            st.info("Uptown — Score: 88/100")

            st.markdown("#### Areas to Avoid")
            st.warning("Industrial — Score: 68/100")
            st.error("Downtown (Night) — Score: 70/100")

    # ===== SAFETY COMPONENTS =====
    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Safety Components")

            components = ['Lighting', 'Crime Rate', 'Emergency Access', 'Sidewalk Quality', 'Traffic Safety']
            scores = [85, 78, 92, 88, 80]

            fig = go.Figure(go.Scatterpolar(
                r=scores,
                theta=components,
                fill='toself',
                name='Current Location'
            ))

            fig.add_trace(go.Scatterpolar(
                r=[90, 85, 95, 90, 85],
                theta=components,
                fill='toself',
                name='City Average'
            ))

            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                showlegend=True,
                title="Safety Component Analysis"
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("#### Risk Factors")

            risk_factors = {
                "Poor Lighting": 25,
                "Isolated Areas": 20,
                "High Crime": 15,
                "No Sidewalks": 18,
                "Heavy Traffic": 12,
                "Construction": 10
            }

            fig = px.pie(
                values=list(risk_factors.values()),
                names=list(risk_factors.keys()),
                title="Risk Factor Distribution"
            )

            st.plotly_chart(fig, use_container_width=True)

    # ===== TIME PATTERNS =====
    with tab3:
        st.markdown("#### Safety Trends Throughout the Day")

        hours = list(range(24))
        safety = [85, 87, 88, 85, 82, 78, 75, 80, 85, 88, 90, 92, 91, 90, 88, 85, 82, 78, 72, 68, 65, 70, 75, 80]

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=hours,
            y=safety,
            mode='lines+markers',
            name='Safety Score',
            line=dict(width=3),
            fill='tonexty'
        ))

        fig.add_hrect(y0=85, y1=100, fillcolor="green", opacity=0.1, annotation_text="Safe")
        fig.add_hrect(y0=70, y1=85, fillcolor="yellow", opacity=0.1, annotation_text="Moderate")
        fig.add_hrect(y0=0, y1=70, fillcolor="red", opacity=0.1, annotation_text="Caution")

        fig.update_layout(
            title="24-Hour Safety Pattern",
            xaxis_title="Hour of Day",
            yaxis_title="Safety Score",
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("#### 💡 Time-based Recommendations")

        col1, col2 = st.columns(2)

        with col1:
            st.success("Best Times to Travel")
            st.write("• 9 AM - 5 PM (Score: 90+)")
            st.write("• 6 AM - 8 AM (Score: 85+)")

        with col2:
            st.warning("Avoid if Possible")
            st.write("• 11 PM - 5 AM (Score: <70)")
            st.write("• 7 PM - 9 PM in Industrial area")

    # ===== ALERTS =====
    with tab4:
        st.markdown("#### 🚨 Active Safety Alerts")

        alerts = [
            {"level": "high", "title": "Poor Lighting Reported", "location": "Park Avenue Underpass", "time": "Active since 3 days ago", "action": "Use alternate route after dark"},
            {"level": "medium", "title": "Isolated Area", "location": "Industrial District - Sector 5", "time": "Permanent warning", "action": "Travel in groups recommended"},
            {"level": "low", "title": "Construction Zone", "location": "Main Street & 3rd", "time": "Next 2 weeks", "action": "Sidewalk detour available"}
        ]

        for alert in alerts:
            if alert["level"] == "high":
                container = st.error
            elif alert["level"] == "medium":
                container = st.warning
            else:
                container = st.info

            with container(f"{alert['title']}"):
                st.write(f"📍 {alert['location']}")
                st.write(f"⏰ {alert['time']}")
                st.write(f"💡 {alert['action']}")

    # ---------- SETTINGS ----------
    st.markdown("---")
    st.markdown("### ⚙️ Personal Safety Preferences")

    col1, col2, col3 = st.columns(3)

    with col1:
        min_safety = st.slider("Minimum Safety Score", 0, 100, 70)
        avoid_night = st.checkbox("Avoid night routes", value=True)

    with col2:
        emergency_contacts = st.checkbox("Share location with emergency contacts", value=True)
        auto_reroute = st.checkbox("Auto-reroute for safety", value=True)

    with col3:
        alert_threshold = st.select_slider(
            "Alert Sensitivity",
            options=["Low", "Medium", "High"],
            value="Medium"
        )

        if st.button("💾 Save Preferences", use_container_width=True):
            st.success("Safety preferences saved!")


if __name__ == "__main__":
    main()
