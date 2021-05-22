# main file for PyBank
#import the modules necessary to create file paths and read csv files

import os
import csv

dates = []
profit_changes = []
profits = []
average_profit_change = 0
max_profit_change = 0
min_profit_change = 0
output_file = "budget_solution.txt"

#store the file path associated with the file
csvPath = os.path.join('.', 'Resources', 'budget_data.csv')

#read the csv file
with open (csvPath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for r in csvreader:
        dates.append(r[0])
        profits.append(int(r[1]))
        


#Count the rows to get the total number of months minus the header

total_month_count = len(dates)

#Calculate the total Profit/Losses over time

total_profits = sum(profits)

#Calculate the changes in Profit/Losses, find the average change

for i in range(len(profits)-1):
    profit_changes.append(profits[i+1] - profits[i])

average_profit_change = sum(profit_changes)/len(profit_changes)

#Determine the greatest increase in profits (date and amount)

max_profit_change = max(profit_changes)
index_of_max = profit_changes.index(max_profit_change)
max_profit_change_date = str(dates[index_of_max])

#Determine the greatest decrease in profits (date and amount)

min_profit_change = min(profit_changes)
index_of_min = profit_changes.index(min_profit_change)
min_profit_change_date = str(dates[index_of_min])

# Add text that will display the info as shown in the example
print("Financial Analysis")
print("=============================")
print("Total Months: " + str(total_month_count))
print("Total Revenue: " + str(total_profits))
print("Average Revenue Change: " + "$" + str(average_profit_change))
print("Greatest Increase in Revenue " + str(max_profit_change_date) + "  $" + str(max_profit_change))
print("Greatest Decrease in Revenue " + str(min_profit_change_date) + "  $" + str(min_profit_change))

# Write to new text file
with open(output_file, 'w') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("====================\n")
    txt_file.write("Total Months: " + str(total_month_count) + "\n")
    txt_file.write("Total Revenue: " + str(total_profits) + "\n")
    txt_file.write("Average Revenue Change: " + "$" + str(average_profit_change) + "\n")
    txt_file.write("Greatest Increase in Revenue " + str(max_profit_change_date) + "  $" + str(max_profit_change) + "\n")
    txt_file.write("Greatest Decrease in Revenue " + str(min_profit_change_date) + "  $" + str(min_profit_change))