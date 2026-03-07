"""Settings page - User preferences and app configuration"""

import streamlit as st

st.set_page_config(page_title="Settings - Accessible Map AI", layout="wide")

def main():
    st.title("⚙️ Settings")
    st.markdown("### Configure your accessibility preferences and app settings")
    
    # Settings Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "♿ Accessibility", "🔔 Notifications", "🗺️ Navigation", "👤 Profile", "🔐 Privacy"
    ])
    
    with tab1:
        st.markdown("#### Accessibility Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### Mobility Settings")
            
            mobility_profile = st.selectbox(
                "Mobility Profile",
                ["No limitations", "Wheelchair user", "Walking aid user", "Limited mobility"]
            )
            
            if mobility_profile != "No limitations":
                max_incline = st.slider("Maximum incline (%)", 0, 15, 5)
                need_ramps = st.checkbox("Require ramps", value=True)
                need_elevators = st.checkbox("Require elevators for multi-level", value=True)
                avoid_stairs = st.checkbox("Avoid stairs completely", value=True)
                rest_stops = st.checkbox("Include rest stops", value=False)
            
            st.markdown("##### Vision Settings")
            
            vision_profile = st.selectbox(
                "Vision Profile",
                ["Normal vision", "Low vision", "Blind", "Color blind"]
            )
            
            if vision_profile != "Normal vision":
                high_contrast = st.checkbox("High contrast mode", value=True)
                large_text = st.checkbox("Large text", value=True)
                screen_reader = st.checkbox("Screen reader optimization", value=True)
                audio_cues = st.checkbox("Enhanced audio cues", value=True)
        
        with col2:
            st.markdown("##### Hearing Settings")
            
            hearing_profile = st.selectbox(
                "Hearing Profile",
                ["Normal hearing", "Hard of hearing", "Deaf"]
            )
            
            if hearing_profile != "Normal hearing":
                visual_alerts = st.checkbox("Visual alerts", value=True)
                vibration = st.checkbox("Vibration alerts", value=True)
                captions = st.checkbox("Live captions", value=True)
            
            st.markdown("##### Cognitive Settings")
            
            cognitive_support = st.checkbox("Enable cognitive support")
            
            if cognitive_support:
                simple_mode = st.checkbox("Simplified interface", value=True)
                reminders = st.checkbox("Frequent reminders", value=True)
                confirmation = st.checkbox("Confirm all actions", value=True)
                pictograms = st.checkbox("Use pictograms", value=True)
        
        if st.button("💾 Save Accessibility Settings", use_container_width=True, type="primary"):
            st.success("✅ Accessibility settings saved!")
    
    with tab2:
        st.markdown("#### Notification Preferences")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### Alert Types")
            
            route_alerts = st.checkbox("Route updates", value=True)
            obstacle_alerts = st.checkbox("Obstacle warnings", value=True)
            traffic_alerts = st.checkbox("Traffic conditions", value=True)
            safety_alerts = st.checkbox("Safety notifications", value=True)
            community_alerts = st.checkbox("Community reports", value=False)
            
            st.markdown("##### Alert Methods")
            
            push_notif = st.checkbox("Push notifications", value=True)
            email_notif = st.checkbox("Email alerts", value=False)
            sms_notif = st.checkbox("SMS alerts", value=False)
            in_app = st.checkbox("In-app notifications", value=True)
        
        with col2:
            st.markdown("##### Alert Timing")
            
            quiet_hours = st.checkbox("Enable quiet hours")
            
            if quiet_hours:
                col_a, col_b = st.columns(2)
                with col_a:
                    quiet_start = st.time_input("Quiet hours start")
                with col_b:
                    quiet_end = st.time_input("Quiet hours end")
            
            st.markdown("##### Alert Frequency")
            
            frequency = st.select_slider(
                "Notification frequency",
                options=["All", "Important only", "Critical only"],
                value="Important only"
            )
            
            bundle = st.checkbox("Bundle notifications", value=True)
            
            if bundle:
                bundle_interval = st.selectbox(
                    "Bundle interval",
                    ["Every 15 min", "Every 30 min", "Every hour", "Twice daily"]
                )
        
        if st.button("💾 Save Notification Settings", use_container_width=True, type="primary"):
            st.success("✅ Notification settings saved!")
    
    with tab3:
        st.markdown("#### Navigation Preferences")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### Route Preferences")
            
            route_type = st.selectbox(
                "Preferred route type",
                ["Most accessible", "Fastest", "Safest", "Scenic"]
            )
            
            avoid_options = st.multiselect(
                "Avoid",
                ["Highways", "Unpaved roads", "Busy intersections", "Hills", "Isolated areas"]
            )
            
            public_transport = st.checkbox("Include public transport", value=True)
            
            if public_transport:
                transport_modes = st.multiselect(
                    "Transport modes",
                    ["Bus", "Subway", "Train", "Tram"],
                    default=["Bus", "Subway"]
                )
        
        with col2:
            st.markdown("##### Voice Navigation")
            
            voice_enabled = st.checkbox("Enable voice navigation", value=True)
            
            if voice_enabled:
                voice_type = st.selectbox(
                    "Voice type",
                    ["Female", "Male", "Neutral"]
                )
                
                voice_speed = st.slider("Voice speed", 0.5, 2.0, 1.0)
                
                voice_detail = st.select_slider(
                    "Instruction detail",
                    options=["Minimal", "Standard", "Detailed"],
                    value="Standard"
                )
            
            st.markdown("##### Map Display")
            
            map_type = st.selectbox(
                "Map type",
                ["Standard", "Satellite", "Terrain", "High Contrast"]
            )
            
            auto_zoom = st.checkbox("Auto-zoom", value=True)
            north_up = st.checkbox("North up orientation", value=False)
            show_landmarks = st.checkbox("Show landmarks", value=True)
        
        if st.button("💾 Save Navigation Settings", use_container_width=True, type="primary"):
            st.success("✅ Navigation settings saved!")
    
    with tab4:
        st.markdown("#### Profile Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### Personal Information")
            
            name = st.text_input("Name", value="John Doe")
            email = st.text_input("Email", value="john.doe@email.com")
            phone = st.text_input("Phone", value="+1 555-0123")
            birth_date = st.date_input("Date of Birth")
            
            st.markdown("##### Address")
            
            address = st.text_input("Home Address", value="123 Main St")
            city = st.text_input("City", value="New York")
            zipcode = st.text_input("ZIP Code", value="10001")
        
        with col2:
            st.markdown("##### Medical Information")
            
            blood_type = st.selectbox("Blood Type", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
            
            allergies = st.text_area("Allergies", value="Penicillin, Peanuts")
            medications = st.text_area("Current Medications", value="Insulin, Aspirin")
            conditions = st.text_area("Medical Conditions", value="Diabetes Type 2")
            
            st.markdown("##### Emergency Contact")
            
            emergency_name = st.text_input("Contact Name", value="Jane Doe")
            emergency_phone = st.text_input("Contact Phone", value="+1 555-0124")
            emergency_relation = st.text_input("Relationship", value="Spouse")
        
        if st.button("💾 Update Profile", use_container_width=True, type="primary"):
            st.success("✅ Profile updated successfully!")
    
    with tab5:
        st.markdown("#### Privacy & Security")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### Data Sharing")
            
            share_location = st.checkbox("Share location for better recommendations", value=True)
            anonymous_data = st.checkbox("Share anonymous usage data", value=True)
            community_sharing = st.checkbox("Share reports with community", value=True)
            
            st.markdown("##### Location Privacy")
            
            location_precision = st.select_slider(
                "Location precision",
                options=["Exact", "Approximate", "City only"],
                value="Approximate"
            )
            
            location_history = st.checkbox("Save location history", value=True)
            
            if location_history:
                history_duration = st.selectbox(
                    "Keep history for",
                    ["1 week", "1 month", "3 months", "1 year", "Forever"]
                )
        
        with col2:
            st.markdown("##### Security")
            
            two_factor = st.checkbox("Two-factor authentication", value=False)
            biometric = st.checkbox("Biometric login", value=True)
            auto_lock = st.checkbox("Auto-lock app", value=True)
            
            if auto_lock:
                lock_time = st.selectbox(
                    "Lock after",
                    ["Immediately", "1 minute", "5 minutes", "15 minutes"]
                )
            
            st.markdown("##### Data Management")
            
            if st.button("📥 Download My Data", use_container_width=True):
                st.info("Preparing data download...")
            
            if st.button("🗑️ Delete My Data", use_container_width=True):
                st.warning("Are you sure? This action cannot be undone.")
        
        if st.button("💾 Save Privacy Settings", use_container_width=True, type="primary"):
            st.success("✅ Privacy settings saved!")
    
    # Footer
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**App Version:** 2.1.0")
        st.markdown("**Last Updated:** Jan 15, 2024")
    
    with col2:
        if st.button("📖 Help & Support", use_container_width=True):
            st.info("Opening help center...")
        if st.button("💬 Send Feedback", use_container_width=True):
            st.info("Opening feedback form...")
    
    with col3:
        if st.button("📜 Terms of Service", use_container_width=True):
            st.info("Opening terms...")
        if st.button("🔒 Privacy Policy", use_container_width=True):
            st.info("Opening privacy policy...")

if __name__ == "__main__":
    main()
