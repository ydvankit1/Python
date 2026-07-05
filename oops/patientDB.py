class Patient:
    def __init__(self, patientId, patientName, diseaseCategory, treatmentCost, doctorName):
        self.patientId=patientId
        self.patientName=patientName
        self.diseaseCategory=diseaseCategory
        self.treatmentCost=treatmentCost
        self.doctorName=doctorName

class Hospital:
    def __init__(self, patientdb, hospitalName):
        self.patientdb=patientdb
        self.hospitalName=hospitalName

    def searchByPatientName(self, patientName):
        ptntLst=[]
        for ptnt in self.patientdb.values():
            if ptnt.ptntName==patientName:
                ptntLst.append(ptnt)
        if len(ptntLst==0):
            return None
        else:
            return ptntLst

    def calculateTotalCostByDiseaseCategory(self, diseaseCategory, percentDeduction):
        cost=0
        for ptnt in self.patientdb.values():
            if ptnt.diseaseCategory==diseaseCategory:
                cost+=ptnt.treatmentCost

        if cost==0:
            return 0
        else:
            return cost-[(percentDeduction/100)*cost]
        

if __name__ == "__main__":
    n=int(input())
    patientdb={}
    for i in range(1, n+1):
        patientId=int(input())
        patientName=input()
        diseaseCategory=input()
        treatmentCost=float(input())
        doctorName=input()
        ptntObj=Patient(patientId, patientName, diseaseCategory, treatmentCost, doctorName)
        patientdb[i]=ptntObj

    hsptlobj=Hospital(patientdb, "abc")

    ptntName=input()
    ptnt=hsptlobj.searchByPatientName(ptntName)
    if ptnt is None:
        print("No patient exists with the name")
    else:
        for p in ptnt:
            print(p.patientId)
            print(p.patientName)
            print(p.diseaseCategory)
            print(p.treatmentCost)
            print(p.doctorName)

    diseaseCategory=input()
    percentageDeduction=int(input)
    cost=hsptlobj.calculateTotalCostByDiseaseCategory(diseaseCategory,percentageDeduction)
    if cost==0:
        print("0.0")
    else:
        print(float(cost))


        
        


