import requests
import os
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWN_API_KEY") # 1af388b7XXXXXXXXXXX8ac627fc
account_sid = os.environ.get("twilo_account_sid") # AC3f28c8XXXXXXXXXXe09d19781bc10
auth_token = os.environ.get("TWILO_AUTH_TOKEN") # 854242cXXXXXXXXXXX9faf0b99

weather_params = {
    "lat": 34.01,
    "lon": 158.07,
    "appid": api_key,
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an ☔️",
        from_="+16107703071",
        to="+972526839273"
    )
    print(message.status)