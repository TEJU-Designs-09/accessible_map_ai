"""Assisted Travel page - Request and provide travel assistance"""

import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Assisted Travel - Accessible Map AI", layout="wide")

def main():
    st.title("🤝 Assisted Travel")
    st.markdown("### Connect with volunteers for personalized travel assistance")
    
    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Active Volunteers", "23", "+5", help="Volunteers available now")
    
    with col2:
        st.metric("Avg Wait Time", "8 min", "-2 min", help="Average response time")
    
    with col3:
        st.metric("Success Rate", "96%", "+2%", help="Successful assistance rate")
    
    with col4:
        st.metric("Your Trips", "5", "+1", help="Assisted trips this month")
    
    st.markdown("---")
    
    # Main Content
    tab1, tab2, tab3, tab4 = st.tabs(["🆘 Request Assistance", "👥 Be a Volunteer", "📅 Scheduled", "💬 Messages"])
    
    with tab1:
        st.markdown("#### Request Travel Assistance")
        
        assistance_type = st.radio(
            "Type of Assistance Needed",
            ["Immediate Help", "Schedule for Later", "Recurring Assistance"]
        )
        
        if assistance_type == "Immediate Help":
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("##### Trip Details")
                start = st.text_input("📍 Current Location", value="Using GPS location...")
                destination = st.text_input("🎯 Destination", placeholder="Where do you need to go?")
                
                assistance_needs = st.multiselect(
                    "Assistance Required",
                    ["Wheelchair pushing", "Visual guidance", "Carry items", "Communication help", "General companionship"]
                )
            
            with col2:
                st.markdown("##### Additional Information")
                special_requirements = st.text_area(
                    "Special Requirements",
                    placeholder="Any specific needs or medical conditions...",
                    height=100
                )
                
                preferred_gender = st.selectbox("Preferred Helper", ["No preference", "Male", "Female"])
                language = st.selectbox("Language", ["English", "Spanish", "Mandarin", "Other"])
            
            if st.button("🆘 Request Immediate Assistance", type="primary", use_container_width=True):
                with st.spinner("Finding available volunteers..."):
                    st.success("✅ Volunteer found! John D. will arrive in approximately 8 minutes.")
                    
                    # Show volunteer info
                    with st.container():
                        col1, col2 = st.columns([1, 2])
                        with col1:
                            st.image("https://via.placeholder.com/150/4A90E2/FFFFFF?text=John+D.", use_column_width=True)
                        with col2:
                            st.markdown("**Volunteer: John D.**")
                            st.markdown("⭐⭐⭐⭐⭐ 4.9 rating (127 trips)")
                            st.markdown("✅ Background checked")
                            st.markdown("🗣️ Languages: English, Spanish")
                            
                            col_a, col_b = st.columns(2)
                            with col_a:
                                if st.button("📞 Call", use_container_width=True):
                                    st.info("Calling...")
                            with col_b:
                                if st.button("💬 Message", use_container_width=True):
                                    st.info("Opening chat...")
        
        elif assistance_type == "Schedule for Later":
            col1, col2 = st.columns(2)
            
            with col1:
                date = st.date_input("Date", min_value=datetime.now())
                time = st.time_input("Time")
                duration = st.selectbox("Estimated Duration", ["30 min", "1 hour", "2 hours", "Half day", "Full day"])
            
            with col2:
                start = st.text_input("📍 Pickup Location")
                destination = st.text_input("🎯 Destination")
                return_trip = st.checkbox("Need return trip assistance")
            
            if st.button("📅 Schedule Assistance", use_container_width=True):
                st.success("✅ Assistance scheduled! You'll receive a confirmation 24 hours before.")
        
        else:  # Recurring Assistance
            st.markdown("##### Set up recurring travel assistance")
            
            col1, col2 = st.columns(2)
            
            with col1:
                frequency = st.selectbox("Frequency", ["Daily", "Weekdays", "Weekly", "Custom"])
                if frequency == "Weekly":
                    days = st.multiselect("Select Days", ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
                
                time = st.time_input("Regular Time")
                duration_weeks = st.number_input("Duration (weeks)", min_value=1, max_value=52, value=4)
            
            with col2:
                route = st.text_input("Regular Route", placeholder="e.g., Home to Medical Center")
                preferred_volunteer = st.checkbox("Request same volunteer when possible")
                notes = st.text_area("Special Instructions", height=100)
            
            if st.button("🔄 Set Up Recurring Assistance", use_container_width=True):
                st.success("✅ Recurring assistance set up successfully!")
    
    with tab2:
        st.markdown("#### Become a Volunteer")
        
        volunteer_status = st.checkbox("I want to volunteer")
        
        if volunteer_status:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("##### Availability")
                availability = st.multiselect(
                    "Available Days",
                    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                )
                
                time_slots = st.multiselect(
                    "Preferred Times",
                    ["Morning (6AM-12PM)", "Afternoon (12PM-6PM)", "Evening (6PM-10PM)"]
                )
                
                max_distance = st.slider("Maximum Distance (km)", 1, 20, 5)
            
            with col2:
                st.markdown("##### Skills & Preferences")
                skills = st.multiselect(
                    "I can help with",
                    ["Wheelchair assistance", "Visual guidance", "Sign language", "Heavy lifting", "Medical emergencies"]
                )
                
                languages = st.multiselect(
                    "Languages Spoken",
                    ["English", "Spanish", "Mandarin", "French", "Arabic", "Other"]
                )
                
                vehicle = st.checkbox("I have a vehicle")
                if vehicle:
                    vehicle_type = st.selectbox("Vehicle Type", ["Car", "Van", "SUV"])
                    wheelchair_accessible = st.checkbox("Wheelchair accessible vehicle")
            
            if st.button("💚 Start Volunteering", type="primary", use_container_width=True):
                st.success("🎉 Thank you for volunteering! You're now active and will receive requests.")
                st.balloons()
        
        # Volunteer Stats
        st.markdown("---")
        st.markdown("##### Your Volunteer Stats")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Trips Completed", "0", help="Start volunteering to earn stats")
        with col2:
            st.metric("People Helped", "0")
        with col3:
            st.metric("Hours Volunteered", "0")
        with col4:
            st.metric("Rating", "N/A")
    
    with tab3:
        st.markdown("#### 📅 Scheduled Assistance")
        
        # Upcoming
        st.markdown("##### Upcoming")
        
        upcoming = [
            {
                "date": "Tomorrow, 2:00 PM",
                "type": "Medical Appointment",
                "volunteer": "Sarah M.",
                "status": "Confirmed"
            },
            {
                "date": "Friday, 10:00 AM",
                "type": "Grocery Shopping",
                "volunteer": "Pending",
                "status": "Searching"
            }
        ]
        
        for trip in upcoming:
            with st.container():
                col1, col2, col3 = st.columns([2, 1, 1])
                
                with col1:
                    st.markdown(f"**{trip['date']}**")
                    st.caption(trip['type'])
                
                with col2:
                    if trip['volunteer'] != "Pending":
                        st.markdown(f"Volunteer: {trip['volunteer']}")
                    else:
                        st.warning("Searching for volunteer")
                
                with col3:
                    if st.button("Cancel", key=f"cancel_{trip['date']}"):
                        st.warning("Trip cancelled")
                
                st.markdown("---")
        
        # Past
        st.markdown("##### Past Assistance")
        
        past_trips = [
            "Last Monday - Grocery shopping with Mike R. ⭐⭐⭐⭐⭐",
            "Jan 10 - Medical appointment with Sarah M. ⭐⭐⭐⭐",
            "Jan 5 - Park visit with John D. ⭐⭐⭐⭐⭐"
        ]
        
        for trip in past_trips:
            st.info(trip)
    
    with tab4:
        st.markdown("#### 💬 Messages")
        
        # Conversations
        conversations = [
            {"name": "John D.", "message": "I'm 5 minutes away!", "time": "2 min ago", "unread": True},
            {"name": "Sarah M.", "message": "See you tomorrow at 2 PM", "time": "1 hour ago", "unread": False},
            {"name": "Support Team", "message": "Welcome to Assisted Travel!", "time": "Yesterday", "unread": False}
        ]
        
        for conv in conversations:
            with st.container():
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    if conv['unread']:
                        st.markdown(f"**🔴 {conv['name']}**")
                        st.markdown(f"**{conv['message']}**")
                    else:
                        st.markdown(f"**{conv['name']}**")
                        st.caption(conv['message'])
                
                with col2:
                    st.caption(conv['time'])
                    if st.button("Open", key=f"open_{conv['name']}"):
                        st.info("Opening chat...")
                
                st.markdown("---")

if __name__ == "__main__":
    main()
