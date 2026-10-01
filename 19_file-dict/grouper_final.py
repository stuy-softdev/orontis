# Leon Wong
# Strawberry Shortcake
# SoftDev
# K19 -- Bring It Back Home
# 2026-10-02f
# time spent: 1.0

import csv
import random


# DANK JE WEL DEVO FAM Darren|Triple T Trio
# cleans data read from the csv
def sanitize(text):
    if text == None:
        return ""

    text = text.strip()
    text = text.replace('"', '')
    text = text.replace('“', '')
    text = text.replace('”', '')
    text = text.replace(';', '')

    return text


'''
CSV MODULE / DATA SANITIZATION:

DictReader reads every row of the CSV as a dictionary. The column
headers DEVO and DUCKIE become keys, so values can be accessed with
row["DEVO"] and row["DUCKIE"] instead of manually splitting lines.

Each Devo and duckie is passed through sanitize(), which removes
extra spaces and unwanted characters before the values are stored.

DictWriter writes the cleaned dictionary into handles_w_quackers.csv.
fieldnames determines the DEVO and DUCKIE columns, writeheader()
writes the column headings, and writerow() writes each cleaned pair.
'''


def readFile(file):
    master_dict = {}

    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            devo = sanitize(row['DEVO'])
            duckie = sanitize(row['DUCKIE'])

            # DANK JE WEL DEVO FAM Darren|Triple T Trio
            # handles missing Devo or duckie values
            if devo == "":
                devo = "NO_DEV"

            if duckie == "":
                duckie = "NO_DUCK"

            # handles duplicate Devo names so they do not overwrite
            # previous entries in the dictionary
            if devo in master_dict:
                number = 2
                newDevo = devo + str(number)

                while newDevo in master_dict:
                    number += 1
                    newDevo = devo + str(number)

                devo = newDevo

            master_dict[devo] = duckie

    return master_dict


# writes the cleaned data into a csv file
def writeFile(file, master_dict):
    with open(file, "w", newline='', encoding='utf-8') as csvfile:
        fieldnames = ["DEVO", "DUCKIE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for devo, duckie in master_dict.items():
            writer.writerow({
                "DEVO": devo,
                "DUCKIE": duckie
            })


# sorts the dictionary alphabetically by Devo name
def alphaSorter(master_dict):
    sorted_dict = dict(sorted(master_dict.items()))
    return sorted_dict


'''
SEPARATION CRITERIA AND APPROACH:

1. Sort all Devos alphabetically
2. Convert the dictionary into a list
3. Distribute every third Devo into the same tribe
4. This creates 3 tribes that are as equal in size as possible
5. Shuffle the members inside each tribe
6. Create teams with one person from each tribe when possible
7. If the last team has only one person, move somebody from the
   previous team so nobody is left alone
'''


# DANK JE WEL DEVO FAM Saxon|Devo Trio
# distributes every nth entry into the same tribe instead of
# cutting the sorted list into three separate alphabetical sections
def splitter(master_dict, tribeNum):
    entries = list(master_dict.items())

    tribes = {}

    for i in range(tribeNum):
        tribeEntries = entries[i::tribeNum]
        tribeName = f"tribe{i+1}"
        tribes[tribeName] = dict(tribeEntries)

    return tribes


# DANK JE WEL DEVO FAM Josiah|We Need More Time
# builds each team by checking the same position in every tribe
# and only adding a member if that tribe has somebody at that index
def teamMaker(tribes):
    tribe1 = list(tribes["tribe1"].items())
    tribe2 = list(tribes["tribe2"].items())
    tribe3 = list(tribes["tribe3"].items())

    random.shuffle(tribe1)
    random.shuffle(tribe2)
    random.shuffle(tribe3)

    teams = []

    largest = max(
        len(tribe1),
        len(tribe2),
        len(tribe3)
    )

    for i in range(largest):
        team = []

        if i < len(tribe1):
            team.append(tribe1[i])

        if i < len(tribe2):
            team.append(tribe2[i])

        if i < len(tribe3):
            team.append(tribe3[i])

        teams.append(team)

    # prevents a final team of only one person
    if len(teams) > 1 and len(teams[-1]) == 1:
        movedPerson = teams[-2].pop()
        teams[-1].append(movedPerson)

    return teams


# reads and sanitizes the dirty csv
master_dict = readFile("handles_w_quackers-dirty.csv")

# writes the sanitized data into the clean csv
writeFile("handles_w_quackers.csv", master_dict)

# sorts Devo names alphabetically
sorted_dict = alphaSorter(master_dict)

# splits the Devos into three tribes
three_tribes = splitter(sorted_dict, 3)


print("SEPARATION CRITERIA:")
print("Devos are sorted alphabetically, then distributed evenly across 3 tribes")
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