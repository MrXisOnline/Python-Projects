from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests

url = "https://en.wikipedia.org/wiki/Stock_market"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
# print(page_html)
page_soup = soup(page_html, "html.parser")
container = page_soup.find_all("div", {"class": "mw-parser-output"})
contain = container[0]
print(contain.p)


