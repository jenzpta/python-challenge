# Module for reading CSV file
import os
import csv

# Define file path
csvpath = os.path.join('..', 'Pybank', 'Resources', 'budget_data.csv')

# Declare variables
total_months = 0
net_profit_loss = 0
profit_loss_change = []
previous_profit_loss = None
greatest_pro_increase_date = ""
greatest_pro_increase = 0
greatest_pro_decrease = 0
greatest_pro_decrease_date = ""
average_change = 0

# Open CSV file
with open('budget_data.csv') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter= ",")
    next(csv_reader)

    # Read through each row of data
    for row in csv_reader:
        total_months += 1
        profit_loss = int(row[1])
        net_profit_loss += profit_loss

        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            profit_loss_change.append(change)

            if change > greatest_pro_increase:
                greatest_pro_increase = change
                greatest_pro_increase_date = row[0]

            if change < greatest_pro_decrease:
                greatest_pro_decrease = change
                greatest_pro_decrease_date = row[0]
        previous_profit_loss = profit_loss

if profit_loss_change:
    average_change = sum(profit_loss_change) / len(profit_loss_change)

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_profit_loss}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_pro_increase_date, greatest_pro_increase}")
print(f"Greatest Decrease in Profits: {greatest_pro_decrease_date, greatest_pro_decrease}")

# Export a text file with the results
output_path = os.path.join("PyBank", "Resources", "pybank.txt")

with open('pybank.txt', "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("------------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: $ {net_profit_loss}\n")
    textfile.write(f"Average Change: $ {net_profit_loss}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_pro_increase_date} ($ {greatest_pro_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_pro_decrease_date} ($ {greatest_pro_decrease})\n")

