import csv
import random
from flask import Flask

"""
Duo: Lucas Ou, Leon Wong

Approach:
Parse CSV file with DictReader and store a list of dictionaries in a variable.
Then write function that gets a random job from this list and route it to flask. 
This function first generates a random number from 0 to TOTAL percentage (near 100), 
then uses a counter to add up each individual job percentage to check which job the random number landed on.
"""

app = Flask(__name__)

def getJobsFromCSV(filename):
    """Gets a list of jobs and their percentage from a CSV file.

    The CSV should be in a specific format, with the job entry "Total" as the last line, which is meant to hold the total percentage by adding all of the other job percentages.

    Args:
        filename: The name of the CSV file

    Returns:
        A list of dictionaries for each job, with keys 'Job Class' and 'Percentage' for each.
    """
    temp = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['Percentage'] = float(row['Percentage'])
            temp.append(row)
    return temp

# global variable jobs so that getRandomJob() can access it
# not sure how to be able to pass a parameter to a function and route it at the same time...
jobs = getJobsFromCSV("occupations.csv")

@app.route("/")
def getRandomJob():
    """Gets a random job given a array of jobs

    The array should be in a specific format, with each job represented by a dictionary with keys 'Job Class' and 'Percentage' for each.
    The last element of the array should also contain a 'Job Class' of 'Total', which has 'Percentage' storing the total percentage of all jobs.

    Args:
        jobs: The array

    Returns:
        A string contining the chosen job name
    """

    # Using random.choices()
    # jobs = [job['Job Class'] for job in l]
    # weights = [job['Percentage'] for job in l]
    # return random.choices(jobs, weights)
    
    # Manually
    chosenNum = random.random() * jobs[-1]['Percentage'] # Get random number scaled by the total percentage
    percentageWheel = 0.0 # To find which job our chosenNum has landed on.
    i = 0 # index
    while (percentageWheel < chosenNum):
        percentageWheel += jobs[i]['Percentage']
        i += 1
    # We return jobs[i-1] becuase of the i+=1 on the last line... 
    # the occupation that is compared for each while loop is the previous one before we peform the next jobs[i]['Percentage']
    return jobs[i-1]['Job Class'] 

if __name__ == "__main__":
    app.debug = True
    app.run()