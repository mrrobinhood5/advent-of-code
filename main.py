import requests
import pprint

data = requests.get("https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USD&limit=1")
j = data.json()
pprint.pp(j)