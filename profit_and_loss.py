import API, csv
from pathlib import Path

forex = API.api_function()

def profit_and_loss(forex):
    """"
    function will compute the
    difference in the net profit between each day. If
    the net profit is not consecutively higher each
    day, the program will highlight the day where net
    profit is lower than the previous day and the value
    difference
    """
    report_path = Path.cwd()/"summary_report.txt"
    profit_n_lost_path = Path.cwd()/"csv_report"/"profit_and_loss_usd.csv"


    try:
        with profit_n_lost_path.open(mode="r", encoding = "UTF-8") as file:
            profit_n_lost_list = []
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                profit_n_lost_list.append(line)


            losses = []

            if losses == []:
                file.write("\n[NET PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
                file.close()

            i = []
            while len(profit_n_lost_list) > i + 1:

                if float(profit_n_lost_list(i+1)[4]) < float(profit_n_lost_list[i][4]):

                    losses = float(profit_n_lost_list[i][4]) - float(profit_n_lost_list[i + 1][4])

                    with report_path.open(mode= "a") as file:
                        file.write(f"\n[PROFIT DEFICIT] DAY: {profit_n_lost_list[i + 1 ][0]}, AMOUNT: SGD{round((losses *forex),2)}")
                        file.close()

                i += 1



            file.close()

    except:
        with report_path.open(mode="a") as file:
            file.write(f"[Cash on hand File Error] There is an error with Cash on hand file. Please try to input correct file name\n")
            file.close()

    else:
        pass




