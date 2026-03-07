"""Smart Parking page - Find accessible parking spots"""

import streamlit as st
from utils import get_mock_parking

st.set_page_config(page_title="Smart Parking - Accessible Map AI", layout="wide")

def main():
    st.title("🅿️ Smart Parking")
    st.markdown("### Find and reserve accessible parking spaces")
    
    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Available Spots", "23", "-5", help="Accessible spots within 1km")
    
    with col2:
        st.metric("Avg. Distance", "0.3 km", "-0.1", help="Average distance to parking")
    
    with col3:
        st.metric("Avg. Rate", "$4/hr", "+$0.50", help="Average parking rate")
    
    with col4:
        st.metric("Reserved", "2", "+1", help="Your reserved spots")
    
    st.markdown("---")
    
    # Search Section
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        destination = st.text_input("🎯 Destination", placeholder="Where are you going?")
    
    with col2:
        duration = st.selectbox("Duration", ["30 min", "1 hour", "2 hours", "4 hours", "All day"])
    
    with col3:
        st.markdown("#### Filters")
        covered_only = st.checkbox("Covered only")
        max_distance = st.slider("Max distance (km)", 0.1, 2.0, 0.5)
    
    # Advanced Filters
    with st.expander("🔧 Advanced Filters"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Accessibility Features**")
            wide_spaces = st.checkbox("Extra wide spaces", value=True)
            level_access = st.checkbox("Level access", value=True)
            elevator = st.checkbox("Elevator available")
        
        with col2:
            st.markdown("**Amenities**")
            ev_charging = st.checkbox("EV charging")
            security_24_7 = st.checkbox("24/7 Security")
            restrooms = st.checkbox("Accessible restrooms")
        
        with col3:
            st.markdown("**Payment**")
            max_rate = st.slider("Max rate ($/hr)", 1, 20, 10)
            payment_method = st.multiselect(
                "Payment methods",
                ["Credit Card", "Mobile App", "Cash", "Contactless"]
            )
    
    if st.button("🔍 Search Parking", type="primary", use_container_width=True):
        
        # Get mock parking data
        parking_spots = get_mock_parking()
        
        st.markdown("---")
        st.markdown("### 📍 Available Parking")
        
        # Display parking options
        for spot in parking_spots:
            with st.container():
                col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
                
                with col1:
                    availability_color = "🟢" if spot['available'] > 3 else "🟡" if spot['available'] > 0 else "🔴"
                    st.markdown(f"### {availability_color} {spot['name']}")
                    
                    # Features badges
                    features_html = " ".join([f"<span style='background: #E3F2FD; padding: 2px 8px; border-radius: 12px; margin: 2px;'>{f}</span>" for f in spot['features']])
                    st.markdown(features_html, unsafe_allow_html=True)
                
                with col2:
                    st.metric("Available", f"{spot['available']}/{spot['accessible_spots']}")
                    st.caption(spot['rate'])
                
                with col3:
                    st.metric("Distance", f"{spot['distance']} km")
                    st.caption("5 min walk")
                
                with col4:
                    if spot['available'] > 0:
                        if st.button("Reserve", key=f"reserve_{spot['name']}", use_container_width=True):
                            st.success("Reserved!")
                    else:
                        st.button("Full", key=f"full_{spot['name']}", disabled=True, use_container_width=True)
                
                st.markdown("---")
    
    # Map View
    st.markdown("### 🗺️ Parking Map")
    
    # Placeholder for map
    st.info("🗺️ Interactive map showing parking locations would appear here")
    st.image("https://via.placeholder.com/800x400/4A90E2/FFFFFF?text=Parking+Map+View", use_column_width=True)
    
    # Reservations Section
    st.markdown("---")
    st.markdown("### 📋 My Reservations")
    
    tab1, tab2 = st.tabs(["Active", "History"])
    
    with tab1:
        if st.session_state.get('reservations'):
            for reservation in st.session_state['reservations']:
                st.info(f"📍 {reservation}")
        else:
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.info("**North Garage** - Space A12")
                st.caption("Reserved until 3:00 PM today")
            
            with col2:
                if st.button("Cancel", key="cancel_1"):
                    st.warning("Reservation cancelled")
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.info("**Central Plaza** - Space B05")
                st.caption("Tomorrow 9:00 AM - 12:00 PM")
            
            with col2:
                if st.button("Cancel", key="cancel_2"):
                    st.warning("Reservation cancelled")
    
    with tab2:
        st.info("📍 South Lot - Used yesterday (2 hours)")
        st.info("📍 East Side Parking - Used 3 days ago (4 hours)")
        st.info("📍 West End Garage - Used last week (All day)")
    
    # Tips Section
    st.markdown("---")
    st.markdown("### 💡 Parking Tips")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Peak Hours to Avoid:**
        • Weekdays: 8-10 AM, 5-7 PM
        • Saturdays: 11 AM - 3 PM
        • Event days: Check calendar
        """)
    
    with col2:
        st.success("""
        **Best Times for Parking:**
        • Early mornings (before 8 AM)
        • Mid-afternoon (2-4 PM)
        • Evenings after 7 PM
        """)

if __name__ == "__main__":
    main()
