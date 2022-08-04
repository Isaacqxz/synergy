import csv, API
from pathlib import Path

forex = API.api_function()

def overhead(forex):
    
    path = str(Path.cwd())+"\csv_report\overheads.csv"
    try:
        rows = []
        with open(path, "r") as a:
            csvreader = csv.reader(a)
            next(csvreader)

            for row in csvreader:rows.append(row)

        max = 0
        # this is so that the first number in overheads.csv can be max since all overheads is > 0. After first number is max, the code will use the max and compare with subsequence data to aquire new max
        Highest_overhead = []

        for i in range(len(rows)):
            if max < float(rows[i][1]):
                max = float(rows[i][1])
                Highest_overhead = [rows[i][0], round((max * forex),2)]

            return Highest_overhead

        with open("summary_report.txt", "a") as a:
            a.write(f"[HIGHEST OVERHEAD] {overhead(forex)[0].upper()}: SGD{overhead(forex)[1]}\n")

    except:
        with open("summary_report.txt", "a") as a:
            a.write("problem")
    else:
        with open("summary_report.txt", "a") as a:
            a.write(f"[HIGHEST OVERHEAD] {overhead(forex)[0].upper()}: SGD{overhead(forex)[1]}\n")
        # pass