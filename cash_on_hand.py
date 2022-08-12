import API, csv
from pathlib import Path

forex = API.api_function()

def cash_on_hand(forex):
    """"
    function will compute the    
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
            losses = 0
            # empty variables

            while len(cash_on_hand_list) > i + 1:
                # using len as the amount of rows there is in the csv file 
                # using while to create a loop so that code runs through all the datas len

                if float(cash_on_hand_list[i+1][1]) < float(cash_on_hand_list[i][1]):
                # using if function to check every rows in the range, if the row  is i+1 ,which is one day ahead and if the column 4, 
                # which is the Cash on hand, is smaller than just row 1, which is the current day
                    losses = float(cash_on_hand_list[i][1]) - float(cash_on_hand_list[i + 1][1])
                # will append the difference of the day ahead and the current day 
                    with summary_path.open(mode= "a") as file_data:
                        file_data.write(f"\n[CASH DEFICIT] DAY: {cash_on_hand_list[i + 1][0]}, AMOUNT: SGD{round((losses *forex),2)}")
                        file_data.close()
                    # opening the summary path to write the CASH DEFICIT data into it. Forex is to convert USD to SGD
                i += 1
                # it will run the next line before looping 


            if losses == 0:
                # if no data is extracted, meaning that net profit on each day is higher than the previous day, this if will run instead. 


                with summary_path.open(mode= "a") as file_data:
                    # opening summary path
                    file_data.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
                    file_data.close()
                    # writing NET CASH SURPLUS in summary path



            file_data.close()
            # close the file


    except:
        with summary_path.open(mode="a") as file_data:
            # opening summary path
            file_data.write(f"\n[Cash on hand file_data Error] There is an error with Cash on hand file_data. Please try to input correct file_data name")
            # writing error code to notify that code is not working
            file_data.close()
            # close file
    else:
        pass































