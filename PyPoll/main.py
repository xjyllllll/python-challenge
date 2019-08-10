import csv
import os

#file path
csvpath = "C:/Users/XJY/Desktop/COLNYC20190716DATA-master/02-Homeworks/03-Python/Instructions/PyPoll/resources/election_data.csv"
pathout = "C:/Users/XJY/Desktop/COLNYC20190716DATA-master/02-Homeworks/03-Python/Instructions/PyPoll/resources/election_analysis.txt"
total_count = 0; khan_count = 0; correy_count = 0; li_count = 0; otooley_count = 0; max_votecount = 0


#read CSV file
with open(csvpath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')

     for i in csvreader:
         voterid = i[0]
         country = i[1]
         candidate = i[2]
         total_count = total_count + 1

         
         if candidate =="Khan":
            khan_count = khan_count + 1
         if candidate =="Correy":
            correy_count = correy_count + 1
         if candidate =="Li":
            li_count = li_count + 1
         if candidate =="O'Tooley":
            otooley_count = otooley_count + 1
            
# Define (dictionary) list : candidate and votes
     candidatevote = {"Khan": khan_count,"Correy": correy_count,"Li" :li_count, "O'Tooley": otooley_count}
     # Find winner 
     for candidate, value in candidatevote.items():
         if value > max_votecount:
            max_votecount = value
            winner = candidate

#Function for % calculation
def percentage (part, whole):
    return 100 * float(part)/float(whole)

# Display results       
print('Election Results')
print("-------------------------------------")
print(f'Total Votes: {total_count}'+'\n')
print("-------------------------------------")
print(f'Khan: {percentage(khan_count,total_count):.2f}%  ({khan_count})')
print(f'Correy: {percentage(correy_count,total_count):.2f}%  ({correy_count})')
print(f'Li: {percentage(li_count,total_count):.2f}%  ({li_count})')
print(f'O\'Tooley: {percentage(otooley_count,total_count):.2f}%  ({otooley_count})')
print(f'--------------------------------'+'\n')
print(f'Winner: {winner} '+'\n')
print(f'--------------------------------'+'\n')

# output files
with open (pathout, "w") as txt_file:

    txt_file.write("Election Results")
    txt_file.write("-------------------------------------")
    txt_file.write(f'Total Votes: {total_count}'+'\n')
    txt_file.write("-------------------------------------")
    txt_file.write(f'Khan: {percentage(khan_count,total_count):.2f}%  ({khan_count})')
    txt_file.write(f'Correy: {percentage(correy_count,total_count):.2f}%  ({correy_count})')
    txt_file.write(f'Li: {percentage(li_count,total_count):.2f}%  ({li_count})')
    txt_file.write(f'O\'Tooley: {percentage(otooley_count,total_count):.2f}%  ({otooley_count})')
    txt_file.write(f'--------------------------------'+'\n')
    txt_file.write(f'Winner: {winner} '+'\n')
    txt_file.write(f'--------------------------------'+'\n')