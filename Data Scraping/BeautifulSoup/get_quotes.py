from bs4 import BeautifulSoup
import requests

res = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(res.text, "html.parser")
for tag in soup.findAll("span", {'class': 'text'}):
    print(tag.text.strip())
