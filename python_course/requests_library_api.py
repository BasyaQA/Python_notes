# библиотека содержит модули
# библиотека requests позволяет делать запросы к api

import requests

url = "https://api.binance.com/api/v3/ticker/price"

response = requests.get(url, params={"symbol": "BTCUSDT"})

content = response.content

print(content)
print(type(content))
