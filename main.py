import requests
import re

url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey=8YE528VKW69J7ZJ9'
r = requests.get(url)
data = r.json()

#data['Time Series FX (Weekly)']
#check what this is. look at the format of what comes out. identified the weeks are the keys of the dictionary


weeks = list(data['Time Series FX (Weekly)'].keys())
#take the weeks only and put into list

answers = {}
for i in weeks:
    answers[i]=float(data['Time Series FX (Weekly)'][i]['4. close'])
#we need this to be float, not string.

#iterate thru all the weeks present, put into a new dictionary called answers as key, value as closing price for that week.

length = len(answers)
closing_price = list(answers.values())
mean_closing_price = sum(closing_price)/length
print(mean_closing_price)
