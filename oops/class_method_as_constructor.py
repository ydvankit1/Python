class employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    @classmethod
    def formStr(self, str):
        return self(str.split("-")[0],int(str.split("-")[1]))

str="ankit-100000"
# obj=employee(str.split("-")[0],str.split("-")[1])
obj=employee.formStr(str)

print(obj.name)
print(obj.salary)

