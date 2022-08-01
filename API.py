import requests , re ,csv

url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey=8YE528VKW69J7ZJ9'
r = requests.get(url)
data = r.json()

function= (CURRENCY_EXCHANGE_RATE)
from_symbol= (USD)
to_symbol= (SGD)
API_KEY = "8YE528VKW69J7ZJ9"
