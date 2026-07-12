class employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    @classmethod      # no use of self 
    def formStr(cls, str):
        name, salary = str.split("-")
        return cls(name, int(salary))
    
str="ankit-100000"
obj=employee.formStr(str)

print(obj.name)
print(obj.salary)

