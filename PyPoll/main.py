import os
import csv

# Define file path
csvpath = os.path.join("/Users/jenzapata/Downloads/Starter_Code/PyPoll/Resources/election_data.csv")
output_file = "election_results.txt"

# Declare variables
total_votes_cast = 0
candidate_votes = {}
total_votes_candidates = {}

# Open CSV file
with open(csvpath) as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',')
    next(csv_read)
    
    # Loop through to find total votes
    for row in csv_read:
        total_votes_cast += 1
       
        candidate_name = row[2]
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1
winner_candidate = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes_cast}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage_votes = (votes / total_votes_cast) * 100
    total_votes_candidates[candidate] = votes
    print(f"{candidate}: {percentage_votes:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner_candidate}")
print("-------------------------")
print("Total Votes Each Candidate Won:")
for candidate, total_votes in total_votes_candidates.items():
    print(f"{candidate}: {total_votes}")


# Write results to file
with open(output_file, 'w') as file:

    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total votes: {total_votes_cast}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage_votes = (votes / total_votes_cast) * 100
        total_votes_candidates[candidate] = votes
        file.write(f"{candidate}: {percentage_votes:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner_candidate}\n")
    file.write("-------------------------\n")
    file.write("Totoal votes Each candidate won:\n")
    for candidate, total_votes in total_votes_candidates.items():
        file.write(f"{candidate}: {total_votes}\n")
