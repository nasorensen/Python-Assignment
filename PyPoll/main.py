# Import necessary modules
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
vote_count = {}
winner = None
winner_count = 0
# Winning Candidate and Winning Count Tracker

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter=',')

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        candidates.append(candidate)

        # Add a vote to the candidate's count
        if candidate in vote_count:
            vote_count[candidate] += 1
        else:
            vote_count[candidate] = 1

        # Get the vote count and calculate the percentage
    vote_percents = {candidate: (vote_count / total_votes) * 100 for candidate, vote_count in vote_count.items()}

        # Update the winning candidate if this one has more votes
    for candidate, votes in vote_count.items():
        if votes > winner_count:
            winner_count = votes
            winner = candidate

    # Print Results in Terminal

    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------")
    for candidate, votes in vote_count.items():
        print(f"{candidate}: {round(vote_percents[candidate], 2)}% ({vote_count[candidate]})")
    print("---------------------------")
    print("The winner is " + winner)

    # Open a text file to save the output

output = ["Election Results", 
        "---------------------------", 
        f"Total Votes: {total_votes}", 
        "---------------------------", 
        "The winner is " + winner, 
        "---------------------------" 
]
with open(file_to_output, "w") as txt_file:
    txt_file.write(str(output))
    for candidate, votes in vote_count.items():
        txt_file.write(f"{candidate}: {round(vote_percents[candidate], 2)}% ({vote_count[candidate]})") 




    