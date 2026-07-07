class Vector:
    def __init__(self, i, j, k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self): # dunder method (double underscore) for printing str object
        return f"{self.i}i+{self.j}j+{self.k}k"
    
    def __add__(self,x): # x=v2 and add used for operator overloading
        return Vector(self.i+x.i, self.j+x.j, self.k+x.k)
    
v1=Vector(3, 5, 6)
print(v1)
 
v2=Vector(1, 2, 9)
print(v2)

print(v1+v2)  # python internally convert it into v1.__add__(v2)
