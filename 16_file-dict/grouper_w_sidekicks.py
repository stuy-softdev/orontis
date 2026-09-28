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

print("The groups are split by handles and sorted by length. Meaning, the first group contains the first third of handles by length.")

for i in [group_1, group_2, group_3]:
    print("\n")
    print(i)

#Split the groups into smaller groups!
devo_trios = [[group_1[x], group_2[x],group_3[x]] for x in range(len(group_1))]

#If one person is left out
if len(group_3) - len(group_1) == 1:
    #take the last person from the last group and make a duo
    devo_trios.append([devo_trios[-1][-1], group_3[-1]])
    #then remove the last person from the last group!
    devo_trios[-2] = devo_trios[-2][:-1]
#If two people are left out
elif len(group_3) - len(group_1) == 2:
    #Add those two people to the group!
    devo_trios.append([group_3[-2], group_3[-1]])
       

#Print the groups!
print("Devo trios:")
for i in devo_trios:
    trio = ""
    for x in i:
        trio += x + ", "
    print(trio[:-2])