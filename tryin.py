import API, csv
from pathlib import Path

forex = API.api_function()

def coh_function(forex):
    coh_path = Path.cwd()/"csv_report"/"cash_on_hand_usd.csv"
    report_path = Path.cwd()/"summary_report.txt"

    try:
        with coh_path.open(mode="r", encoding = "UTF-8") as file:
            reader = csv.reader(file)
            next(reader)

            coh_list = []
            for line in reader:
                coh_list.append(line)

            index = 0
            deficit = 0

            while index + 1 < len(coh_list):

                if float(coh_list(index)[1]) > float(coh_list[index + 1][1]):

                    deficit = float(coh_list[index][1]) - float(coh_list[index + 1][1])

                    with report_path.open(mode= "a") as file:
                        file.write(f"\n[CASH DEFICIT] DAY: {coh_list[index + 1 ][0]}, AMOUNT: SGD{round((deficit *forex),2)}")
                        file.close()

                index += 1

            if deficit == 0:
                file.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
                file.close()

            file.close()

    except:
        with report_path.open(mode="a") as file:
            file.write("\n[COH File Error] File is missing or not renamed properly. Ensure that file is named 'cash_on_hand_usd.csv")
            file.close()

    else:
        pass







