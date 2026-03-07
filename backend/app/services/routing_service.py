import osmnx as ox
import networkx as nx
from geopy.geocoders import Nominatim
import json
from geopy.distance import geodesic

with open("app/data/safety_zones.json") as f:
    SAFETY_ZONES = json.load(f)

geolocator = Nominatim(user_agent="accessible_map_ai")

def safety_penalty(lat, lon):

    penalty = 0

    for zone in SAFETY_ZONES:
        d = geodesic((lat, lon), (zone["lat"], zone["lon"])).meters

        if d < 300:
            penalty += zone["risk"]

    return penalty

def accessibility_weight(u, v, data, user):

    weight = data.get("length", 1)

    lat = data.get("y", 0)
    lon = data.get("x", 0)

    # stairs
    if user.avoid_stairs and data.get("highway") == "steps":
        weight *= 10

    # rough road
    if data.get("surface") in ["gravel", "dirt"]:
        weight *= 2

    # crowd approx
    if user.avoid_crowds and data.get("highway") in ["primary", "secondary"]:
        weight *= 1.5

    # safety penalty
    weight += safety_penalty(lat, lon)

    return weight


def calculate_route(user):

    start_loc = geolocator.geocode(user.start)
    end_loc = geolocator.geocode(user.end)

    if not start_loc or not end_loc:
        return None

    start = (start_loc.latitude, start_loc.longitude)
    end = (end_loc.latitude, end_loc.longitude)

    G = ox.graph_from_point(start, dist=5000, network_type="walk")

    start_node = ox.distance.nearest_nodes(G, start[1], start[0])
    end_node = ox.distance.nearest_nodes(G, end[1], end[0])

    route = nx.shortest_path(
        G,
        start_node,
        end_node,
        weight=lambda u, v, d: accessibility_weight(u, v, d, user)
    )

    coords = [(G.nodes[n]["y"], G.nodes[n]["x"]) for n in route]

    distance = nx.shortest_path_length(G, start_node, end_node, weight="length") / 1000

    score = 90 - int(distance)

    if user.avoid_stairs:
        score += 2

    score -= len(SAFETY_ZONES)

    return {
        "distance": round(distance, 2),
        "safety_score": score,
        "accessibility_score": score,
        "route_coords": coords
    }