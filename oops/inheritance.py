class employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id

    def show(self):
        print(f"the name of emplyee: {self.id} is {self.name}")

class prgrmr(employee):
    def showlang(self):
        print("python")

obj1 = employee("ankit", 111)
obj1.show()

obj2=prgrmr("yad", 112)
obj2.show()  #inheritance
obj2.showlang()
