# -*- coding: UTF-8 -*-

# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# More variables to track other necessary financial data
profit = []
previous_profit = None
max_increase = 0 
max_increase_row = None
max_decrease = 0
max_decrease_row = None

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=',')

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:

        # Track the total
       total_months += 1
       total = int(row[1])
       total_net += total
       
        # Track the net change 
       change = int(row[1])
       profit.append(change)

        # Calculate the greatest increase and decrease in profits (month and amount)
       current_profit = int(row[1])
       if previous_profit is not None:
            increase = current_profit - previous_profit
            decrease = previous_profit - current_profit
            if increase > max_increase:
                max_increase = increase
                max_increase_row = str(row[0])
            if decrease > max_decrease:
                max_decrease = decrease
                max_decrease_row = str(row[0])
       previous_profit = current_profit

# Calculate the average net change across the months
profit_changes = [profit[i] - profit [i-1] for i in range(1, len(profit))]
average_change = sum(profit_changes) / len(profit_changes) if profit_changes else 0
formatted_average_change = "{:.2f}".format(average_change)

# Generate the output summary
output = [
"Financial Analysis  " 
f"Total Months: {str(total_months)},  "
f"Total: ${str(total_net)},  "
f"Average Change: ${str(formatted_average_change)},  "
f"Greatest Increase in Profits: {max_increase_row} (${max_increase}),  "
f"Greatest Decrease in Profits: {max_decrease_row} ($-{max_decrease}),  "
]

# Print the output
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_net)}")
print(f"Average Change: ${str(formatted_average_change)}")
print(f"Greatest Increase in Profits: {max_increase_row} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_row} ($-{max_decrease})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(str(output)) 
