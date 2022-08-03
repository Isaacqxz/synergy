import csv, API
from pathlib import Path

forex = API.api_function()

def overhead(forex):
    path = str(Path.cwd())+"\csv_report\overheads.csv"

    rows = []
    with open(path, "r") as a:
        csvreader = csv.reader(a)
        next(csvreader)

        for row in csvreader:rows.append(row)

    max = 0
    Highest_overhead = []

    for i in range(len(rows)):
        if max < float(rows[i][1]):
            max = float(rows[i][1])
            Highest_overhead = [rows[i][0], round((max * forex),2)]

        with open("summary_report.txt", "w") as a:
            a.write(f"[HIGHEST OVERHEAD] {overhead(forex)[0].upper()}: SGD{overhead(forex)[1]}\n")
            a.close()

    return Highest_overhead