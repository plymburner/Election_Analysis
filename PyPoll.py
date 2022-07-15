# The data we need to retrive.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# County options and County votes.
county_options = []
county_votes = {}

# Track the highest turnout percentage.
turnout_highest = ""
turnout_percentage = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:

        #1. The total number of votes cast
        # Add to the total vote count.
        total_votes += 1

        # Get the county name from each row.
        county = row[1]

        # If the county does not match any existing county, add the
        # the county list.
        if county not in county_options:

            # Add the candidate name to the candidate list.
            county_options.append(county)

            # And begin tracking that candidate's voter count.
            county_votes[county] = 0

        # Add a vote to that county's count.
        county_votes[county] += 1

        #2. A complete list of candidates who received votes
        # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        #4. The total number of votes each candidate won
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    # Print the winning candidate's results to the terminal.
    result_header = ("County Votes:")
    print(result_header)

 #  Save the county results header to our text file.
    txt_file.write(result_header)        

    for county in county_votes:

        # Retrieve vote count and percentage.
        votes = county_votes[county]

        # The percentage of votes each county
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each county's voter count and percentage to the terminal.
        print(county_results)

        #  Save the county results to our text file.
        txt_file.write(county_results)

    # Determine highest turnout county.
    county_turnout = max(county_votes, key = county_votes.get)
  
    # Print the winning candidate's results to the terminal.
    largest_turnout = (
        f"-------------------------\n"
        f"Largest County Turnout:  {county_turnout}\n"
        f"-------------------------\n")
    print(largest_turnout)

    # Save the winning candidate's results to the text file.
    txt_file.write(largest_turnout)

    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]

        #3. The percentage of votes each candidate won
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        #5. The winner of the election base on popular vote
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)