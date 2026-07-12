class myclass:
    def __init__(self, value): # constructor

        self.value=value

    @property               # allow method calling by obj.fun instead of obj.fun()
    def fun(self):  # getter
        return self.value+2
    
    @fun.setter  
    def fun(self, newVal):  # setter
        self.value=newVal

obj=myclass(10)
print(obj.value)  # 10
obj.fun=67  # call setter
print(obj.fun)   # 69