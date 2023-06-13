import requests

APP_ID = "a37fbeeb"
API_KEY = "728a5146763a516a57a769adfd5d8cc5"
BASE_URL = "https://trackapi.nutritionix.com/"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

exercise_data = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 90,
    "height_cm": 1.72,
    "age": 35
}

response = requests.post(url=f"{BASE_URL}v2/natural/exercise", json=exercise_data, headers=HEADERS)
response.raise_for_status()
data = response.json()

print(data)