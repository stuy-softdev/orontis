# Leon Wong
# Strawberry Shortcake
# SoftDev
# K17 -- Back in the (NY) Groove
# 2026-10-01r
# time spent: 2

import math
import csv

# sanitize data with .strip()
def readFile(file):
    master_dict = {}
    with open(file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            devo = row['DEVO'].strip()
            duckie = row['DUCKIE'].strip()
            master_dict[devo] = duckie
    return master_dict

# sorts the dictionary of devos and their duckies by the devo's names alphanumerically
def alphaSorter(master_dict):
    sorted_dict = dict(sorted(master_dict.items()))
    return sorted_dict
'''
splitter
1. convert master_dict into a list 'copy' so to take stuff from it and slice it.
2. find groupSize and the remainder of people who won't fit.
3. for each team, find the size of the group (+ 1 if there is a remainder)
4. convert copy into a dict by chunks determined by the start and end indices determined by groupSize.
'''
def splitter(master_dict, teamNum):
    copy = list(master_dict.items())
    groupSize = len(master_dict) // teamNum
    remainder = len(master_dict) % teamNum
    
    teams = {}
    start = 0
    
    for i in range(teamNum):
        currentSize = groupSize + (1 if i < remainder else 0)
        end = start + currentSize
        
        dictTeam = dict(copy[start:end])
        teamName = f"team{i+1}"
        teams[teamName] = dictTeam
        
        start = end
        
    return teams

three_teams = splitter(alphaSorter(readFile("handles_w_quackers.csv")), 3)
print(three_teams)