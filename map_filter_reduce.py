# def cube(x):
#     return x*x*x

l=[1,2,4,6,4,3]
# newl=[]
# for itm in l:
#     newl.append(cube(itm))

# function taking argument as other function called higher order function

# map------------------------

# newl=list(map(cube,l))
# print(newl);

# filter--------------------------

# def filtr_fun(a):
#     return a>4

# newl= list(filter(filtr_fun, l))
# print(newl);


# reduce----------------------------

from functools import reduce

number=[1,2,3,4,5]

def mysum(x,y):
    return x+y

sum = reduce(mysum, number)

print(sum)


