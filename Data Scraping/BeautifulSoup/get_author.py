import requests
from bs4 import BeautifulSoup as bs

res = requests.get("https://quotes.toscrape.com/")
if res.status_code == 200:
    soup = bs(res.text, "html.parser")
    for a in soup.find_all("small", {"class": "author"}):
        print(a.text)
