from bs4 import BeautifulSoup
import requests

web = "https://www.imdb.com"
res = requests.get("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(res.text, "html.parser")
titles = soup.find_all("td", {"class": "titleColumn"})
ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})
for i in range(0, 10):
    link = web + titles[i].a["href"]
    link_res = requests.get(link)
    link_soup = BeautifulSoup(link_res.text, "html.parser")
    ul = link_soup.find("ul", {"class": ["kqWovI"]})
    lis = ul.find_all("li")
    div = link_soup.find("div", {"class": ["ggbGKe"]})
    genres = div.find_all("div")[1].find_all("a")
    genre_text = " ".join(gen.text for gen in genres)
    print(f"{titles[i].a.string.replace(',', '')}, {titles[i].span.string.replace('(', '').replace(')', '')}, {ratings[i].strong.string}, {lis[0].a.text}, {lis[-1].text}, {genre_text}\n")