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


    try:
        with cash_on_hand_path.open(mode="r", encoding = "UTF-8") as a:
            cash_on_hand_list = []
            reader = csv.reader(a)
            next(reader)
            for line in reader:
                cash_on_hand_list.append(line)




            i = 0
            losses = []

            while len(cash_on_hand_list) > i + 1:

                if float(cash_on_hand_list[i+1][1]) < float(cash_on_hand_list[i][1]):

                    losses = float(cash_on_hand_list[i][1]) - float(cash_on_hand_list[i + 1][1])

                    with report_path.open(mode= "a") as a:
                        a.write(f"\n[CASH DEFICIT] DAY: {cash_on_hand_list[i + 1 ][0]}, AMOUNT: SGD{round((losses *forex),2)}")
                        a.close()

                i += 1



            if losses == []:
                a.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
                a.close()



            a.close()

    except:
        with report_path.open(mode="a") as a:
            a.write(f"\n[Cash on hand a Error] There is an error with Cash on hand a. Please try to input correct a name\n")
            a.close()

    else:
        pass
            































