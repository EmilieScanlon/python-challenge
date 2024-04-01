import os
import csv
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Lists to store data
date = []
profit = []
total=0
count=0
maxchange = 0
minchange = 0
before = 0 


with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    count = 0
    for row in csvreader:
        first = row[1]
        count = count + 1
        if count == 1:
            break

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        #add date
        date.append(row[0])
        #add profit
        profit.append(row[1])
        #calculate number of Months
        Months=len(date)
        #find sum of profit
        total += int(row[1])
        #Find the last profit for change calculation
        last=row[1]
        change=int(row[1]) - before
        before=int(row[1])
        if maxchange < change:
            maxchange = change
        if minchange > change:
            minchange = change
    

    

#Total Months calc plus output
Months=len(date)
print("Total Months: " + str(Months))
        
#Print Total Profit/Losses
print("Total : $" + str(total))

#Find change of profit [last  - first]
change = int(last) - int(first)
#Find Average change of profit 
average = round(int(change) / int(Months-1),2)
#Print Average Profit/Losses
print("Average Change: $" + str(average))
#Print the maximum change
print("Greatest Increase in Profits: $" + str(maxchange))
#Print the mininum change
print("Greatest Decrease in Profits: $" + str(minchange))


###Print to txt file
f= open('output.txt','w')
print("Total Months: " + str(Months),file=f)      
#Print Total Profit/Losses
print("Total : $" + str(total),file=f)
#Print Average Profit/Losses
print("Average Change: $" + str(average),file=f)
#Print the maximum change
print("Greatest Increase in Profits: $" + str(maxchange),file=f)
#Print the mininum change
print("Greatest Decrease in Profits: $" + str(minchange),file=f)
