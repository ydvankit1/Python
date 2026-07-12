class math:
    def __init__(self,num):
        self.num=num

    def addtonum(self, n):
        self.num = self.num+n;

    @staticmethod       # no use of self
    def add(a,b):  # to ship it along with math class  (utility/helper fumction related to class)
        return a+b
    
a=math(5)
print(a.num) # 5
a.addtonum(6)  
# print(a.num) # 11

print(math.add(7,2)) # access diretly using class name   