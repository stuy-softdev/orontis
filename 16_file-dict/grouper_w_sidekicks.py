import random

devo_duckies = {}

with open ("handles_w_quackers.csv", "r") as file:
    lines = file.read().split("\n")
    for line in lines:
        if line != "":
            parts = line.split(",")
            devo = parts[0].strip()
            duck = parts[1].strip()
            devo_duckies[devo] = duck
print(devo_duckies)

#Get all Devo handles from dictionary
handles = list(devo_duckies.keys())

handles.sort(key=len)

tribe_len = len(handles) // 3

#Split the three groups! (as equally as possible, with the reminder ends up in group_3)
group_1 = handles[:tribe_len]
group_2 = handles[tribe_len: tribe_len * 2]
group_3 = handles[tribe_len * 2:]

tribe_1 = {}
tribe_2 = {}
tribe_3 = {}

for devo in group_1:
    tribe_1[devo] = devo_duckies[devo]
for devo in group_2:
    tribe_2[devo] = devo_duckies[devo]
for devo in group_3:
    tribe_3[devo] = devo_duckies[devo]
    
tribe_1_handles = list(tribe_1.keys())
tribe_2_handles = list(tribe_2.keys())
tribe_3_handles = list(tribe_3.keys())
random.shuffle(tribe_1_handles)
random.shuffle(tribe_2_handles)
random.shuffle(tribe_3_handles)

devo_teams = []

for i in range(len(tribe_1_handles)):
    team = [
        tribe_1_handles[i],
        tribe_2_handles[i],
        tribe_3_handles[i]
    ]

    devo_teams.append(team)

print("The groups are split by handles and sorted by length. Meaning, the first group contains the first third of handles by length.")

for i in [group_1, group_2, group_3]:
    print("\n")
    print(i)

print("\nDevo teams:")

for team in devo_teams:
    print(team)