import API, overheads, profit_and_loss, cash_on_hand

def overall():
    forex = API.api_function()
    max_overheads = overheads.overhead(forex)
    profit_n_loss_losses = profit_and_loss.profit_and_loss(forex)
    cash_on_hand_losses = cash_on_hand.cash_on_hand(forex)

    with open("summary_report.txt", "w") as a:
        a.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}\n")
        a.write(f"[HIGHEST OVERHEAD] {max_overheads[0].upper()}: SGD{max_overheads[1]}\n")

        if cash_on_hand_losses == AttributeError:
            print("Error for cash_on_hand function")
        elif cash_on_hand_losses == []:
            a.write(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
        elif cash_on_hand_losses != []:
            for i in range(len(cash_on_hand_losses)):
                a.write(f"[CASH DEFICIT] DAY: {cash_on_hand_losses[i][0]}, AMOUNT: SGD{cash_on_hand_losses[i][1]}\n")

            

            
        if profit_n_loss_losses == []:
            a.write(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY \n")
        elif profit_n_loss_losses != []:
            for i in range(len(profit_n_loss_losses)):
                a.write(f"[PROFIT DEFICIT] DAY: {profit_n_loss_losses[i][0]}, AMOUNT: SGD{profit_n_loss_losses[i][1]}\n")
        else:
            print("Error for profit_n_loss function")
                
    print("output successful")

print(overall())

