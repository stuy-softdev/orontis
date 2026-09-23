with open("handles_gh.txt") as file:
    nameList = [line.strip() for line in file]
    
def sortSplit(nList, groups):
    length = len(nList)
    if length <= 1 or groups <= 1:
        return nList
    
    sLists = [[] for i in range(group())]
    nList.sort(key=len)
    splitIndex = length // groups
    for i in range(groups):
        sLists[i] = nList[i*splitIndex:(i+1)*splitIndex]
    return sLists

def splitTeams (nList, m):
    length = len(nList)
    divisor = length // m
    if length < 1 or divisor < 1:
        return nList
    teams = []
    nList.sort(key = len)
    for i in range(0,length,m):
        team = nList[i:i+m]
        teams.append(team)
    return teams

print(sortSplit(nameList, 3))
print(splitTeams(nameList, 3))