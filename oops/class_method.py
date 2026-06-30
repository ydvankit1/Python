class employee:
    company="apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(self, newCompany):
        self.company=newCompany

obj1 =employee()
obj1.name="ankit"
obj1.show()
obj1.changeCompany("Tesla")
obj1.show()

