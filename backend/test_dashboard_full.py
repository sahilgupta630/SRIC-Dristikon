
import requests
import json

BASE_URL = "http://localhost:8000/api/v1/dashboard"

endpoints = [
    "executive",
    "financial",
    "portfolio",
    "hr",
    "pipeline",
    "kpi"
]

print("--- Testing Dashboard APIs ---")
for ep in endpoints:
    try:
        url = f"{BASE_URL}/{ep}"
        resp = requests.get(url)
        print(f"GET /{ep}: {resp.status_code}")
        if resp.status_code == 200:
            print(json.dumps(resp.json(), indent=2))
        else:
            print(resp.text)
    except Exception as e:
        print(f"Error calling {ep}: {e}")
