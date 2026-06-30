# class gurukul
# attributes: gurukulNo,noOfSeat, area, facultyName
# init method that take all perimeter and set Value 

# class zone
# attributes: zoneName, zoneList 
# init method take all perimeter and set Value 

# implement method inside zone:

# FindGurukulWithFacultyName: return gurukul number form the zone list if their is any gurukul number with the faculty name 
# else return No Gurukul

# FindLeastAreaGurukul: return least area gurukul from zonelist (gurukul_number, no_of_seats, Area, faculty_name)

# create gurukul object
# read the value of n and take input for n object (gurukul name, no of seats, area, faculty name)
# create gurukul object and add to list

# create zone object by passing the zone name and list of zone

# call methods print output

# I/P:

# 4
# 12
# 15
# 1500
# sai
# 13
# 25
# 4000
# sushmitha
# 14
# 25
# 4000
# sahaja
# 15
# 15
# 2000
# rakesh
# sahaja


# O/P:
# 14
# 12
# 15
# 1500
# sairam



class gurukul:
    def __init__(self, gurukulNo, noOfSeat, area, facultyName):
        self.gurukulNo=gurukulNo
        self.noOfSeat=noOfSeat
        self.area=area
        self.facultyName=facultyName

class zone:
    def __init__(self, zoneName, zoneList):
        self.zoneName=zoneName
        self.zoneList=zoneList

    def findGurukulWithFacultyName(self, facultyName):
        for i in self.zoneList:
            if i.facultyName==facultyName   :
                return i.gurukulNo
        return None
        
    def findLeastAreaGurukul(self):
        if not self.zoneList:
            return None
        mnArea=self.zoneList[0]
        for i in self.zoneList:
            if i.area<mnArea.area:
                mnArea=i
        return mnArea


if __name__=="__main__":
    zoneList=[]
    n=int(input())
    for i in range(n):
        gurukulNo=int(input())
        noOfSeat=int(input())
        area=int(input())
        facultyName=input()
        grklObj=gurukul(gurukulNo, noOfSeat, area, facultyName)
        zoneList.append(grklObj)

    facltyFind=input()
    znObj=zone("zone1", zoneList)

    grklNo=znObj.findGurukulWithFacultyName(facltyFind)
    if grklNo is None:
        print("No data found")
    else:
        print(grklNo)

    lstGrkl=znObj.findLeastAreaGurukul()
    if grklNo is None:
        print("No data found")
    print(lstGrkl.gurukulNo)
    print(lstGrkl.noOfSeat)
    print(lstGrkl.area)
    print(lstGrkl.facultyName)
