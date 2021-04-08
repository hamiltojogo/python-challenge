# write a python script that analyzes the votes and calculates
# total number of votes cast
# complete list of candidates who received votes
# percentage of votes each candidate won
# total number of votes each candidate won
# winner of the election based on popular vote
# print the analysis to the terminal and export a text file


#import required modules 
import os
import csv


#set path for file 

csvpath = os.path.join("Resources", "election_data.csv")


#variables

CorreyCount = 0
KhanCount = 0
LiCount = 0
TooleyCount = 0
TotalVote = 0
CandidatesList = []


#open csv file 

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #skip the headers
    next(csvreader, None)
    
    #creating loop to move through the data
    
    for row in csvreader:
    
        #Tallying votes
        
        TotalVote = TotalVote + 1
        
        if row[2] == "Correy":
            CorreyCount = CorreyCount + 1
        
        if row[2] == "Khan":
            KhanCount = KhanCount + 1
            
        if row[2] == "Li":
            LiCount = LiCount + 1
            
        if row[2] == "O'Tooley":
            TooleyCount = TooleyCount + 1
            
    # Create Candidate List
    if KhanCount > 0:
        CandidatesList.append("Khan")
    
    if LiCount > 0:
        CandidatesList.append("Li")
    
    if CorreyCount > 0:
        CandidatesList.append("Correy")
    
    if TooleyCount > 0:
        CandidatesList.append("O'Tooley")
        
    #Find the winner
    
    if KhanCount > LiCount:
        Winner = "Khan"
        WinnerCount = KhanCount
    else:
        Winner = "Li"
        WinnerCount = LiCount
        
    if WinnerCount > CorreyCount:
        Winner = Winner
        WinnerCount = WinnerCount
    else:
        Winner = Correy
        WinnerCount = CorreyCount
        
    if WinnerCount > TooleyCount:
        Winner = Winner
        WinnerCount = WinnerCount
    else:
        Winner = "O'Tooley"
        WinnerCount = TooleyCount
    
    # Vote percentage
    
    CorreyPercent = int((CorreyCount / TotalVote) * 100)
    KhanPercent = int((KhanCount / TotalVote) * 100)
    LiPercent = int((LiCount / TotalVote) * 100)
    TooleyPercent = int((TooleyCount / TotalVote) * 100)
    
#print results in terminal

print("Election Results")
print("--------------------------------------------")
print("Total Votes: " + str(TotalVote))
print("--------------------------------------------")
print(CandidatesList[0]+ ": " + str(KhanPercent) + "% (" + str(KhanCount) + ")")
print(CandidatesList[2]+ ": " + str(CorreyPercent) + "% (" + str(CorreyCount) + ")")
print(CandidatesList[1]+ ": " + str(LiPercent) + "% (" + str(LiCount) + ")")
print(CandidatesList[3]+ ": " + str(TooleyPercent) + "% (" + str(TooleyCount) + ")")
print("--------------------------------------------")
print("Winner: " + Winner) 
print("--------------------------------------------")
    


os.mkdir("Analysis")

txtpath = os.path.join('Analysis', "PollAnalysis.txt")

#write results to text file
Line1 = "Election Results"
Line2 = "Total Votes: " + str(TotalVote)
Line3 = CandidatesList[0]+ ": " + str(KhanPercent) + "% (" + str(KhanCount) + ")"
Line4 = CandidatesList[2]+ ": " + str(CorreyPercent) + "% (" + str(CorreyCount) + ")"
Line5 = CandidatesList[1]+ ": " + str(LiPercent) + "% (" + str(LiCount) + ")"
Line6 = CandidatesList[3]+ ": " + str(TooleyPercent) + "% (" + str(TooleyCount) + ")"
Line7 = "Winner: " + Winner

textlist = [Line1, Line2, Line3, Line4, Line5, Line6, Line7]

outF = open(txtpath,"w")
for line in textlist:
    outF.write(line)
    outF.write("\n")
outF.close()


