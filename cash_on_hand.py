import API, csv
from pathlib import Path

forex = API.api_function()

def cash_on_hand(forex):
    """"
    function will compute the difference in Cash-on-Hand between each day. 
    If Cash-on-Hand is not consecutively higher each day, the program will highlight the day
    where Cash-on-Hand is lower than the previous day and the value difference.
    """
    summary_path = Path.cwd()/"summary_report.txt"
    cash_on_hand_path = Path.cwd()/"csv_report"/"cash_on_hand_usd.csv"
    # creating file_data

    try:
        # exception handling
        with cash_on_hand_path.open(mode="r", encoding = "UTF-8") as file_data:
            # opening file as read to retrieve data from cash_on_hand_used.csv
            cash_on_hand_list = []
            # creating a empty list to append into
            reader = csv.reader(file_data)
            next(reader)
            # To skip the header
            for line in reader:
                cash_on_hand_list.append(line)
            # appending into empty list




            i = 0
            losses = []
            # empty variables

            while len(cash_on_hand_list) > i + 1:

                if float(cash_on_hand_list[i+1][1]) < float(cash_on_hand_list[i][1]):

                    losses = float(cash_on_hand_list[i][1]) - float(cash_on_hand_list[i + 1][1])

                    with summary_path.open(mode= "file_data") as file_data:
                        file_data.write(f"\n[CASH DEFICIT] DAY: {cash_on_hand_list[i + 1 ][0]}, AMOUNT: SGD{round((losses *forex),2)}")
                        file_data.close()

                i += 1



            if losses == []:
                file_data.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
                file_data.close()



            file_data.close()

    except:
        with summary_path.open(mode="file_data") as file_data:
            file_data.write(f"\n[Cash on hand file_data Error] There is an error with Cash on hand file_data. Please try to input correct file_data name\n")
            file_data.close()

    else:
        pass
            































