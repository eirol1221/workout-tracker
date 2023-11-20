import requests
import os
from datetime import *

NUTRI_APP_ID = os.environ["NUTRI_APP_ID"]
NUTRI_API_KEY = os.environ["NUTRI_API_KEY"]
SHEETY_URL = os.environ["SHEETY_ENDPOINT"]
TOKEN = os.environ["TOKEN"]

date_now = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%H:%M:%S")


nutri_headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
    "Content-Type": "application/json",
}

nutri_query = {
    "query": input("Tell me which exercises you did: ")
}

nutri_response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                               headers=nutri_headers, json=nutri_query)
print(nutri_response.json())
exercise_details = nutri_response.json()['exercises']

exercise_list = {}

for item in exercise_details:
    sheety_header = {
        "Content-Type": "application/json",
        "Authorization": TOKEN,
    }
    sheety_body = {
        "workout": {
            "date": date_now,
            "time": time_now,
            "exercise": item['user_input'].title(),
            "duration": item['duration_min'],
            "calories": item['nf_calories']
        }
    }

    sheety_response = requests.post(url=SHEETY_URL, json=sheety_body, headers=sheety_header)
    print(sheety_response.text)