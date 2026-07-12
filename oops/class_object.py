class Person:
    name="ankit"
    occupation="SDE"
    network=10

    def info(self): # self contain object for, those method is called (can give it any name)
        print(f"{self.name} is a {self.occupation}")

obj=Person()
print(obj.network)  #10
obj.network=15

obj.age=23

print(obj.network)  #15 network change for only current object
print(Person.network)   #10  no change in class network
print(obj.age)

del obj.network

print(obj.network)  #10
print(Person.network)    #10

del obj.age
print(obj.age)  # error because it not  part of attribute of class  ----- called attribute shadowing  

obj.info()   # by default object has reference of the class