import requests , re ,csv

# url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey=8YE528VKW69J7ZJ9'
# r = requests.get(url)
# data = r.json()

def api_function():
    function= "CURRENCY_EXCHANGE_RATE"
    from_symbol= "USD"
    to_symbol= "SGD"
    api_key = "8YE528VKW69J7ZJ9"

    url = f'https://www.alphavantage.co/query?function={function}&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={api_key}'

    data = requests.get(url).json()

    return float(data["Realtime Currency Exchange Rate"]["5. exchange Rate"])
