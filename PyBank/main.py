# main file for PyBank
#import the modules necessary to create file paths and read csv files

import os
import csv

#store the file path associated with the file
csvPath = os.path.join('.', 'Resources', 'budget_data.csv')

#read the csv file
with open (csvPath) as csvfile:
    #count the rows to ge tthe total number of months minus the header
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    csvData = list(csvreader)
    rowCount = len(csvData)
    print("The total number of months is: ")
    print(rowCount)

#Calculate the total Profit/Losses over time
    amount = (int(row[1]) for row in csvreader)
    total = sum(amount)
    print(total)


#Calculate the changes in Profit/Losses, find the average change



#Determine the greatest increase in profits (date and amount)



#Determine the greatest decrease in profits (date and amount)





