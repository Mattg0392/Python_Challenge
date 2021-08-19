# Analyze election data
import os
import csv
#set local path to csv file
election_csv = os.path.join("..", "..", "election_data.csv")
#create dic
votes = {}
#read csv
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        candidate = row[2]
        #if unique candidate add it, if it does exist, add vote.
        if candidate not in votes:
            votes[candidate] = 1
        else:
            votes[candidate] += 1

#establish dictionary keys
values = votes.values()
voteTotal = sum(values)
#output vote total

