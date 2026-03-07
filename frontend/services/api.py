import requests

BASE_URL = "https://accessible-map-ai-backend-fey0.onrender.com"

def get_route(start, end, profile=None, stairs=False, audio=False, crowds=False):

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
        else:
            print("API error:", res.status_code)

    except Exception as e:
        print("Connection error:", e)

    return None