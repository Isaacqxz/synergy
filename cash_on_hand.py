from pathlib import Path
from tkinter.tix import DisplayStyle
import requests
import re, csv


# file_path_deceit = Path(r"deceit_report.txt")

# file_path_cash = Path(r"cash-on-hand-usd.csv")
# file_path_overheads = Path(r"overheads-day-90.csv")
# file_path_pnl = Path(r"profit-and-loss-usd.csv")



# with file_path_overheads.open(mode="r", encoding = "UTF-8", newline="") as file:
#     csv.reader(file_path_overheads, delimiter=' ')
#     included_cols = [1,2]




#         with file_path_deceit.open(mode="w") as file:
#             file.write("HIGHEST OVERHEADS {highest_overheads}")
#         file.close()
    
    
file_path_overheads = Path.cwd()/"CSV.report"/"overheads-day-90.csv"

with file_path_overheads.open(mode="r", encoding = "UTF-8", newline="") as file:
    data = csv.reader(file, delimiter=';')
    maxVal = []
    for i in data:
        maxVal.append(float(i[1]))


csv.writer.writerow(maxVal)
print(max(maxVal))


# QUESTIONS FOR TEACHER:
# how to highlight/flag 
# how to read the specific columns
# how to if values is highest




# for i in range(1,len(coh)):
#     deficit = coh["Cash On Hand"][i-1] - coh["Cash On Hand"][i]
#     if(deficit > 0):
#         print(pnl['Day'][i] , deficit)



























