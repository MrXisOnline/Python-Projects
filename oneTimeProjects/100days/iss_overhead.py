import requests
from datetime import datetime
import time
while True:
	MY_LAT = 28.613939 # Your latitude
	MY_LONG = 77.209023 # Your longitude

	response = requests.get(url="http://api.open-notify.org/iss-now.json")
	response.raise_for_status()
	data = response.json()

	iss_latitude = float(data["iss_position"]["latitude"])
	iss_longitude = float(data["iss_position"]["longitude"])

	#Your position is within +5 or -5 degrees of the ISS position.


	parameters = {
	    "lat": MY_LAT,
	    "lng": MY_LONG,
	    "formatted": 0,
	}

	response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
	response.raise_for_status()
	data = response.json()
	sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
	sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

	time_now = datetime.now()

	if (MY_LAT -5 < iss_latitude < MY_LAT +5) and (MY_LONG -5 < iss_longitude < MY_LONG +5):
		if time_now.hour > sunset:
			print("Look up")
		else:
			print("currently at your position but it is day")
	else:
		print("No Luck")
	print("again check after 100 seconds")
	time.sleep(100)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
