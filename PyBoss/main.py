# Create a Python script able to convert your employee records to the required format
# Name column should be split into separate First Name and Last Name columns
# DOB data should be re-written into MM/DD/YYYY format
# SSN data should be re-written as ***-**-####
# State data should be re-written as simple two-letter abbreviations


#import required modules 
import os
import csv
import datetime


# State dictionary from us_state_abbrev.py

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


#set path for file 

csvpath = os.path.join("Resources", "employee_data.csv")


#Variables

ID = []
First = []
Last = []
DOB = []
SSN = []
State = []


#open csv file 

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #skip the headers
    next(csvreader, None)
    
    #creating loop to move through the data
    
    for row in csvreader:
    
        #add employee id 
        ID.append(row[0])
        
        #split name into first and last
        FirstName,LastName = row[1].split(" ")
        
        #add first name 
        First.append(FirstName)
        #add last name 
        Last.append(LastName)
        
        #change date format and add to list
        #formated_date = datetime.datetime.strptime(row[2],"%y-%m-%d")
        #DOB.append(formated_date)
        
        Y,M,D = row[2].split("-")
        
        DOB.append(M + "/" + D + "/" + Y)
        
        #split social security number, change format, and add to list
        SS1,SS2,SS3 = row[3].split("-")
        SSN.append("***-**-" + SS3)
        
        #add state
        
        abbreviation = us_state_abbrev[row[4]]
        
        State.append(abbreviation)
    
    
    #compile new data 
    
#New_Employee_Data_List = [ID, First, Last, DOB, SSN, State]

New_Employee_Data_List = zip(ID, First, Last, DOB, SSN, State)
    

#write results to text file
os.mkdir("output")

outpath = os.path.join('output', "New_Employee_Data.csv")    

#file = open(outpath, 'w', newline ='')
    
with open(outpath, "w", newline ="") as csvfile:
    
    header = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
    
    csvwriter = csv.writer(csvfile, delimiter = ",")
    
    csvwriter.writerow(header)
    
    csvwriter.writerows(New_Employee_Data_List)
    
   
    


