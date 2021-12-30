from bs4 import BeautifulSoup as soup
import requests
import lxml
from smtplib import SMTP

def send_mail():
	my_mail="hackingwithbhai@gmail.com"
	pass_ = input("Enter Pass : ")
	connect = SMTP("smtp.gmail.com", port=587)
	connect.starttls()
	connect.login(user=my_mail,password=pass_)
	message = f"Subject: About Amazon Product\n\n{url}\nIs at {price} And it is Dropped by {MIN_PRICE-price}\nSHOP NOW!!!"
	connect.sendmail(from_addr=my_mail,to_addrs="sg704992@gmail.com",msg=message)
	connect.close()


MIN_PRICE = 10000
header = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
	"Accept-Language": "en-US,en;q=0.5"
}
url = "https://www.amazon.in/Intel-Corporation-Generation-Processor-Graphics/dp/B07MRCGQQ4/ref=sr_1_2?dchild=1&keywords=i5+9gen&qid=1616167904&sr=8-2"
response = requests.get(url, headers=header)
html = soup(response.text, "lxml")
# print(html.prettify().encode("utf-8"))
# # print(html.unescape(html))
# # print(html.prettify())
tag = html.select_one("#priceblock_ourprice")
text = tag.getText()
with open("depen.txt", mode="w", encoding="utf-8") as file:
	file.write(text)
with open("depen.txt") as file:
	new_text = file.read()
price = int(new_text.split()[1].replace(",", '').split(".")[0])
print(price)
if price < MIN_PRICE:
	send_mail()