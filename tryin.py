import API, csv
from pathlib import Path

forex = API.api_function()

def cash_on_hand(forex):
    """"
    function will compute
    the difference in Cash-on-Hand between each
    day. If Cash-on-Hand is not consecutively higher
    each day, the program will highlight the day
    where Cash-on-Hand is lower than the previous
    day and the value difference.
    """
    cash_on_hand_path = Path.cwd()/"csv_report"/"cash_on_hand_usd.csv"
    report_path = Path.cwd()/"summary_report.txt"

    try:
        with cash_on_hand_path.open(mode="r", encoding = "UTF-8") as file:
            reader = csv.reader(file)
            next(reader)

            cash_on_hand_list = []
            for line in reader:
                cash_on_hand_list.append(line)


            deficit = []

            if deficit == []:
                file.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
                file.close()
                
            index = 0
            while index + 1 < len(cash_on_hand_list):

                if float(cash_on_hand_list(index)[1]) > float(cash_on_hand_list[index + 1][1]):

                    deficit = float(cash_on_hand_list[index][1]) - float(cash_on_hand_list[index + 1][1])

                    with report_path.open(mode= "a") as file:
                        file.write(f"\n[CASH DEFICIT] DAY: {cash_on_hand_list[index + 1 ][0]}, AMOUNT: SGD{round((deficit *forex),2)}")
                        file.close()

                index += 1



            file.close()

    except:
        with report_path.open(mode="a") as file:
            file.write("\n[COH File Error] File is missing or not renamed properly. Ensure that file is named 'cash_on_hand_usd.csv")
            file.close()

    else:
        pass







