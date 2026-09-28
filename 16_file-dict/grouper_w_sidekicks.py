import random
devo_duckies = {}

"""
DATA SANITIZATION:
The program reads the CSV file line by line. Empty lines are ignored.
Each non-empty line is split at the comma into a Devo handle and a ducky.
.strip() removes any extra spaces from both values before they are stored
as a Devo:Ducky key-value pair in the dictionary.
"""

with open("handles_w_quackers.csv", "r") as file:
    lines = file.read().split("\n")
    for line in lines:
        if line != "":
            parts = line.split(",")
            devo = parts[0].strip()
            duck = parts[1].strip()
            devo_duckies[devo] = duck
            
"""
SEPARATION CRITERIA AND APPROACH:
The Devo handles are sorted from shortest to longest by number of characters.
They are then divided into three tribes that are as equal in size as possible.
If the total number of Devos is not divisible by 3, the extra one or two
people are placed into the first and second tribes.

After the tribes are created, the order of the Devos inside each tribe is
randomized. Teams are then created using at most one Devo from each tribe.
If the total number of Devos does not divide evenly into teams of three,
the remaining Devos are placed into one or two teams of two.
"""

# Get all Devo handles from dictionary
handles = list(devo_duckies.keys())

# Sort handles by length
handles.sort(key=len)

tribe_len = len(handles) // 3
remainder = len(handles) % 3

# Determine tribe sizes
if remainder == 0:
    size_1 = tribe_len
    size_2 = tribe_len
    size_3 = tribe_len
elif remainder == 1:
    size_1 = tribe_len + 1
    size_2 = tribe_len
    size_3 = tribe_len
else:
    size_1 = tribe_len + 1
    size_2 = tribe_len + 1
    size_3 = tribe_len
    
# Split handles into the three groups
group_1 = handles[:size_1]
group_2 = handles[size_1:size_1 + size_2]
group_3 = handles[size_1 + size_2:]

# Create the three tribe dictionaries
tribe_1 = {}
tribe_2 = {}
tribe_3 = {}

for devo in group_1:
    tribe_1[devo] = devo_duckies[devo]
for devo in group_2:
    tribe_2[devo] = devo_duckies[devo]
for devo in group_3:
    tribe_3[devo] = devo_duckies[devo]
    
# Explain the separation criterion
print("The tribes are separated by Devo handle length, from shortest to longest.")
print("The Devos are then divided into three tribes of as-equal-as-possible size.")

# Print tribes
print("\nTRIBE 1:")
for devo in tribe_1:
    print(devo + " : " + tribe_1[devo])
print("\nTRIBE 2:")
for devo in tribe_2:
    print(devo + " : " + tribe_2[devo])
print("\nTRIBE 3:")
for devo in tribe_3:
    print(devo + " : " + tribe_3[devo])

# Create lists of handles for random selection
tribe_1_handles = list(tribe_1.keys())
tribe_2_handles = list(tribe_2.keys())
tribe_3_handles = list(tribe_3.keys())
# Shuffle so that each run produces different teams
random.shuffle(tribe_1_handles)
random.shuffle(tribe_2_handles)
random.shuffle(tribe_3_handles)
devo_teams = []

# No remainder: everyone can be put into trios
if remainder == 0:
    for i in range(tribe_len):
        team = [
            tribe_1_handles[i],
            tribe_2_handles[i],
            tribe_3_handles[i]
        ]
        devo_teams.append(team)

# One extra person:
# make one fewer trio, leaving four people for two duos
elif remainder == 1:
    for i in range(tribe_len - 1):
        team = [
            tribe_1_handles[i],
            tribe_2_handles[i],
            tribe_3_handles[i]
        ]
        devo_teams.append(team)
    devo_teams.append([
        tribe_1_handles[-2],
        tribe_2_handles[-1]
    ])
    devo_teams.append([
        tribe_1_handles[-1],
        tribe_3_handles[-1]
    ])


# Two extra people:
# make normal trios and one final duo
elif remainder == 2:
    for i in range(tribe_len):
        team = [
            tribe_1_handles[i],
            tribe_2_handles[i],
            tribe_3_handles[i]
        ]
        devo_teams.append(team)
    devo_teams.append([
        tribe_1_handles[-1],
        tribe_2_handles[-1]
    ])


# Print final teams with duckies
print("\nDEVO TEAMS:")
team_number = 1
for team in devo_teams:
    print("\nTeam " + str(team_number) + ":")
    for devo in team:
        print(devo + " : " + devo_duckies[devo])
    team_number += 1