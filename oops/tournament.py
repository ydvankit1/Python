# class country-attributes:
# int matches, int wins, int defeatss, string country_name
# create init methos that take all the perimeter and set Value 

# class tournament-attribute:
# string leagueName
# list countryList
# create init method to  take all perimeter and set vlaue

# implement method in tournament class-
# findCountryByMaximumMatches: return country having maximum value of matches of all the country in the countrylist else return none to main
# sortByWins: return sorted list of wins in ascending order from all the country  else return none

# main:
# create tournament and country object
# read value of n for country list
# read country attributes n time and add to countrylist by making country object

# create tournament object by passing tournamentName and list of country 

# call method findCountryByMaximumMatches using tournament object and sortByWins using  tournament object 
# print output accordingly and if return then print no data found
    
# I/P:
# 5
# 44
# 24
# 20
# sri lanka
# 69
# 50
# 19
# india
# 40
# 31
# 9
# england
# 60
# 40
# 20
# australia
# 55
# 35
# 20
# south africa
# trnmnt1

# o/p-
# 69
# 50
# 19
# india
# 24
# 31
# 35
# 40
# 50


class country:
    def __init__(self, matches, wins, defeats, countryName):
        self.matches=matches
        self.wins=wins
        self.defeats=defeats
        self.countryName=countryName

class tournament:
    def __init__(self, tmtName, countryList):
        self.leagueName=tmtName
        self.countryList=countryList

    def findCountryByMaximumMatches(self):
        if not self.countryList:
            return None
        maxi=self.countryList[0]
        for mtch in self.countryList :
            if mtch.matches>=maxi.matches:
                maxi=mtch
        return maxi
        

    def sortByWins(self):
        if not self.countryList:
            return None
        return sorted(self.countryList,key=lambda country: country.wins)

    
if __name__ == "__main__":
    n=int(input())
    countryList=[]

    for i in range(n):
        matches=int(input())
        wins=int(input())
        defeats=int(input())
        countryName=input()
        cntryObj=country(matches, wins, defeats, countryName)
        countryList.append(cntryObj)

    tmtName=input()
    tmntObj=tournament(tmtName, countryList)

    mxMtch=tmntObj.findCountryByMaximumMatches()
    if mxMtch is None:
        print("No data found")
    else:
        print(mxMtch.matches)
        print(mxMtch.wins)
        print(mxMtch.defeats)
        print(mxMtch.countryName)

    srtdLst=tmntObj.sortByWins()
    if srtdLst is None:
        print("No data found")
    else:
        for i in srtdLst:
            print(i.wins)



