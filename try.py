import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=T6RUC1GIJE0O6U1T'
# get the url to extract data from alphavantage
r = requests.get(url)
data = r.json()

print(data.keys())