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


# single Inheritance


class Animal:
    def __init__(self, name, species):
        self.name=name
        self.species=species
        
    def make_sound(self):
        print("sound made by animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species=Dog)
        self.breed=breed

    def make_sound(self):
        print("Bark!")
    
d=Dog("dog","dog")
d.make_sound()   # bark (override)

a=Animal("dog","dog")
a.make_sound()


# Multiple Inheritance

class Employee:
    def __init__(self, name):
        self.name=name
    def show(self):
        print("I am a employee method")

class Dancer:
    def __init__(self, dance):
        self.dance=dance
    def show(self):
        print("I am a Dancer method")

class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance=dance
        self.name=name

obj=DancerEmployee("kathak", "shiv")
print(obj.name)
print(obj.dance)
obj.show() # print employee self method (i.e, first pass params) 