class employee:
    companyName="Google"  # class variable 
    def __init__(self, name):
        self.name=name
        self.raise_amount=0.02  # instance variable

    def showDetails(self):
        print(f"the name of the employee is {self.name} and the raise amout in {self.companyName} is {self.raise_amount}")


obj1=employee("ankit")
obj1.raise_amount=0.9
obj1.showDetails()

obj2=employee("yadav")
obj2.showDetails()