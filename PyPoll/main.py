# import modules 
import csv
import os

# source to read budget data file
budget_path = os.path.join('Resources', "election_data.csv")

#output file
outputFile = os.path.join('analysis', "election_analysis.txt")


total_votes= 0
election_results = {}
elec_candidate_result =""
winner_percent=0.0
winner_candidate=""

with open(budget_path) as budget_data:
    #create a csv reader object 
    csvreader = csv.reader(budget_data)
    header = next(csvreader)

    for row  in csvreader:
        total_votes += 1
        
        # check to see if candidate key exists
        if  election_results.get(row[2]) == None:
            election_results[row[2]] = 1
        else:
            candidate_result = election_results.get(row[2])
            election_results[row[2]] = candidate_result + 1

# loop through candidate election results
for candidate in election_results:
    total_candidate_votes = election_results[candidate]
    percent_votes = (total_candidate_votes/total_votes) *100
    elec_candidate_result +=  f"{candidate}: {round(percent_votes,3)}% ({total_candidate_votes})\n"
    if winner_percent < percent_votes:
        winner_percent = percent_votes
        winner_candidate = candidate

output = (
    f"\nElection Results\n"
    "------------------------\n"
    f"Total Votes: {total_votes}\n"
    "------------------------\n"
    f"{elec_candidate_result}\n"
    "------------------------\n"
    f"Winner: {winner_candidate}\n"
    "------------------------\n"
)

print(output)


# Export to analysis file
with open(outputFile,"w") as textFile:
    textFile.write(output)
