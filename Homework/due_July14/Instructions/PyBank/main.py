# import budget data csv
import os
import csv

# file_path = os.path.join( "PyBank", "Resources", "budget_data.csv")
file_path = "nu homework/python-challenge/Homework/due_July14/Instructions/PyBank/Resources/budget_data.csv"

with open(file_path) as budget_file:
    csv_reader = csv.reader(budget_file, delimiter=',')


# Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    money = []
    
    for row in csv_reader:
        money.append(row)

# count total number of months in data set
len(money)
number_months= len(money)
 
#net total amount of profit and losses per year
    # sum entire column
profit = 0

for line in money:
    profit = profit + int(line[1])
print(profit)

# calcuate the avg. profit/loss over the entire time
avg = profit / number_months
print(avg)
# need to get the greatest increase in profits
max_inc = 0
for inc in money:
    max_inc = max_inc + int(line[1])
print(max_inc)

# need to get the biggest lost in profits
max_dec = 0
for dec in money:
    max_dec = max_dec = int(line[1])
print(max_dec)


#export analysis into text file--done at the end 

