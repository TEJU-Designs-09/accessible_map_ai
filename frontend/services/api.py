import requests

BASE_URL = "http://127.0.0.1:8000"

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