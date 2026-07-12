class employee:
    companyName="Google"  # class variable ------- sinlge copy shared by all object
    def __init__(self, name):
        self.name=name
        self.raise_amount=0.02  # instance variable

    def showDetails(self):
        print(f"the name of the employee is {self.name} and the raise amout in {self.companyName} is {self.raise_amount}")


obj1=employee("ankit")
obj1.raise_amount=0.9  # update the value for the current object
obj1.showDetails() 

obj2=employee("yadav")
obj2.showDetails()

print(obj2.companyName)
print(obj1.companyName)
print(employee.companyName)   