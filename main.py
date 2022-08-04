import API, overheads, profit_and_loss, cash_on_hand, tryin


def main():
    forex = API.api_function()    
    overheads.overhead(forex)
    tryin.cash_on_hand(forex)
    profit_and_loss.profit_and_loss(forex)
    return("output successful")

print(main())
