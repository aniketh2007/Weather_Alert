import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

API_KEY = os.environ.get("OWM_API_KEY")
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = your_account_sid
auth_token = os.environ.get("AUTH_TOKEN")
MY_NUMBER = YOUR_PHONE_NUMBER
MY_LAT = 12.9762
MY_LONG = 77.6033

params = {
    "lat" : 12.9762,
    "lon" : 77.6033,
    "appid" : API_KEY,
    "cnt" : 4
}
response = requests.get(OWM_endpoint,params=params)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_codes = hour_data["weather"][0]["id"]
    if int(condition_codes) <= 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid,auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="Carry an Umbrella 😔.As it is going to rain today ☔. Have a good day",
        from_=MY_NUMBER,
        to=SENDER_PHONE_NUMBER,
    )
    print(message.status)
else:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token,http_client=proxy_client)
    message = client.messages.create(
        body="Yaya!! Its not Raining. the sun is out ☀️."
             "You have a good sunny day 😄. Remember apply sunscreen ",
        from_=MY_NUMBER,
        to=SENDER_PHONE_NUMBER,
    )
    print(message.status)
