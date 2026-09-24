nameList = []

#data is sanitized with .strip() that removes any empty space. Each line creates a new index in nameList that is the name only.
with open("handles_gh.txt") as file:
    nameList = [line.strip() for line in file]
   
#sorts a list by length of name, then splits it into 3 separate lists stored in 1 master list
def sortSplit(nList, groups):
    length = len(nList)
    if length < 1 or groups < 1:
        return nList
   
    sLists = [[] for i in range(groups)]
    nList.sort(key=len)
    splitIndex = length // groups
   
    for i in range(groups):
        sLists[i] = nList[i*splitIndex:(i+1)*splitIndex]
       
    return sLists

#sorts the names from least to most characters, then returns a list of lists each containing of m number of names from nList
def splitTeams(nList, m):
    names = nList.copy()
    length = len(names)
   
    if length < 1 or m < 1:
        return names
   
    names.sort(key=len)
    teams = []
    remainder = length % m
    for i in range(0, length - remainder, m):
        teams.append(names[i:i + m])

    #if there is one person left out
    if remainder == 1:
        #takes a person from the last team,
        lastTeam = teams.pop()
        #creates the last team without the person
        teams.append(lastTeam[:-1])
        #create a new team with that person and the leftover person
        teams.append([lastTeam[-1]] + names[length - 1:])
       
    #put leftover people into a group if remainder is 2 or more.
    elif remainder > 0:
        teams.append(names[length - remainder:])

    return teams

#print(sortSplit(nameList, 3))
print(splitTeams(nameList, 3))