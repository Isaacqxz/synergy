import API, csv
from pathlib import Path

forex = API.api_function()

def cash_on_hand(forex):
    """"
    function will compute the difference in Cash-on-Hand between each day. 
    If Cash-on-Hand is not consecutively higher each day, the program will highlight the day
    where Cash-on-Hand is lower than the previous day and the value difference.
    """
    report_path = Path.cwd()/"summary_report.txt"
    cash_on_hand_path = Path.cwd()/"csv_report"/"cash_on_hand_usd.csv"


    # try:
    with cash_on_hand_path.open(mode="r", encoding = "UTF-8") as file:
        cash_on_hand_list = []
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            cash_on_hand_list.append(line)




        i = float[]
        losses = []

        while len(cash_on_hand_list) > i + 1:

            if float(cash_on_hand_list(i+1)[1]) < float(cash_on_hand_list[i][1]):

                losses = float(cash_on_hand_list[i][1]) - float(cash_on_hand_list[i + 1][1])

                with report_path.open(mode= "a") as file:
                    file.write(f"\n[CASH DEFICIT] DAY: {cash_on_hand_list[i + 1 ][0]}, AMOUNT: SGD{round((losses *forex),2)}")
                    file.close()

            i += 1



        if losses == []:
            file.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            file.close()



        file.close()

    # except:
    #     with report_path.open(mode="a") as file:
    #         file.write(f"[Cash on hand File Error] There is an error with Cash on hand file. Please try to input correct file name\n")
    #         file.close()

    # else:
    #     pass
            































