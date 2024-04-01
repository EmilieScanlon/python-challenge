import os
import csv
ballot_csv = os.path.join('Resources', 'election_data.csv')

# Lists to store data
ID = []
Candidate = []
Votecount = 1
Names = []
OrderNames=[]
VotebyName=[]
Votes = []
first = 1


with open(ballot_csv) as csvfile:
    ballot = csv.reader(csvfile, delimiter=",")
    next(ballot)
    #Enter sort of column 2 here
    for row in ballot:
        #add Candidates
        Candidate.append(row[2])
    Candidate.sort()
    for Names in Candidate:
        if Names != first:
            first = Names
            OrderNames.append(first)
            VotebyName.append(Votecount)
            Votecount = 0
        if Names == first:
            Votecount += 1
    VotebyName.append(Votecount)
        #calculate winning index
    for Counts in VotebyName:
        WinIndex = 0
        if VotebyName[0] > WinIndex:
            WinIndex = 0
        if VotebyName[1] > VotebyName[0]:
            WinIndex = 1
        if VotebyName[2] > VotebyName[1]:
            WinIndex = 2
        if VotebyName[3] > VotebyName[2]:
            WinIndex = 3
    


#Begin Prints
print("Election Results")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 

 #output total votes                
Votes=len(Candidate)

#print results by name
print("Total Votes: " + str(Votes))
print(OrderNames[0] + ": " + str(round(100*VotebyName[1] / len(Candidate),3)) + "%  " + 
"(" +str(VotebyName[1]) + ")")
print(OrderNames[1] + ": " + str(round(100*VotebyName[2] / len(Candidate),3)) + "%  " + 
"(" +str(VotebyName[2]) + ")")
print(OrderNames[2] + ": " + str(round(100*VotebyName[3] / len(Candidate),3)) + "%  " + 
"(" +str(VotebyName[3]) + ")")

#print winner
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Winner: " + str(OrderNames[int(WinIndex-1)]))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


###Print to txt file
f= open('output.txt','w')
print("Election Results",file=f)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",file=f) 

print("Total Votes: " + str(Votes))
print(OrderNames[0] + ": " + str(round(100*VotebyName[1] / len(Candidate),3)) + "%  " + 
"(" +str(VotebyName[1]) + ")",file=f)
print(OrderNames[1] + ": " + str(round(100*VotebyName[2] / len(Candidate),3)) + "%  " + 
"(" +str(VotebyName[2]) + ")",file=f)
print(OrderNames[2] + ": " + str(round(100*VotebyName[3] / len(Candidate),3)) + "%  " + 
"(" +str(VotebyName[3]) + ")",file=f)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",file=f)
print("Winner: " + str(OrderNames[int(WinIndex-1)]),file=f)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",file=f)



