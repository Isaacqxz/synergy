import requests

def api_function():
    
    function= "CURRENCY_EXCHANGE_RATE"
    from_symbol= "USD"
    to_symbol= "SGD"
    apikey = "8YE528VKW69J7ZJ9"

    url = f'https://www.alphavantage.co/query?function={function}&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={apikey}'

    data = requests.get(url).json()

    return float(data)
