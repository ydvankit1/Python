# in python no concept of access modifier but we make according to our convention

# class employee:
#     def __init__(self):
#         self.name="ankit"

# obj=employee()  
# print(obj.name)  # by default variable public




class employee:
    def __init__(self):
        self.__name="ankit"  # now it become private i.e, can't access directly

obj=employee()  
print(obj._employee__name)  # can access indirectly