"""Route Planner page - Plan accessible routes"""

import streamlit as st
import folium
from streamlit_folium import st_folium
from components import render_route_card

from services.api import get_route
from utils import get_mock_routes, generate_mock_coordinates
from gtts import gTTS
import base64
import os

def speak(text):
    tts = gTTS(text)
    tts.save("voice.mp3")

    audio_file = open("voice.mp3", "rb")
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format="audio/mp3")
    
    
st.set_page_config(page_title="Route Planner - Accessible Map AI", layout="wide")

# ---------- SESSION STATE ----------
if "routes" not in st.session_state:
    st.session_state.routes = None

# ---------- STYLES ----------
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
    st.title("🗺️ Route Planner")
    st.markdown("### Find the most accessible route for your journey")
    st.caption("Routes are optimized based on accessibility, safety, and user preferences")

    # ---------- INPUT SECTION ----------
    st.markdown("#### 📍 Trip Details")

    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        start_location = st.text_input(
            "Starting Point",
            placeholder="Enter address or use current location"
        )
        use_current = st.checkbox("Use current location")

    with col2:
        destination = st.text_input(
            "Destination",
            placeholder="Enter destination address"
        )

    with col3:
        st.markdown("**Profile**")
        profile = st.selectbox(
            "Accessibility Profile",
            ["Standard", "Wheelchair", "Vision Impaired", "Elderly", "Hearing Impaired"]
        )

    # ---------- ADVANCED OPTIONS ----------
    with st.expander("⚙️ Accessibility Preferences"):
        col1, col2, col3 = st.columns(3)

        with col1:
            avoid_stairs = st.checkbox(
                "Avoid stairs",
                value=True if profile == "Wheelchair" else False
            )
            need_audio = st.checkbox(
                "Audio signals required",
                value=True if profile == "Vision Impaired" else False
            )

        with col2:
            max_distance = st.slider("Max walking distance (km)", 0.5, 5.0, 2.0)
            rest_stops = st.checkbox(
                "Include rest stops",
                value=True if profile == "Elderly" else False
            )

        with col3:
            time_of_day = st.time_input("Departure time")
            avoid_crowds = st.checkbox("Avoid crowded areas")

    # ---------- SEARCH ----------
    if st.button("🔍 Find Routes", type="primary", use_container_width=True):

        if not destination:
            st.warning("Please enter destination")
            return

        with st.spinner("Calculating accessible routes..."):

            data = get_route(
                start_location or "Current Location",
                destination,
                profile,
                avoid_stairs,
                need_audio,
                avoid_crowds
            )
                

            # ✅ BACKEND SUCCESS
            if data:
                st.session_state.routes = [{
                    "name": "AI Optimized Route",
                    "accessibility_score": data["accessibility_score"],
                    "duration": round(data["distance"] * 4),
                    "distance": data["distance"],
                    "alerts": ["AI optimized"],
                    "features": [
                        "Safe route",
                        "Accessible path",
                        "Low traffic",
                        "Profile optimized"
                    ]
                }]
                st.success("Live AI route loaded 🚀")

            # ✅ FALLBACK
            else:
                st.session_state.routes = get_mock_routes(
                    start_location or "Current Location",
                    destination,
                    profile
                )
                st.info("Using demo data (backend not connected)")

    # ---------- SHOW ROUTES ----------
    if st.session_state.routes:

        st.markdown("---")
        st.markdown("### 📋 Available Routes")
        st.caption("Routes ranked by accessibility and safety")

        for route in st.session_state.routes:
            render_route_card(
                route_name=route['name'],
                accessibility_score=route['accessibility_score'],
                duration=f"{route['duration']} min",
                distance=f"{route['distance']} km",
                alerts=route.get('alerts', []),
                features=route.get('features', [])
            )

        # ---------- SMART ALERTS ----------
        st.markdown("### ⚠️ Smart Alerts")

        st.warning("🚧 Construction ahead (500m)")
        st.info("👥 Crowded area detected")
        st.error("⚠️ Accident-prone zone nearby")
        
        # ---------- LIVE AI SCORE ----------
        import random

        st.markdown("### 🤖 Live AI Safety Score")

        score = random.randint(82, 97)

        st.progress(score/100)
        st.metric("Current Safety Score", f"{score}%")
        
        # ---------- VOICE NAVIGATION ----------
        import time

        st.markdown("### 🔊 Voice Navigation")

        if st.button("Start Voice Guidance"):

            steps = [
                "Head straight for 200 meters",
                "Turn right ahead",
                "Continue on accessible sidewalk",
                "Destination is on your left"
            ]

            for step in steps:
                st.success(step)
                speak(step) #REAL VOICE
                time.sleep(1)
        
        # ---------- LIVE TRACKING ----------
        st.markdown("### 📍 Live Route Tracking")

        if st.button("Start Tracking"):

            progress_bar = st.progress(0)

            for i in range(100):
                time.sleep(0.02)
                progress_bar.progress(i + 1)

            st.success("You reached destination 🎉")
            
            
        # ---------- ROUTE PROGRESS ----------
        st.markdown("### 🚶 Route Progress")

        st.metric("Distance Covered", "1.8 km")
        st.metric("Remaining", "2.9 km")
        st.metric("ETA", "12 mins")

        # ---------- MAP ----------
        st.markdown("---")
        st.markdown("### 🗺️ Route Map")

        if st.session_state.routes:

            coords = st.session_state.routes[0].get("coords")

            if coords:

                m = folium.Map(location=coords[0], zoom_start=14)

                # route line
                folium.PolyLine(coords, color="blue", weight=5).add_to(m)

                # start/end markers
                folium.Marker(coords[0], tooltip="Start").add_to(m)
                folium.Marker(coords[-1], tooltip="End").add_to(m)

                # 🔥 CROWD HEATMAP (mock)
                from folium.plugins import HeatMap
                heat_data = [
                    [coords[0][0]+0.002, coords[0][1]+0.002],
                    [coords[0][0]+0.004, coords[0][1]-0.002],
                    [coords[0][0]-0.003, coords[0][1]+0.003],
                ]
                HeatMap(heat_data).add_to(m)

                st_folium(m, height=450)
                
        # ---------- WHY THIS ROUTE ----------
        st.markdown("### 🤖 Why This Route?")

        st.success("✔ Avoids stairs and steep slopes")
        st.success("✔ Safer lighting conditions")
        st.success("✔ Lower accident probability")
        st.success("✔ Optimized for accessibility profile")

        # ---------- DEMO MODE ----------
    st.markdown("### 🎬 Demo Mode")

    if st.button("Start Full Demo"):

        speak("Starting accessible navigation demo")

        st.info("Calculating safest route...")
        time.sleep(1)

        st.warning("Crowded area ahead")
        speak("Crowded area ahead")

        time.sleep(1)

        st.error("Accident-prone zone nearby")
        speak("Accident-prone zone nearby")

        time.sleep(1)

        st.success("Re-routing to safer path")
        speak("Re-routing to safer path")

        time.sleep(1)

        st.success("Destination reached")
        speak("Destination reached")

    # ---------- SAVED ROUTES ----------
    st.markdown("---")
    st.markdown("### 💾 Saved Routes")

    tab1, tab2 = st.tabs(["Favorites", "Recent"])

    with tab1:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.info("🏠 Home to Office - 95% Accessible")
        with col2:
            st.button("Load", key="load_home_office")

        col1, col2 = st.columns([3, 1])
        with col1:
            st.info("🏥 Medical Center Route - 98% Accessible")
        with col2:
            st.button("Load", key="load_medical")

    with tab2:
        st.info("📍 Museum District → Central Park - Used 2 hours ago")
        st.info("📍 Library → Shopping Mall - Used yesterday")


# ---------- DEMO CONTROL PANEL ----------
st.markdown("### 🎛 Demo Control Panel")

col1, col2, col3 = st.columns(3)

with col1:
    demo_mode = st.toggle("Demo Mode")

with col2:
    night_mode = st.toggle("Night Simulation")

with col3:
    accessibility_focus = st.toggle("Accessibility Priority")
    
# ---------- SMART STATS ----------
st.markdown("### 📊 Smart Route Insights")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Accessibility Score", "94%")
col2.metric("Risk Level", "Low")
col3.metric("Crowd Density", "Moderate")
col4.metric("Lighting Quality", "Good")    
    
# ---------- FINAL SCREEN ----------
st.markdown("---")
st.markdown("### 🏁 Accessible Map AI")

st.info("""
Accessible Map AI combines real-time routing, accessibility intelligence,
AI safety scoring, crowd detection, and inclusive navigation
into one unified smart mobility platform.
""")    
    

if __name__ == "__main__":
    main()
