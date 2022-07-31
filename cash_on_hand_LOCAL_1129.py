import requests
import re

url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey=8YE528VKW69J7ZJ9'
r = requests.get(url)
data = r.json()
# weekly_average = sum(data)

# [x for x in data if '1.' in str(x)]
# print(x)
# # n = [1.[0-9][0-9][0-9][0-9][0-9]]
# # if n in data:
# #     print("true")

# # print(data)
# # print(weekly_average)
for weekly in data:
    empty_list=[]
    weekly = re.findall(r"\'4. close\': \'1.[0-9][0-9][0-9][0-9][0-9]\'", data)
    # empty_list.append(weekly) 
    print(weekly)

# string = ''.join(data)
# for weekly in data:
#     match = re.findall(r"\'4. close\': \'1.[0-9][0-9][0-9][0-9][0-9]\'")





print(match)
# print(data['Time Series FX (Weekly)'])

