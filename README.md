# Election_Analysis
Election Analysis Assignment

## Overview of Project
    The project is to create a process that will evaluate and audit the election results using python to automate the process. Additionally in the process of creating the python process, there is an introduction to using Git Bast to copy and sync the updated files.

### Purpose
    The purpose of the project is to analyze the electionbased on: 
        1. The total number of votes
        2. The candidates running in the election
        3. The votes the candidates received
        4. The candidates' percentage of votes
        5. The winning candidate
        6. The voter turnout for each county
        7. The percentage of votes from each county out of the total count
        8. The county with the highest turnout
    These dimensions provide an opportunity to look deeper by segmentating the data and provide better expectations based on the election results data for the three counties provided.

## Analysis and Challenges
    The data provided good opportunities to segment the data across various dimensions.
    Analysis:
        1. There were a total number of votes of 369,711 base on a count of the number of records.
        2. The three county turnout results are: 
            Denver 82.8% (306,055), Jefferson 10.5% (38,855), and Arapahoe 6.7% (24,801).
        4. The election results are: 
            Diana DeGette 73.8% (272,892) (Winner), Charles Casper Stockham 23.0% (85,213), and Raymon Anthony Doane 3.1% (11,606)
        3. Link to the PyPoll.py python code to process the data file
            https://github.com/plymburner/Election_Analysis/blob/main/PyPoll.py
        4. Link to election_analysis text file:
            https://github.com/plymburner/Election_Analysis/blob/main/analysis/election_analysis.txt
        5. Screenshot of the outcome of the code ran in terminal
            https://github.com/plymburner/Election_Analysis/blob/main/analysis/election_analysis.png
            
    Challenges:
        1. The data in steps was setup exclusively with the candidate data and in order to proceed with the additional county based metrics, a list of the county data was established to conduct a count of the overall turnout and county turnout.
        2. The "County Votes:" header for the total turnout for the counties varies between the terminal output and the text file output where the character return in the screenshot yet that was not in the text file, resulting in the header and first county turnout result rendering on the same line.
        3. The additional folders for the for the Resources and Analysis, were problematic when adding the files to the Git Bash Add, commit and push processes. Eventually after adding the files and folders, I was able to push updated files into GitHub.


### Analysis of Outcomes Based on Election Results
    Outcomes:
        1. County Turnout
            - Determined the turnout counts and percentages by county as well as the county with the highest turnout.
                - Denver county has the majority of the voter turnout.
            - County Turnout
                -  Voter Turnout
                    Jefferson: 10.5% (38,855)
                    Denver: 82.8% (306,055)
                    Arapahoe: 6.7% (24,801)
                - Largest County Turnout
                    Denver
        2. Candidate Results
            - Determined the winning candidate, and each candidate's vote count and percentage of votes.
                - Diana DeGette won the majority of the vote in the election.
            - Election Results
                - Charles Casper Stockham: 23.0% (85,213)
                - Diana DeGette: 73.8% (272,892)
                - Raymon Anthony Doane: 3.1% (11,606)
            - Winning Results
                - Winner: Diana DeGette
                - Winning Vote Count: 272,892
                - Winning Percentage: 73.8%
        3. Overall
            - The counts matched the checked point values in the assignment and consistent with the number of rows in the spreadsheet
                - The number of votes were consistent for both the voter turnout and the number of votes the candidates received.
                - Total Votes: 369,711
    Link to Visual:
        https://github.com/plymburner/Election_Analysis/blob/main/analysis/election_analysis.png

### Analysis of Outcomes Based on Goals
    Outcomes:
        1. The total number of votes
            - The total turnout was consistent and determined by counting the number of records
        2. The candidates running in the election
            - The three candidates were entered into a dictionary based on the distinct names in the file
        3. The votes the candidates received
            - A count of the number of times the name appeared was appended to the dictionary for refernce
        4. The candidates' percentage of votes
            - The percentage of votes was determined by the number of candidate votes divided by the overall turnout and added to the dictionary
        5. The winning candidate
            - The candidate with the largest number of votes was then selected from the dictionary and used to pull the results for that candidate from the dictionary
        6. The voter turnout for each county
            - The distinct counties were added to a dictionary
            - A count of the counties by name was added to pull turnout
        7. The percentage of votes from each county out of the total count
            - Added the voter turnout divided by the overall turnout to include the percentage value to the dictionary.
        8. The county with the highest turnout
            - Selected the name of the county with the highest voter turnout
    Link to Code:
        https://github.com/plymburner/Election_Analysis/blob/main/PyPoll.py

### Challenges and Difficulties Encountered
    1. Text File Output
        - The header for the "County Votes:" section didn't render with it on a separate line as it did in the terminal output
    2. Git Bash push into GitHub
        - Without a 100% match in structure and files there were errors in the process and were only remedied once the folder and the online repository were structured in a similar manner.

## Results

    - What are two conclusions you can draw about the outcome of the election?
        1. Denver county had a significantly higher turnout than the other two counties in the election data.
        2. One candidate, Diana DeGette, received nearly three-quarters of the votes in those three counties.

    - What can you conclude about the Outcomes based on Goals?
        1. The OS functions allowed for the import of data and the creation of and output file to the file folder. 
            - There is an overlap of functionality between OS functions and Git Bash to create and manage files and directories on the local computer. 
        2. Voter turnout and counting votes were similar processes with separate dictionaries to retain the result data.

    - What are some limitations of this dataset?
        1.  Without the office to group the data there wouldn't be a way to segment the results for additional races when using the code in wider use cases with multiple 
        2. There were not null or N/A values in the data that would represent ballot errors (i.e. voting for more than one person when not allowed) or skipped races 
        3. The premise for the assignment was for a winner takes all election, while there are races where the top N candidates win office.

    - What are some other possible tables and/or graphs that we could create?
        1. Graphs
            - Stacked bar for outcomes based on the number of votes for either by county or candidate
            - Pie chart of the percentages of the votes by either counth or candidate
            - Further subdivide the data into the votes for each candidate by county or county by candidate in a stacked bar by percentage, which would provide which candidate had the most support in a given county, not withstanding the winner of the plurality of the vote.
