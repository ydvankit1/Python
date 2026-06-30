class Person:
    name="ankit"
    occupation="SDE"
    network=10

    def info(self): # contain object for whose method is called (can give it any name)
        print(f"{self.name} is a {self.occupation}")

obj=Person()
print(obj.network)
obj.network=15;
print(obj.network)

obj.info()   