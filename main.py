import API, overheads, profit_and_loss, cash_on_hand, tryin
# import from API, overheads, profit_and_loss, cash_on_hand, tryin into main.py

#defining function
def main():
    """
    
    """
    forex = API.api_function()    
    overheads.overhead(forex)
    cash_on_hand.cash_on_hand(forex)
    profit_and_loss.profit_and_loss(forex)
    return("output successful")

#printing the function
print(main())
