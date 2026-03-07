"""Community Reports page - Report and view accessibility issues"""

import streamlit as st
from datetime import datetime
from utils import get_mock_reports

st.set_page_config(page_title="Community Reports - Accessible Map AI", layout="wide")

def main():
    st.title("👥 Community Reports")
    st.markdown("### Help improve accessibility by reporting obstacles and improvements")
    
    # Stats Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Active Reports", "47", "+5", help="Reports submitted today")
    
    with col2:
        st.metric("Resolved", "132", "+12", help="Issues resolved this week")
    
    with col3:
        st.metric("Your Reports", "8", "+2", help="Your contribution")
    
    with col4:
        st.metric("Community Points", "234", "+15", help="Points earned from reporting")
    
    st.markdown("---")
    
    # Main Content
    tab1, tab2, tab3 = st.tabs(["📝 Submit Report", "📋 View Reports", "🏆 Leaderboard"])
    
    with tab1:
        st.markdown("#### Submit New Report")
        
        col1, col2 = st.columns(2)
        
        with col1:
            report_type = st.selectbox(
                "Report Type",
                ["Obstacle", "Hazard", "Improvement", "Suggestion", "Compliment"]
            )
            
            location = st.text_input("📍 Location", placeholder="Address or landmark")
            use_current = st.checkbox("Use current location")
            
            severity = st.select_slider(
                "Severity/Priority",
                options=["Low", "Medium", "High", "Critical"],
                value="Medium"
            )
            
            category = st.multiselect(
                "Affected Users",
                ["Wheelchair Users", "Vision Impaired", "Hearing Impaired", "Elderly", "General"]
            )
        
        with col2:
            description = st.text_area(
                "Description",
                placeholder="Describe the issue in detail...",
                height=150
            )
            
            photo = st.file_uploader("Upload Photo (optional)", type=['jpg', 'png', 'jpeg'])
            
            if photo:
                st.image(photo, caption="Uploaded image", use_column_width=True)
        
        st.markdown("#### Additional Information")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            temporary = st.checkbox("Temporary issue")
            if temporary:
                end_date = st.date_input("Expected end date")
        
        with col2:
            recurring = st.checkbox("Recurring issue")
            if recurring:
                pattern = st.selectbox("Pattern", ["Daily", "Weekdays", "Weekends", "Random"])
        
        with col3:
            anonymous = st.checkbox("Submit anonymously")
            notify = st.checkbox("Notify me of updates", value=True)
        
        if st.button("📤 Submit Report", type="primary", use_container_width=True):
            st.success("✅ Report submitted successfully! Thank you for improving accessibility.")
            st.balloons()
            st.info("You earned +10 community points!")
    
    with tab2:
        st.markdown("#### Community Reports Feed")
        
        # Filters
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            filter_type = st.selectbox("Type", ["All", "Obstacle", "Hazard", "Improvement"])
        
        with col2:
            filter_status = st.selectbox("Status", ["All", "New", "In Progress", "Resolved"])
        
        with col3:
            filter_time = st.selectbox("Time", ["Today", "This Week", "This Month", "All Time"])
        
        with col4:
            sort_by = st.selectbox("Sort by", ["Newest", "Most Votes", "Severity", "Nearest"])
        
        # Reports Feed
        reports = get_mock_reports()
        
        for report in reports[:5]:
            with st.container():
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    # Report type icon
                    type_icons = {
                        "Obstacle": "🚧",
                        "Hazard": "⚠️",
                        "Improvement": "✅",
                        "Feedback": "💬"
                    }
                    
                    icon = type_icons.get(report['type'], "📍")
                    st.markdown(f"### {icon} {report['location']}")
                    st.write(report['description'])
                    st.caption(f"Reported {report['timestamp']}")
                
                with col2:
                    # Status badge
                    status_colors = {
                        "New": "🔴",
                        "In Progress": "🟡",
                        "Resolved": "🟢"
                    }
                    
                    st.markdown(f"**Status:** {status_colors.get(report['status'], '')} {report['status']}")
                    st.metric("Votes", report['votes'])
                
                with col3:
                    if st.button("👍 Upvote", key=f"vote_{report['id']}"):
                        st.success("Voted!")
                    
                    if st.button("💬 Comment", key=f"comment_{report['id']}"):
                        st.info("Comment added")
                    
                    if report['status'] != "Resolved":
                        if st.button("✅ Verify", key=f"verify_{report['id']}"):
                            st.success("Verified!")
                
                st.markdown("---")
    
    with tab3:
        st.markdown("#### 🏆 Top Contributors")
        
        # Leaderboard
        contributors = [
            {"rank": 1, "name": "AccessHero", "points": 1250, "reports": 89, "badge": "🥇"},
            {"rank": 2, "name": "CommunityFirst", "points": 980, "reports": 67, "badge": "🥈"},
            {"rank": 3, "name": "PathFinder", "points": 875, "reports": 58, "badge": "🥉"},
            {"rank": 4, "name": "You", "points": 234, "reports": 8, "badge": "⭐"},
            {"rank": 5, "name": "Helper2024", "points": 210, "reports": 15, "badge": ""},
        ]
        
        for contributor in contributors:
            col1, col2, col3, col4 = st.columns([1, 2, 1, 1])
            
            with col1:
                st.markdown(f"### {contributor['badge']} #{contributor['rank']}")
            
            with col2:
                st.markdown(f"**{contributor['name']}**")
            
            with col3:
                st.metric("Points", contributor['points'])
            
            with col4:
                st.metric("Reports", contributor['reports'])
        
        st.markdown("---")
        
        # Achievements
        st.markdown("#### 🎖️ Your Achievements")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style='text-align: center; padding: 1rem; background: #FFE4B5; border-radius: 8px;'>
                <h1>🌟</h1>
                <b>First Reporter</b><br>
                <small>Submit your first report</small>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='text-align: center; padding: 1rem; background: #F0F8FF; border-radius: 8px;'>
                <h1>🎯</h1>
                <b>Sharp Eye</b><br>
                <small>10 verified reports</small>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style='text-align: center; padding: 1rem; background: #E6E6FA; border-radius: 8px;'>
                <h1>🏅</h1>
                <b>Community Champion</b><br>
                <small>100+ points earned</small>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
