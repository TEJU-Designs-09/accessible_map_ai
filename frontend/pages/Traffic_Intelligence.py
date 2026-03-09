"""Traffic Intelligence page - Real-time traffic and congestion info"""

import streamlit as st
import pandas as pd
from frontend.utils.helpers import get_mock_traffic

st.set_page_config(page_title="Traffic Intelligence - Accessible Map AI", layout="wide")

def main():
    st.title("🚦 Traffic Intelligence")
    st.markdown("### Real-time traffic analysis for accessible route planning")
    
    # Traffic Overview
    col1, col2, col3, col4 = st.columns(4)
    
    traffic_data = get_mock_traffic()
    
    with col1:
        congestion_color = {"Low": "🟢", "Medium": "🟡", "High": "🔴"}
        st.metric(
            "Congestion Level",
            traffic_data['congestion_level'],
            congestion_color.get(traffic_data['congestion_level'], "")
        )
    
    with col2:
        st.metric(
            "Avg Speed",
            f"{traffic_data['average_speed']} mph",
            f"{traffic_data['average_speed'] - 25} mph"
        )
    
    with col3:
        st.metric(
            "Active Incidents",
            traffic_data['incidents'],
            "+2 from hour ago"
        )
    
    with col4:
        st.metric(
            "Est. Delay",
            f"{traffic_data['estimated_delay']} min",
            f"+{traffic_data['estimated_delay']//2} min"
        )
    
    st.markdown("---")
    
    # Main Content
    tab1, tab2, tab3 = st.tabs(["🗺️ Live Map", "📊 Analytics", "⚠️ Incidents"])
    
    with tab1:
        st.markdown("#### Traffic Heatmap")
        
        # Mock heatmap
        fig = go.Figure(data=go.Heatmap(
            z=[[1, 2, 3, 2, 1],
               [2, 4, 5, 3, 2],
               [3, 5, 8, 6, 3],
               [2, 4, 6, 5, 2],
               [1, 2, 3, 2, 1]],
            x=['North', 'East', 'Central', 'West', 'South'],
            y=['Morning', 'Midday', 'Afternoon', 'Evening', 'Night'],
            colorscale='RdYlGn_r',
            text=[['Low', 'Low', 'Medium', 'Low', 'Low'],
                  ['Low', 'Medium', 'High', 'Medium', 'Low'],
                  ['Medium', 'High', 'Critical', 'High', 'Medium'],
                  ['Low', 'Medium', 'High', 'High', 'Low'],
                  ['Low', 'Low', 'Medium', 'Low', 'Low']],
            texttemplate="%{text}",
            textfont={"size": 10},
        ))
        
        fig.update_layout(
            title="Traffic Congestion Heatmap",
            xaxis_title="District",
            yaxis_title="Time of Day",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Accessible routes recommendation
        st.markdown("#### 🚶 Recommended Accessible Routes")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("✅ **Park Avenue Route** - Low traffic, fully accessible")
            st.info("ℹ️ **Museum District Path** - Moderate traffic, good accessibility")
        
        with col2:
            st.warning("⚠️ **Main Street** - High traffic, consider alternatives")
            st.error("❌ **Highway Underpass** - Very congested, poor accessibility")
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Traffic Patterns - Last 7 Days")
            
            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            peak_traffic = [85, 87, 82, 89, 92, 65, 58]
            accessible_impact = [70, 72, 68, 75, 78, 45, 40]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=days, y=peak_traffic,
                name='Peak Traffic %',
                line=dict(color='red', width=2)
            ))
            fig.add_trace(go.Scatter(
                x=days, y=accessible_impact,
                name='Accessibility Impact %',
                line=dict(color='blue', width=2)
            ))
            
            fig.update_layout(
                title="Weekly Traffic vs Accessibility",
                yaxis_title="Percentage",
                height=300
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("#### Peak Hours Distribution")
            
            hours = ["6AM", "9AM", "12PM", "3PM", "6PM", "9PM"]
            congestion = [30, 90, 50, 60, 95, 40]
            
            fig = px.bar(
                x=hours, y=congestion,
                color=congestion,
                color_continuous_scale="RdYlGn_r",
                title="Congestion by Hour"
            )
            
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        # Accessibility Impact Analysis
        st.markdown("#### 🎯 Accessibility Impact Analysis")
        
        impact_data = {
            "Factor": ["Heavy Traffic", "Road Work", "Events", "Weather", "Rush Hour"],
            "Impact on Wheelchair": [60, 85, 40, 70, 65],
            "Impact on Vision Impaired": [70, 90, 50, 60, 75],
            "Impact on Elderly": [75, 80, 45, 85, 70]
        }
        
        fig = go.Figure()
        
        for column in ["Impact on Wheelchair", "Impact on Vision Impaired", "Impact on Elderly"]:
            fig.add_trace(go.Bar(
                name=column.replace("Impact on ", ""),
                x=impact_data["Factor"],
                y=impact_data[column]
            ))
        
        fig.update_layout(
            title="Traffic Factors Impact on Different User Groups",
            yaxis_title="Impact Score",
            barmode='group',
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("#### 🚨 Current Traffic Incidents")
        
        incidents = [
            {
                "type": "🚧 Construction",
                "location": "5th Avenue & Main",
                "impact": "High",
                "duration": "2 hours",
                "accessibility": "❌ No wheelchair access"
            },
            {
                "type": "🚗 Accident",
                "location": "Highway Exit 12",
                "impact": "Medium",
                "duration": "45 min",
                "accessibility": "⚠️ Limited sidewalk access"
            },
            {
                "type": "🎪 Special Event",
                "location": "City Center",
                "impact": "Low",
                "duration": "All day",
                "accessibility": "✅ Alternative routes available"
            }
        ]
        
        for incident in incidents:
            with st.container():
                col1, col2, col3 = st.columns([2, 1, 1])
                
                with col1:
                    st.markdown(f"**{incident['type']}**")
                    st.caption(f"📍 {incident['location']}")
                
                with col2:
                    impact_color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
                    st.markdown(f"Impact: {impact_color.get(incident['impact'], '')} {incident['impact']}")
                    st.caption(f"Duration: {incident['duration']}")
                
                with col3:
                    st.markdown(incident['accessibility'])
                
                st.markdown("---")
    
    # Predictions Section
    st.markdown("---")
    st.markdown("### 🔮 Traffic Predictions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**Next Hour**: Traffic expected to decrease by 15%")
    
    with col2:
        st.warning("**Tomorrow 9 AM**: Heavy congestion expected - Plan alternate route")
    
    with col3:
        st.success("**Weekend**: Low traffic conditions - Ideal for accessible travel")

if __name__ == "__main__":
    main()
