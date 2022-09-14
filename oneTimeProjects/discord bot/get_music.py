from bs4 import BeautifulSoup as soup
import requests
import os

url = "https://www.myinstants.com"
search = '/en/search/?name='
item = "john+cena"
res = requests.request('GET', url=url+search+item)
text = res.text
html = soup(text, "html.parser")
s_elements = html.select(".instant .small-button")
song = s_elements[0].get("onclick")
song = song.split("'")[-2]
song_link = url + song
song_raw = requests.get(song_link, stream=True)
with open(os.path.join("C:\\Users\\SG704\\PythonProjects\\oneTimeProjects\\discord bot", song_link.split("/")[-1]), 'wb') as fd:
    for chunk in song_raw.iter_content(chunk_size=128):
        fd.write(chunk)
# print(song_raw.raw)
# print(song_link.split("/")[-1])


