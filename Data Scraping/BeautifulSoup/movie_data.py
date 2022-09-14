from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(res.text, "html.parser")
titles = soup.find_all("td", {"class": "titleColumn"})
ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})
with open("C:\\Users\\SG704\\PythonProjects\\Data Scraping\\BeautifulSoup\\movie_data.csv", "w") as f:
    f.write("movie, year, rating\n")
    for i, td in enumerate(titles):
        f.write(f"{td.a.string.replace(',', '')}, {td.span.string.replace('(', '').replace(')', '')}, {ratings[i].strong.string}\n")
