"""Emergency page - Emergency assistance and SOS features"""

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Emergency - Accessible Map AI", layout="wide")

def main():
    st.title("🆘 Emergency Assistance")
    st.markdown("### Quick access to emergency services and assistance")
    
    # Emergency Status Bar
    status_container = st.container()
    with status_container:
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            st.markdown("**Status:** 🟢 All Clear")
        
        with col2:
            st.markdown("**📍 Location:** 123 Main Street (GPS Active)")
        
        with col3:
            st.markdown("**🔋 Battery:** 78%")
    
    st.markdown("---")
    
    # Big Emergency Button
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, #FF6B6B, #FF4444); border-radius: 20px; color: white;'>
            <h1 style='font-size: 60px;'>🆘</h1>
            <h2>SOS EMERGENCY</h2>
            <p>Press and hold for 3 seconds</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚨 ACTIVATE SOS", use_container_width=True, type="primary"):
            st.error("⚠️ SOS ACTIVATED - Contacting emergency services...")
            st.warning("📍 Location shared with emergency contacts")
            st.info("🔊 Loud alarm activated")
    
    st.markdown("---")
    
    # Quick Actions
    st.markdown("### ⚡ Quick Emergency Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📞 Call 911", use_container_width=True):
            st.info("Calling 911...")
    
    with col2:
        if st.button("🏥 Nearest Hospital", use_container_width=True):
            st.info("City Medical Center - 0.8 km")
    
    with col3:
        if st.button("👮 Police", use_container_width=True):
            st.info("Contacting police...")
    
    with col4:
        if st.button("🚑 Ambulance", use_container_width=True):
            st.info("Requesting ambulance...")
    
    st.markdown("---")
    
    # Detailed Emergency Options
    tab1, tab2, tab3, tab4 = st.tabs(["🏥 Medical", "🛡️ Safety", "📞 Contacts", "📍 Share Location"])
    
    with tab1:
        st.markdown("#### Medical Emergency")
        
        col1, col2 = st.columns(2)
        
        with col1:
            medical_type = st.selectbox(
                "Type of Medical Emergency",
                ["Injury", "Illness", "Allergic Reaction", "Heart Issue", "Breathing Problem", "Other"]
            )
            
            severity = st.select_slider(
                "Severity",
                options=["Mild", "Moderate", "Severe", "Critical"],
                value="Moderate"
            )
            
            symptoms = st.multiselect(
                "Symptoms",
                ["Pain", "Bleeding", "Dizziness", "Nausea", "Difficulty Breathing", "Confusion", "Unconscious"]
            )
        
        with col2:
            st.markdown("##### Medical Information")
            
            with st.expander("Your Medical Profile"):
                st.info("**Blood Type:** O+")
                st.info("**Allergies:** Penicillin, Peanuts")
                st.info("**Medications:** Insulin, Aspirin")
                st.info("**Conditions:** Diabetes Type 2")
                st.info("**Emergency Contact:** Jane Doe (555-0123)")
        
        if st.button("🚑 Request Medical Help", use_container_width=True, type="primary"):
            st.error("Medical help requested! ETA: 6 minutes")
    
    with tab2:
        st.markdown("#### Safety Emergency")
        
        col1, col2 = st.columns(2)
        
        with col1:
            threat_type = st.selectbox(
                "Type of Threat",
                ["Feeling Unsafe", "Being Followed", "Robbery", "Assault", "Lost", "Other"]
            )
            
            safe_places = st.checkbox("Show nearby safe places")
            
            if safe_places:
                st.success("✅ **Police Station** - 0.3 km (3 min walk)")
                st.success("✅ **24/7 Store** - 0.1 km (1 min walk)")
                st.success("✅ **Hospital** - 0.8 km (8 min walk)")
        
        with col2:
            st.markdown("##### Safety Features")
            
            siren = st.checkbox("Activate loud siren")
            flash = st.checkbox("Activate flashlight strobe")
            record = st.checkbox("Record audio/video")
            fake_call = st.checkbox("Fake call feature")
            
            if fake_call:
                if st.button("📞 Start Fake Call"):
                    st.info("Incoming call from 'Mom'...")
    
    with tab3:
        st.markdown("#### Emergency Contacts")
        
        # Primary Contacts
        st.markdown("##### Primary Contacts")
        
        contacts = [
            {"name": "Jane Doe (Wife)", "phone": "555-0123", "relationship": "Spouse"},
            {"name": "John Smith (Son)", "phone": "555-0124", "relationship": "Family"},
            {"name": "Dr. Brown", "phone": "555-0125", "relationship": "Doctor"}
        ]
        
        for contact in contacts:
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.markdown(f"**{contact['name']}**")
                st.caption(contact['relationship'])
            
            with col2:
                if st.button("📞 Call", key=f"call_{contact['name']}"):
                    st.info(f"Calling {contact['name']}...")
            
            with col3:
                if st.button("💬 Text", key=f"text_{contact['name']}"):
                    st.info("Opening messages...")
        
        # Emergency Services
        st.markdown("##### Emergency Services")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("**🚨 Emergency:** 911")
            st.info("**🏥 Hospital:** 555-HELP")
            st.info("**☠️ Poison Control:** 1-800-222-1222")
        
        with col2:
            st.info("**🔥 Fire Dept:** 555-FIRE")
            st.info("**👮 Police (Non-emergency):** 555-COPS")
            st.info("**🚗 Roadside Assistance:** 555-ROAD")
    
    with tab4:
        st.markdown("#### Share Location")
        
        # Current Location
        st.markdown("##### 📍 Current Location")
        st.info("**Address:** 123 Main Street, Downtown District")
        st.info("**Coordinates:** 40.7128° N, 74.0060° W")
        st.info("**Accuracy:** ±5 meters")
        
        # Share Options
        st.markdown("##### Share With")
        
        col1, col2 = st.columns(2)
        
        with col1:
            share_contacts = st.multiselect(
                "Select Contacts",
                ["Jane Doe", "John Smith", "Dr. Brown", "Emergency Services"]
            )
            
            share_duration = st.selectbox(
                "Share Duration",
                ["15 minutes", "30 minutes", "1 hour", "Until turned off"]
            )
        
        with col2:
            include_medical = st.checkbox("Include medical info", value=True)
            include_route = st.checkbox("Include planned route")
            continuous_update = st.checkbox("Continuous location updates", value=True)
        
        if st.button("📤 Share Location", use_container_width=True, type="primary"):
            st.success(f"✅ Location shared with {len(share_contacts)} contacts")
            st.info("Location sharing active - Updates every 30 seconds")
    
    # Emergency History
    st.markdown("---")
    st.markdown("### 📜 Emergency History")
    
    with st.expander("View Recent Emergency Events"):
        st.info("📅 Jan 10, 2024 - 2:30 PM - SOS Activated (False alarm)")
        st.info("📅 Dec 28, 2023 - 6:45 PM - Location shared (Returned safely)")
        st.info("📅 Dec 15, 2023 - 11:00 AM - Medical assistance requested")
    
    # Settings
    st.markdown("---")
    st.markdown("### ⚙️ Emergency Settings")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        auto_share = st.checkbox("Auto-share location in emergency", value=True)
        auto_call = st.checkbox("Auto-call 911 after SOS countdown", value=False)
    
    with col2:
        countdown_time = st.slider("SOS countdown (seconds)", 3, 10, 5)
        false_alarm = st.checkbox("Allow false alarm cancellation", value=True)
    
    with col3:
        test_mode = st.checkbox("Test mode (no real calls)", value=False)
        if st.button("🧪 Test Emergency Features"):
            st.info("Testing emergency features... All systems operational!")

if __name__ == "__main__":
    main()
