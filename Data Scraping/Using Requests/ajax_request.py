import requests
import json
record = 5
for page in range(1, 2):
    res = requests.get(f"https://hs-consumer-api.espncricinfo.com/v1/edition/feed?edition=in&lang=en&page={page}&records={record}")
    res = json.loads(res.text)
    for i in range(0, record):
        print(res["results"][i]["containers"][0]["item"]["title"])