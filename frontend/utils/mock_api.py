"""Mock API functions for simulating backend responses"""

import random
from datetime import datetime, timedelta

def get_mock_routes(start, destination, profile="Standard"):
    """
    Get mock route data
    
    Args:
        start: Starting location
        destination: Destination location
        profile: User accessibility profile
    
    Returns:
        List of route dictionaries
    """
    
    routes = []
    
    # Generate 3 mock routes
    route_types = ["Fastest", "Most Accessible", "Scenic"]
    
    for i, route_type in enumerate(route_types):
        base_score = random.randint(70, 95)
        
        # Adjust score based on profile
        if profile == "Wheelchair User" and route_type == "Most Accessible":
            base_score = min(100, base_score + 10)
        
        route = {
            "name": f"{route_type} Route",
            "accessibility_score": base_score,
            "duration": random.randint(15, 45),
            "distance": round(random.uniform(1.5, 5.0), 1),
            "features": generate_route_features(route_type),
            "alerts": generate_route_alerts() if random.random() > 0.5 else [],
            "waypoints": generate_waypoints()
        }
        routes.append(route)
    
    return routes

def generate_route_features(route_type):
    """Generate random accessibility features for a route"""
    all_features = [
        "♿ Wheelchair Accessible",
        "🔊 Audio Signals",
        "📝 Braille Signs",
        "🛗 Elevators Available",
        "🚪 Automatic Doors",
        "🛤️ Wide Pathways",
        "💡 Well Lit",
        "🪑 Rest Areas"
    ]
    
    if route_type == "Most Accessible":
        return random.sample(all_features, k=random.randint(5, 7))
    else:
        return random.sample(all_features, k=random.randint(2, 4))

def generate_route_alerts():
    """Generate random alerts for routes"""
    alerts = [
        "Construction on 3rd Street - Use caution",
        "Elevator maintenance at Station B",
        "Crowded area expected near Market Square",
        "Temporary pathway closure - Alternative available",
        "Steep incline ahead - Consider alternate route"
    ]
    
    return random.sample(alerts, k=random.randint(1, 2))

def generate_waypoints():
    """Generate mock waypoints for a route"""
    waypoints = []
    num_points = random.randint(3, 6)
    
    for i in range(num_points):
        waypoints.append({
            "lat": 40.7128 + random.uniform(-0.01, 0.01),
            "lon": -74.0060 + random.uniform(-0.01, 0.01),
            "description": f"Waypoint {i+1}"
        })
    
    return waypoints

def get_mock_reports():
    """Get mock community reports"""
    report_types = ["Obstacle", "Improvement", "Hazard", "Feedback"]
    locations = ["Main Street", "Central Station", "Park Avenue", "City Hall", "Shopping District"]
    
    reports = []
    for i in range(10):
        hours_ago = random.randint(1, 48)
        report = {
            "id": i + 1,
            "type": random.choice(report_types),
            "location": random.choice(locations),
            "description": generate_report_description(),
            "timestamp": (datetime.now() - timedelta(hours=hours_ago)).strftime("%Y-%m-%d %H:%M"),
            "status": random.choice(["New", "In Progress", "Resolved"]),
            "votes": random.randint(1, 50)
        }
        reports.append(report)
    
    return reports

def generate_report_description():
    """Generate random report descriptions"""
    descriptions = [
        "Broken wheelchair ramp needs repair",
        "New accessible pathway installed",
        "Elevator out of service",
        "Excellent accessibility features added",
        "Sidewalk obstruction blocking path",
        "Audio signals not working properly",
        "New braille signs installed",
        "Lighting improvement needed"
    ]
    return random.choice(descriptions)

def get_mock_parking():
    """Get mock parking data"""
    parking_spots = []
    locations = ["North Garage", "South Lot", "Central Plaza", "East Side Parking", "West End Garage"]
    
    for location in locations:
        spot = {
            "name": location,
            "accessible_spots": random.randint(2, 10),
            "available": random.randint(0, 5),
            "distance": round(random.uniform(0.1, 2.0), 1),
            "rate": f"${random.randint(2, 8)}/hour",
            "features": random.sample(
                ["Wide Spaces", "Level Access", "Covered", "24/7 Security", "EV Charging"],
                k=random.randint(2, 4)
            )
        }
        parking_spots.append(spot)
    
    return parking_spots

def get_mock_traffic():
    """Get mock traffic data"""
    traffic_data = {
        "congestion_level": random.choice(["Low", "Medium", "High"]),
        "average_speed": random.randint(15, 45),
        "incidents": random.randint(0, 5),
        "estimated_delay": random.randint(0, 20)
    }
    return traffic_data
