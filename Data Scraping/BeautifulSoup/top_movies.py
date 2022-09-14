from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(res.text, "html.parser")
tag = soup.find_all("td", {"class": "titleColumn"})
for t in tag:
    print(t.find("a").string, t.find("span").string)
