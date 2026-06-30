# class team: attribut: owner, value, id, Name
# init method take all parameter and set value

# class league: attribute leagueName, teamlist
# init method take all parameter and set Value 

# implement method:
#    create method in league class:
# 1. findMinimumTeamById:
#    return team having minimum value for id of all the team if empty return none

# 2. sortTeamById:
#    return team sorted list for id in ascending order of all team in team list
# if empty return None

# this method called from main
# a: create team and league object

# to create list of n team object read the val of n 
# and for each time read owner, value, id, name
# create team object and add in list

# create league object by passing league name and list of team created previously 

# call method find findMinimumTeamById and sortTeamById using league object

# print o/p for both as given in sample



# ex:I/P:

# 5

# dc 
# 395
# 21
# Pant 
# rcb
# 184
# 5
# virat
# mi
# 132
# 75
# rohit
# csk
# 904
# 87
# dhoni
# pk 
# 849
# 74
# rahul
# randomTeam


# O/P:

# rcb
# 184
# 5
# virat
# 5
# 21
# 74
# 75
# 87



class team:
    def __init__(self, owner, value, id, name):
        self.owner=owner
        self.value=value
        self.id=id
        self.name=name

class league:
    def __init__(self, leagueName, teamList):
        self.leagueName=leagueName
        self.teamList=teamList

    def findMinimumTeamById(self):
        if not self.teamList:
            return None
        # return min(self.teamList, key=lambda team: team.id)
        mini=self.teamList[0]
        for tm in self.teamList:
            if tm.id<mini.id:
                mini=tm
        return mini

    def sortTeamById(self):
        if not self.teamList:
            return None
        return sorted(self.teamList, key=lambda team: team.id)


if __name__ == "__main__":
    n=int(input())
    teamList=[]

    for i in range(n):
        owner=input()
        value=int(input())
        id=int(input())
        name=input()
        tmObj=team(owner, value, id, name)
        teamList.append(tmObj)

    leagueName=input()
    legObj=league(leagueName, teamList) 

    mnTm=legObj.findMinimumTeamById()
    if mnTm is None:
        print("No data found")
    else:
        print(mnTm.owner)
        print(mnTm.value)
        print(mnTm.id)
        print(mnTm.name)

    srtdTm=legObj.sortTeamById()
    if srtdTm is None:
        print("No data found")
    else:
        for srtdId in srtdTm:
            print(srtdId.id)


