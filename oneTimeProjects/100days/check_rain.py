import requests
from twilio.rest import Client
from datetime import datetime as dt

def get_12hour_weather():
	url="https://api.openweathermap.org/data/2.5/onecall"
	parameters={
		"lat":23.181467,
		"lon":79.986404,
		"appid":"7b38b3852997dd1abcb02eb72d02aa11",
		"exclude":"current,minutely,daily,alerts"
	}

	response = requests.get(url,params=parameters)
	data = response.json()
	weather = []
	for i in range(12):
		weather.append(data["hourly"][i]["weather"][0]["id"])
	return weather

def send_sms():
	acc_sid = "ACe394e0afce8239da1b4ce0d5b7afd9da"
	auth_token = "d07795ecbe122c70521b97115fe22c6f"
	client = Client(acc_sid, auth_token)
	message = client.messages.create(
								body="Today might will Rain, Take an Umbrella",
								from_="+15304773447",
								to = "+919871178255"
									)
	print(message.sid)


flag=False
now = dt.now()
# if now.hour == 7:
weather_data = get_12hour_weather()
for i in weather_data:
	if i < 700:
		flag=True
if flag:
	send_sms()
