import requests as req

response = req.get("https://quotes.toscrape.com/")
if response.status_code == 200:
    for line in response.text.split("\n"):
        if '<span class="text" itemprop="text">' in line:
            # print(line)
            print(line.split('<span class="text" itemprop="text">')[1][:-7])
