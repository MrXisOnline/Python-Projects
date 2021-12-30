import requests
from twilio.rest import Client

twi_sid = "ACe394e0afce8239da1b4ce0d5b7afd9da"
twi_auth = "d07795ecbe122c70521b97115fe22c6f"
news_url = "http://newsapi.org/v2/everything"
alpha_url = "https://www.alphavantage.co/query"
alpha_key = "6WI6Q3Q7BLN3BDTI"
news_key = "e60633ec11344b18b1be019f8a202e6b"
alpha_para = {
	"function":"TIME_SERIES_DAILY",
	"symbol":"TSLA",
	"outputsize":"compact",
	"apikey":alpha_key
}
date = ""
response = requests.get(alpha_url,params=alpha_para)
data = response.json()["Time Series (Daily)"]
days = []
# key = data.keys()
i=0
for k in data.keys():
	date = k
	days.append(float(data[k]["4. close"]))
	i += 1
	if i == 2:
		break

news_para = {
	"q":"TSLA",
	"from":date,
	"sortBy":"popularity",
	"language":"en",
	"apiKey":news_key
}

def get_news():
	response = requests.get(news_url,params=news_para)
	news_all = []
	j=0
	for i in range(3):
		news_all.append({
			"title":response.json()["articles"][i]["title"],
			"news":response.json()["articles"][0]["description"]
			})
	return news_all

def send_messages(per,all_news):
	client = Client(twi_sid,twi_auth)
	message_sids = []
	for n in all_news:
		s = f"stock at {per}\n{n['title']}\n{n['news']}"
		msg = client.messages.create(
			body=s,
			from_="+15304773447",
			to="+919871178255"
			)
		message_sids.append(msg)
	print(message_sids)

diff = round(days[0] - days[1],2)
diff_percent = (diff/days[0])*100
if diff_percent > 5:
	send_messages(f"▲{diff_percent}%",get_news())
elif diff_percent < -5:
	send_messages(f"▼{diff_percent}%",get_news())
else:
	print("Market STABLE")

