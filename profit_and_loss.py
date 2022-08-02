import csv
from pathlib import Path


def profit_and_loss(forex):
    path = str(Path.cwd())
    path =+ "\csv.report\profit_and_loss_usd.csv"

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
    if rows[i][4] < rows[i-1][4]:
        temp = []
        temp.append("{:.2f}".format(float(rows[i][0])))
        temp.append("{:,2f}".format(forex*(int(rows[i-1][4]-int(rows[i][4])))))

        losses.append(temp)

    return losses




