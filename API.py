from turtle import hideturtle
import requests

def api_function():
    
    # function= "CURRENCY_EXCHANGE_RATE"
    # from_symbol= "USD"
    # to_symbol= "SGD"
    # apikey = "T6RUC1GIJE0O6U1T"

    # url = f'https://www.alphavantage.co/query?function={function}&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={apikey}'

    # data = requests.get(url).json()
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=T6RUC1GIJE0O6U1T'
    r = requests.get(url)
    data = r.json()

    return float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])



