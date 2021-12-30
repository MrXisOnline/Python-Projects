from bs4 import BeautifulSoup as soup
import requests

# print(os.path.exists("C:\\Users\\SG704\\PythonProjects\\oneTimeProjects\\web dev\\personal site html\\index.html"))
# with open("..\\web_dev\\personal_site\\index.html") as f:
# 	html = soup(f.read(), "html.parser")
# tags = html.find_all(name="td")
# for tag in tags:
# 	print(tag.getText())
# tag = html.find(name="h3",id="b1")
# print(tag.getText())
# com = html.select_one(selector="p a")
# print(com.getText())
# com = html.select(".head")
# print(com)

response = requests.get(url="https://news.ycombinator.com/")
text = response.text
html = soup(text,"html.parser")
a_list = html.select(".title a")
span_list = html.select("td .score")
i=0
for a in a_list:
	print(a.getText())
	print(a.get("href"))
	print(span_list[i].getText().split(" ")[0])
	i += 1