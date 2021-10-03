# import modules 
import csv
import os

# source to read budget data file
budget_path = os.path.join('Resources', "budget_data.csv")

#output file
outputFile = os.path.join('analysis', "budget_analysis.txt")


#variables initialize to 0  
totalMonths= 0
net_profit_loss = 0.0
net_profit_loss_change = 0.0
prev_profit_loss = 0.0
avg_net_profit_loss_change = 0.0
row_num = 1
max_increase_profit = 0.0
max_increase_profit_date = ""
max_decrease_profit = 0.0
max_decrease_profit_date = ""
profit_loss_change = 0.0
# read the csv file 
with open(budget_path) as budget_data:
    #create a csv reader object 
    csvreader = csv.reader(budget_data)
    header = next(csvreader)

    for row  in csvreader:
        totalMonths += 1
        net_profit_loss += float(row[1])

        if row_num != 1:
            profit_loss_change = float(row[1]) - prev_profit_loss

        net_profit_loss_change += profit_loss_change

        # calculate greatest increase in profit
        if profit_loss_change > max_increase_profit:
            max_increase_profit = profit_loss_change
            max_increase_profit_date = row[0]
        
        # calculate greatest decrease in profit
        if profit_loss_change < max_decrease_profit:
            max_decrease_profit = profit_loss_change
            max_decrease_profit_date = row[0]
        row_num+=1
        prev_profit_loss = float(row[1])

    avg_net_profit_loss_change = net_profit_loss_change / (totalMonths - 1)

output = (
    f"\nFinancial Analysis\n"
    "------------------------\n"
    f"\tTotal Months: {totalMonths}\n"
    f"\tTotal: ${round(net_profit_loss)}\n"
    f"\tAverage Change: ${round(avg_net_profit_loss_change,2)}\n"
    f"\tGreatest Increase in Profits: {max_increase_profit_date} (${round(max_increase_profit)})\n"
    f"\tGreatest Decrease in Profits: {max_decrease_profit_date} (${round(max_decrease_profit)})\n"
)

print(output)

# Export to analysis file
with open(outputFile,"w") as textFile:
    textFile.write(output)

