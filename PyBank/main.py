#Pythong script that analyyzes bank records to calculate:

#Total number of months in data set
#Caculate the changes in profit/losses over the entire period
#Capture the date and amount of the greatest increase (profit)
#Capture the date and amount of the greatest decrease (losses)

#Final script should print the analysis to the termine and export a text file of the results 




#import required modules 
import os
import csv


#set path for file 

csvpath = os.path.join("Resources", "budget_data.csv")


#variables

MonthCount = 0
GreatestIncrease = 0
GreatestDecrease = 0
Profit_Losses_List = []
PreviousProfit = 867884


#open csv file 

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    next(csvreader, None)
    
    #creating loop to move through the data
    
    ChangeList = []
    
    for row in csvreader:
        
        #Calculate total months,add profit/loss to list for later calculations, monthly change
        
        MonthCount = MonthCount + 1
            
        ChangeList.append(row[1])
        
        MonthlyChange = (int(row[1]) - PreviousProfit)
        
        #find greatest increase and decrease dates and values
        
        if MonthlyChange > GreatestIncrease:
        
            GreatestIncrease = MonthlyChange
            IncreaseDate = row[0]
            Profit_Losses_List.append(IncreaseDate)
            Profit_Losses_List.append(GreatestIncrease)
            
            
        if MonthlyChange < GreatestDecrease:
        
            GreatestDecrease = MonthlyChange
            DecreaseDate = row[0]
            Profit_Losses_List.append(DecreaseDate)
            Profit_Losses_List.append(GreatestDecrease)
            
        PreviousProfit = int(row[1])
 
#calculate the average profit/losses


NetChange = int(ChangeList[-1]) - int(ChangeList[0])

Average = int(NetChange/(MonthCount-1))


#print Results

print("Financial Analysis")
print( "---------------------------------")
print("TotalMonths: " + str(MonthCount)) 
print("Average Change: $" + str(Average))
print("The month of greatest increase is " + str(IncreaseDate) + " with $" + str(GreatestIncrease))
print("The month of greatest decrease is " + str(DecreaseDate) + " with $" + str(GreatestDecrease))

#write results to text file
os.mkdir("Analysis")

txtpath = os.path.join('Analysis', "FinancialAnalysis.txt")


Line1 = "Financial Analysis"
Line2 = "TotalMonths: " + str(MonthCount)
Line3 = "Average Change: $" + str(Average)
Line4 = "The month of greatest increase is " + str(IncreaseDate) + " with $" + str(GreatestIncrease)
Line5 = "The month of greatest decrease is " + str(DecreaseDate) + " with $" + str(GreatestDecrease)


textlist = [Line1, Line2, Line3, Line4, Line5]

outF = open(txtpath,"w")
for line in textlist:
    outF.write(line)
    outF.write("\n")
outF.close()

