import numpy as np
import requests
import matplotlib.pyplot as plt

API_KEY = "6WI6Q3Q7BLN3BDTI"

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={API_KEY}&outputsize=compact'
r = requests.get(url).json()["Time Series (Daily)"]
# print(json.dumps(r, indent=2))
close_stock = np.empty(shape=(100, 0))
for key, value in r.items():
    close_stock = np.append(close_stock, np.array([float(value["4. close"])]))
plt.scatter(np.arange(0,100), close_stock)
plt.show()
print(close_stock)
