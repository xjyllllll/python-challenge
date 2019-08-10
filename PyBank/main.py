import os
import csv


# file path
filepath = "C:/Users/XJY/Desktop/COLNYC20190716DATA-master/02-Homeworks/03-Python/Instructions/PyBank/Resources/budget_data.csv"
pathout = "C:/Users/XJY/Desktop/COLNYC20190716DATA-master/02-Homeworks/03-Python/Instructions/PyBank/resources/budget_analysis.txt"
total_month = 0
total_revenue = 0
pre_revenue = 0 
revenue_change = 0
Diff = 0 
DiffMax = 0 
DiffMin = 0

#Open and read CSV file
with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - pre_revenue
         revenue_change = revenue_change + Diff
         #Placeholder to track greatest increase in profits
         if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month
         #Placeholder to track greatest decrease in profits 
         if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month

         pre_revenue = iAmount   
         # Get total months 
         total_month = total_month + 1
         total_revenue += int(Amount)

         

average = revenue_change / total_month

#Results    
print('Financial Analysis')
print('----------------------------')
print(f'Total Months : {total_month}')
print(f'Total: $ {total_revenue}')
print(f'Average Change : $ {average}')
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')
print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')

# output files
with open(pathout, "w") as txt_file:

   txt_file.write('Financial Analysis')
   txt_file.write('----------------------------')
   txt_file.write(f'Total Months : {total_month}')
   txt_file.write(f'Total: $ {total_revenue}')
   txt_file.write(f'Average Change : $ {average}')
   txt_file.write(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')
   txt_file.write(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')