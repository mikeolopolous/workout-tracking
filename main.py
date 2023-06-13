import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""
BASE_URL = "https://trackapi.nutritionix.com/"

SHEETY_URL = "https://api.sheety.co/fe3dcca35ca1d03f184574cef51bbcd6/workoutTracking/workouts"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

TOKEN = {
    "Authorization": ""
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

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in data["exercises"]:
    body = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response_sheety = requests.post(url=SHEETY_URL, json=body, headers=TOKEN)
    response_sheety.raise_for_status()

print(response_sheety)
