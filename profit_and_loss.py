import csv, API
from pathlib import Path

forex = API.api_function()
# to extract real time currency exchange from USD to SGD from alphavantage.co

def profit_and_loss(forex):
    path = str(Path.cwd())+"\csv_report\profit_and_loss_usd.csv"
    # to extract cash on hand data from MAB game through CSV file
    rows = []
    #empty list for file to append into 
    with open(path, "r") as a:
        # opening profit_and_loss_usd.csv file
        csvread = csv.reader(a)
        next(csvread)
        # skip header of the file
        for row in csvread:rows.append(row)
        # appending cash_on_hand_usd.csv file as a list
        
    losses = []
    # empty list for imputing formula data

    for i in range(len(rows)-1):
        # The range of the list is the number of rows, which we use len to count, -1 since we are skipping the header and do not want to include it as a row
        if rows[i+1][4] < rows[i][4]:
            # using if function to check every rows in the range, if the row i+1, one day ahead, column 4, which is the net profit, 
            # is smaller than just row 1, the current day, will append the difference of the day ahead and the current day 
            formula = []
            # empty list to append information of the difference between previous day and current day
            formula.append(round(float(rows[i+1][4]),2))
            # this is to extract the day where the net profit is lesser than the previous day
            formula.append(round(forex*(int(rows[i][4]) - int(rows[i+1][4])),2))
            # this is to extract the net profit difference between previous day and current day
            losses.append(formula)
            # write in the above data


    return losses
    # put the data into empty list


with open("summary_report.txt", "a") as a:
    # open a text file to write the datas
    if profit_and_loss(forex) == []:
        # if no data is extracted, that means net profit on each day is higher than the previous day
        a.write(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY \n")

    else:
        for i in range(len(profit_and_loss(forex))):
            #  if there is data extracted, will be appended
            a.write(f"[PROFIT DEFICIT] DAY: {profit_and_loss(forex)[i][0]}, AMOUNT: SGD{profit_and_loss(forex)[i][4]}\n")


