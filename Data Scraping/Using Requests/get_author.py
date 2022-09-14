import requests

response = requests.get("https://quotes.toscrape.com")
if response.status_code == 200:
    with open("C:\\Users\\SG704\\PythonProjects\\Data Scraping\\Using Requests\\authors.txt", "w") as f:
        for line in response.text.split("\n"):
            if ' <span>by <small class="author" itemprop="author">' in line:
                f.write(line.split('<span>by <small class="author" itemprop="author">')[1][:-8] + "\n")

