import requests as rq
from bs4 import BeautifulSoup as Soup
import os

res = rq.get("https://en.wikipedia.org/wiki/Stock_market")
soup = Soup(res.text, "html.parser")
elem = soup.select("div p")
text = ''
for i in range(len(elem)):
    element = elem[i].getText()

    for j in range(len(element)):
        if element[j] != ".":
            text = text + element[j]
        else:
            text = text + element[j] + "\n"

os.chdir("C:\\Users\\SG704\\Desktop")
file = open("file.txt", "w")
file.write(text)
file.close()
print(text)
