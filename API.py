
from turtle import hideturtle
import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=T6RUC1GIJE0O6U1T'
# get the url to extract data from alphavantage
link = requests.get(url)
data = link.json()

def api_function():
    """
    Function is to extract real time currency exchange from USD to SGD from alphavantage.co
    """


    return float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

forex = api_function()

with open("summary_report.txt", "w") as a:
    a.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}\n")




