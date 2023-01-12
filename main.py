import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

api_key = "947655688b1b2a4671fd876b28e2d452"
account_sid = "ACcf4ac1aacd9aa16536ea9cd5153751f3"
auth_token = "4514cb5a9b5cc19b946cc3ea99d15e69"

weather_params = {
    "lat": 38.907192,
    "lon": - 77.036873,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    #for pythonanywhere implemenation
    #proxy_client = TwilioHttpClient()
    #proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Your message here"
        from_="",
        to=""

    )
    print(message.status)