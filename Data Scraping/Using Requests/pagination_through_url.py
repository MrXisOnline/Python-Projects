import requests

with open('C:\\Users\\SG704\\PythonProjects\\Data Scraping\\Using Requests\\quotes.txt', 'w', encoding='utf-8') as f:
    for page in range(1, 10):
        res = requests.get(f"https://quotes.toscrape.com/page/{page}/")
        for line in res.text.split("\n"):
            if '<span class="text" itemprop="text">' in line:
                f.write(line.replace('<span class="text" itemprop="text">', '').replace("</span>", '').strip())
                f.write("\n")