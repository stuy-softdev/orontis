import csv
import random
from flask import Flask, render_template

# Leon Wong, Lucas Ou
# GOD BLESS AMERICA
# SoftDev
# K26 -- Template for Success
# 2026-10-13
# Time Spent: 2

app = Flask(__name__)

'''
APPROACH:
We modified occupations.csv to include an Info column containing a URL for each occupation.

We use csv.DictReader() to read the CSV into a list of dictionaries. Each dictionary stores the job name, percentage, and URL.

We convert percentages into floats so they can be used for random job selection.

We then pass the list of dictionaries to our Jinja template, which generates an HTML table displaying the occupations, percentages, and links.
'''

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
jobList = getJobsFromCSV("data/occupations.csv")

def getRandomJob(jobs):
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

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

@app.route("/wdywtbwygu")
def wdywtbwygu():
    return render_template( 'tablified.html', job=getRandomJob(jobList), collection=jobList)

if __name__ == "__main__":
    app.debug = True
    app.run()
