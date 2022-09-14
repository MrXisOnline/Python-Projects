from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.imdb.com/chart/top/").text
soup = BeautifulSoup(res, "html.parser")
titles = soup.find_all("td", {"class": "titleColumn"})
movies = {title.a.text: "https://www.imdb.com/"+title.a["href"] for title in titles}
movie_name = input("Movie Name: ")
for key, value in movies.items():
    if key == movie_name:
        n_res = requests.get(value).text
        n_soup = BeautifulSoup(n_res, "html.parser")
        ul = n_soup.find("ul", {"class": ["fEgKYH"]})
        director = ul.find_all("li")[0].div.ul.li.a
        print("Director Name:", director.text)
        nn_res = requests.get("https://www.imdb.com" + director["href"]).text
        nn_soup = BeautifulSoup(nn_res, "html.parser")
        known_for_divs = nn_soup.find("div", {"id": "knownfor"}).find_all("div", {"class": "knownfor-title"})
        known_for_movies = {div.find("div", {"class": "knownfor-title-role"}).a.text: "https://www.imdb.com" + div.find("div", {"class": "knownfor-title-role"}).a["href"] for div in known_for_divs}
        print("Known for Movies Like --- ")
        for movie, link in known_for_movies.items():
            print(movie, link)

