from pathlib import Path
import csv, API
forex = API.api_function()



def cash_on_hand(forex):
    path = str(Path.cwd())+"\csv_report\cash_on_hand_usd.csv"


    rows = []
    with open(path, "r") as a:
        csvread = csv.reader(a)
        next(csvread)

        for row in csvread:rows.append(row)
        
    losses = []

    for i in range(len(rows)-1):
        if rows[i+1][1] < rows[i][1]:
            formula = []
            formula.append(round(float(rows[i+1][0]),2))
            formula.append(round(forex*(int(rows[i][1]) - int(rows[i+1][1])),2))
            losses.append(formula)
            print(cash_on_hand(forex))
        
    return losses

with open("summary_report.txt", "a") as a:
    if cash_on_hand(forex) == []:
        a.write(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
        a.close()
    else:
        for i in range(len(cash_on_hand(forex))):
            a.write(f"[CASH DEFICIT] DAY: {cash_on_hand(forex)[i][0]}, AMOUNT: {cash_on_hand(forex)[i][1]}\n")
            a.close()
                































