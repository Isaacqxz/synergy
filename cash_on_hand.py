from pathlib import Path
import csv



def cash_on_hand(forex):
    path = str(Path.cwd())
    path += "\csv_report\cash_on_hand_usd.csv"

    rows = []
    with open(path, "r") as a:
        csvread = csv.reader(a)
        next(csvread)

        for row in csvread:
            rows.append(row)
        
    losses = []

    for i in range(len(rows)):
        if i == 0:
            continue #how to change this
    if rows[i][1] < rows[i-1][1]:
        formula = []
        formula.append("{:.2f}".format(float(rows[i][0])))
        formula.append("{:.2f}".format(forex*(int(rows[i-1][1]) - int(rows[i][1]))))

        losses.append(formula)

    return losses
































