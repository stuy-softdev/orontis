# Leon Wong
# Strawberry Shortcake
# SoftDev
# K17 -- Back in the (NY) Groove
# 2026-10-01r
# time spent: 2

import csv
import random

'''
DATA SANITIZATION:
Read the CSV using DictReader, strip() removes extra spaces
from the Devo and duckie names before putting them into the dictionary.
'''

def readFile(file):
    master_dict = {}

    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            devo = row['DEVO'].strip()
            duckie = row['DUCKIE'].strip()
            master_dict[devo] = duckie

    return master_dict


# sorts the dictionary of devos and their duckies
# alphabetically by the devo's name
def alphaSorter(master_dict):
    sorted_dict = dict(sorted(master_dict.items()))
    return sorted_dict


'''
SEPARATION CRITERIA AND APPROACH:
1. Sort all Devos alphabetically
2. Convert the dictionary into a list so it can be sliced
3. Divide the Devos into 3 tribes that are as equal as possible
4. If there is a remainder, the extra people go into the first tribes
5. Shuffle each tribe and create teams with one member from each tribe
6. If people are left over, put them into teams of 2
'''

def splitter(master_dict, tribeNum):
    copy = list(master_dict.items())

    groupSize = len(master_dict) // tribeNum
    remainder = len(master_dict) % tribeNum

    tribes = {}
    start = 0

    for i in range(tribeNum):
        currentSize = groupSize + (1 if i < remainder else 0)
        end = start + currentSize

        dictTribe = dict(copy[start:end])
        tribeName = f"tribe{i+1}"
        tribes[tribeName] = dictTribe

        start = end

    return tribes


# makes random teams using the three tribes
def teamMaker(tribes):
    tribe1 = list(tribes["tribe1"].items())
    tribe2 = list(tribes["tribe2"].items())
    tribe3 = list(tribes["tribe3"].items())

    random.shuffle(tribe1)
    random.shuffle(tribe2)
    random.shuffle(tribe3)

    total = len(tribe1) + len(tribe2) + len(tribe3)
    smallest = min(len(tribe1), len(tribe2), len(tribe3))

    # prevents one person from being left alone
    if total % 3 == 1:
        fullTeams = smallest - 1
    else:
        fullTeams = smallest

    teams = []

    # makes teams of 3, one person from each tribe
    for i in range(fullTeams):
        team = [
            tribe1[i],
            tribe2[i],
            tribe3[i]
        ]
        teams.append(team)

    # leftover people
    leftover1 = tribe1[fullTeams:]
    leftover2 = tribe2[fullTeams:]
    leftover3 = tribe3[fullTeams:]

    # if 4 people are left, make two teams of 2
    if len(leftover1) == 2:
        teams.append([leftover1[0], leftover2[0]])
        teams.append([leftover1[1], leftover3[0]])

    # if 2 people are left, make one team of 2
    elif len(leftover1) == 1 and len(leftover2) == 1:
        teams.append([leftover1[0], leftover2[0]])

    return teams

master_dict = readFile("handles_w_quackers.csv")
sorted_dict = alphaSorter(master_dict)

three_tribes = splitter(sorted_dict, 3)

print("SEPARATION CRITERIA:")
print("Devos are sorted alphabetically and split into 3 tribes that are as equal in size as possible")
print()

# prints the 3 tribes
for tribe in three_tribes:
    print(tribe)
    for devo, duckie in three_tribes[tribe].items():
        print(devo, ":", duckie)
    print()

# creates and prints random teams
random_teams = teamMaker(three_tribes)

print("RANDOM TEAMS")
print()

for i in range(len(random_teams)):
    print("Team", i + 1)
    for devo, duckie in random_teams[i]:
        print(devo, ":", duckie)
    print()