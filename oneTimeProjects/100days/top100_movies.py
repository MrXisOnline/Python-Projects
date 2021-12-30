from bs4 import BeautifulSoup as soup
import requests as rq

response = rq.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
text = response.text
html = soup(text, "html.parser")
movies = html.find_all(name="h3", class_="title")
print(movies)
