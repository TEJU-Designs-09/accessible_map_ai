import requests

BASE_URL = "https://accessible-map-ai-backend.onrender.com"

def get_route(start, end, profile, stairs, audio, crowds):

    payload = {
        "start": start,
        "end": end,
        "profile": profile,
        "avoid_stairs": stairs,
        "need_audio": audio,
        "avoid_crowds": crowds
    }

    try:
        res = requests.post(f"{BASE_URL}/route", json=payload)

        if res.status_code == 200:
            return res.json()

    except:
        return None