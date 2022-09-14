from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup("<b class='bold_text' id='b1'>Hey You</b><img src='img.jpg' alt='cow'/>", "html.parser")
print(soup.b, soup.img)
print(soup.b["class"], soup.img["alt"])
print(soup.img.attrs)
print(soup.b.attrs)
soup.b["id"] = "nb1"
print(soup.b.attrs)