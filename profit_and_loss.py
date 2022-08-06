import API, csv 
from pathlib import Path 
 
forex = API.api_function() 
 
def profit_and_loss(forex): 
    """" 
    function will compute the difference in the net profit between each day. 
    If the net profit is not consecutively higher each day, 
    the program will highlight the day where net profit is lower than the previous day 
    and the value difference 
    """ 
    summary_path = Path.cwd()/"summary_report.txt" 
    profit_n_lost_path = Path.cwd()/"csv_report"/"profit_and_loss_usd.csv" 
    # creating file_data 
 
 
    try: 
        # exception handling 
        with profit_n_lost_path.open(mode="r", encoding = "UTF-8") as file_data: 
            # opening file as read to retrieve data from profit_and_loss_used.csv 
            profit_n_lost_list = [] 
            # creating a empty list to append into 
            reader = csv.reader(file_data) 
            next(reader) 
            # To skip the header 
            for line in reader: 
                profit_n_lost_list.append(line) 
            # appending into empty list 
 
            i = 0 
            losses = [] 
            # empty variables 
 
            while len(profit_n_lost_list) > i + 1: 
                # using len as the amount of rows there is in the csv file  
                # using while to create a loop so that code runs through all the datas len 
 
                if float(profit_n_lost_list[i+1][4]) < float(profit_n_lost_list[i][4]): 
                # using if function to check every rows in the range, if the row  is i+1 ,which is one day ahead and if the column 4,  
                # which is the net profit, is smaller than just row 1, which is the current day 
 
                    losses = float(profit_n_lost_list[i][4]) - float(profit_n_lost_list[i + 1][4]) 
                    # will append the difference of the day ahead and the current day  
 
                    with summary_path.open(mode= "a") as file_data: 
                        file_data.write(f"\n[PROFIT DEFICIT] DAY: {profit_n_lost_list[i + 1 ][0]}, AMOUNT: SGD{round((losses *forex),2)}") 
                        file_data.close() 
                    # opening the summary path to write the PROFIT DEFICIT data into it. Forex is to convert USD to SGD 
 
                i += 1 
                # so that it will run the next line 
 
            if losses == []: 
                # if no data is extracted, which means net profit on each day is higher than the previous day, this if will run instead 
                with summary_path.open(mode= "a") as file_data: 
                    # opening summary path 
                    file_data.write("\n[NET PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY") 
                    file_data.close() 
                    # writing NET PROFIT SURPLUS in summary path 
 
            file_data.close() 
            # close file 
 
    except: 
        with summary_path.open(mode="a") as file_data: 
            # opening summary path 
            file_data.write(f"\n[Profit and loss] There is an error with profit_and_loss_data. Please try to input correct file_data name") 
            # writing error code to notify that code is not working 
            file_data.close() 
            # close file 
 
    else: 
        pass 
    # continue