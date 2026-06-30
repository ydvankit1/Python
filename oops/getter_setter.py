class myclass:
    def __init__(self, value): # constructor
        self.value=value
    # def show(self):
    #     print(f"value is {self.value}")
    @property # allow method calling obj.fun = instead of obj.fun()
    def fun(self):  # getter
        return 10*self.value
    @fun.setter  
    def fun(self, newVal):  # setter
        self.value=newVal/10

obj=myclass(10)
obj.fun=67  # call setter
print(obj.fun)