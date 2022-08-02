import requests , re ,csv

url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey=8YE528VKW69J7ZJ9'
r = requests.get(url)
data = r.json()

#data['Time Series FX (Weekly)']
#the keys of the dictionary


weeks = list(data['Time Series FX (Weekly)'].keys())
#taking the weeks only and putting into list

answers = {}
for i in weeks:
    answers[i]=float(data['Time Series FX (Weekly)'][i]['4. close'])
#change to float

#iterate thru all the weeks present, value as closing price for that week.

length = len(answers)
closing_price = list(answers.values())
mean_closing_price = sum(closing_price)/length
print(mean_closing_price)
