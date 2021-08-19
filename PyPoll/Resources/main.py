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

#print
print(f"Results")
print(f"----------------")
print(f"Total Votes: {voteTotal}")
print(f"----------------")
for key, value in votes.items():
    print(f"{key}: {value / voteTotal:.3%} ({value})")
print(f"-------------------------")
print(f"Winner: {max(votes, key=votes.get)}")
print(f"-------------------------")

#output the same results to a text file
output_path = os.path.join("..", "analysis", "Election_Results.txt")
with open(output_path, "w", newline='') as datafile:
    datafile.write(
    f"Election_Results\n"
    f"-------------------------\n"
    f"Total Votes: {voteTotal}\n"
    f"-------------------------\n")
    for key, value in votes.items():
        datafile.write(f"{key}: {value / voteTotal:.3%} ({value})\n")
    datafile.write(f"-----------------\n"
    f"Winner: {max(votes, key=votes.get)}\n"
    f"--------------")
