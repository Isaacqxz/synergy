from pathlib import Path
import csv, API
forex = API.api_function()
# to extract real time currency exchange from USD to SGD from alphavantage.co


def cash_on_hand(forex):
    """"
    function will compute
    the difference in Cash-on-Hand between each
    day. If Cash-on-Hand is not consecutively higher
    each day, the program will highlight the day
    where Cash-on-Hand is lower than the previous
    day and the value difference.
    """

    path = str(Path.cwd())/"csv_report"/"cash_on_hand_usd.csv"
    # to extract cash on hand data from MAB game through CSV file
    rows = []
    #empty list for file to append into 
    with open(path, "r") as a:
        # opening cash_on_hand_usd.csv file
        csvread = csv.reader(a)
        next(csvread)
        # skip header of the file
        for row in csvread:rows.append(row)
        # appending cash_on_hand_usd.csv file as a list
            
    losses = []
    # empty list for 


    for i in range(len(rows)-1):
        # Using for i is a variable.
        # The range of the list is the number of rows, which we use len to count, -1 since we are skipping the header and do not want to include it as a row
        if rows[i+1][1] < rows[i][1]:
            # using if function to check every 
            formula = []
            formula.append(round(float(rows[i+1][0]),2))
            formula.append(round(forex*(int(rows[i][1]) - int(rows[i+1][1])),2))
            losses.append(formula)
        
    return losses


with open("summary_report.txt", "a") as a:
    if cash_on_hand(forex) == []:
        a.write(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")

    else:
        for i in range(len(cash_on_hand(forex))):
            a.write(f"[CASH DEFICIT] DAY: {cash_on_hand(forex)[i][0]}, AMOUNT: SGD{cash_on_hand(forex)[i][1]}\n")




            
            # return losses

    # with open("summary_report.txt", "a") as a:
    #     if cash_on_hand(forex) == []:
    #         a.write(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")

    #     else:
    #         for i in range(len(cash_on_hand(forex))):
    #             a.write(f"[CASH DEFICIT] DAY: {cash_on_hand(forex)[i][0]}, AMOUNT: SGD{cash_on_hand(forex)[i][1]}\n")
    # except:
    #     with open("summary_report.txt", "a") as a:
    #         a.write("help")

    # else:
    #     pass
        # with open("summary_report.txt", "a") as a:
        #     if cash_on_hand(forex) == []:
        #         a.write(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")

        #     else:
        #         for i in range(len(cash_on_hand(forex))):
        #             a.write(f"[CASH DEFICIT] DAY: {cash_on_hand(forex)[i][0]}, AMOUNT: SGD{cash_on_hand(forex)[i][1]}\n")

                































