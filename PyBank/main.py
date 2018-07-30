#open csv file
import os 
import csv

csvpath = os.path.join('.','PyBank','budget_data.csv')

with open (csvpath,newline = '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    #header
    csv_header = next(csvreader)

    Totalnumberofmonths = 0
    Total = 0
    Revenue = []
    Date = []

    for row in csvreader:
        if row[0] != None:
            Totalnumberofmonths += 1
            Date.append(row[0])
        if row[1] != None:
            Total = Total + int(row[1])
            Revenue.append(row[1])

    change_list = []
    for i in range(len(Revenue)-1):
        change = int(Revenue[i+1]) - int(Revenue[i])
        change_list.append(change)
        max_change = max(change_list)
        min_change = min(change_list)
        average_change = sum(change_list)/len(change_list)

    index_max_change = change_list.index( max_change )
    index_min_change = change_list.index( min_change )
    Date_max = Date[index_max_change]
    Date_min = Date[index_min_change]
    
    print(f''' Financial Analysis 
                ----------------------------
                Total Months: {Totalnumberofmonths}
                Total: {Total}
                Average  Change: ${average_change}
                Greatest Increase in Profits: {Date_max} (${max_change})
                Greatest Decrease in Profits: {Date_min} (${min_change})''')

    with open(os.path.join('.','PyBank','output.txt'), "w") as text_file:
        print(f''' Financial Analysis 
                ----------------------------
                Total Months: {Totalnumberofmonths}
                Total: {Total}
                Average  Change: ${average_change}
                Greatest Increase in Profits: {Date_max} (${max_change})
                Greatest Decrease in Profits: {Date_min} (${min_change})''', file=text_file)