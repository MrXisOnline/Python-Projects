import requests

quote = ''
author = ''
for page in range(1, 11):
    res = requests.get(f"https://quotes.toscrape.com/page/{page}/")
    with open("C:\\Users\\SG704\\PythonProjects\\Data Scraping\\Using Requests\\author_quotes.csv", "a", encoding='utf-8') as f:
        for line in res.text.split("\n"):
            if '<span class="text" itemprop="text">' in line:
                quote = line.replace('<span class="text" itemprop="text">', '').replace("</span>", '').strip()
            elif '<span>by <small class="author" itemprop="author">' in line:
                author = line.replace('<span>by <small class="author" itemprop="author">', '').replace("</small>", '').strip()
                f.write(f"{author}, {quote.replace(',', '')}" + "\n")

