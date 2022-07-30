import requests
import re, csv

url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey=8YE528VKW69J7ZJ9'
r = requests.get(url)
data = r.json()

# dict_keys(['Meta Data', 'Time Series FX (Weekly)'])
# print(data["Meta Data"])

import json
# print(json.dumps(data["Time Series FX (Weekly)"],indent=4 ))

close_data = data["Time Series FX (Weekly)"]
print(close_data)
# for close in close_data:
#     print(close["4. close"])