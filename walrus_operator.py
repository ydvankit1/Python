print(a:=False) # allow to assign a value to a varible with an expression


# without walrus operator

# foods=list()
# while True:
#     food=input("what food do you like?: ")
#     if food=="quit":
#         break
#     foods.append(food)

# with walrus operator

foods =list()
while (food := input("what food do you like?: "))!="quit":
    foods.append(food)
