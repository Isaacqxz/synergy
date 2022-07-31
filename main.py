import requests
import re


url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey=8YE528VKW69J7ZJ9'
r = requests.get(url)
data = r.json()

print(data)
print(data['Time Series FX (Weekly)'])
