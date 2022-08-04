import csv, API
from pathlib import Path

forex = API.api_function()

def profit_and_loss(forex):
    path = str(Path.cwd())+"\csv_report\profit_and_loss_usd.csv"
    rows = []
    with open(path, "r") as a:
        csvread = csv.reader(a)
        next(csvread)
        for row in csvread:rows.append(row)
        
    losses = []

    for o in range(len(rows)-1):
        if rows[o+1][4] < rows[o][4]:
            formula = []
            formula.append(round(float(rows[o+1][4]),2))
            formula.append(round(forex*(int(rows[o][4]) - int(rows[o+1][4])),2))
            losses.append(formula)
            print(o)


    return losses


with open("summary_report.txt", "a") as a:
    if profit_and_loss(forex) == []:
        a.write(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY \n")
        # a.close()
    else:
        for i in range(len(profit_and_loss(forex))):
            a.write(f"[PROFIT DEFICIT] DAY: {profit_and_loss(forex)[i][0]}, AMOUNT: {profit_and_loss(forex)[i][4]}\n")
            # a.close()






