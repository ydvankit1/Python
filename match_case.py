x= int(input("Enter value of x: "))

# match x:
#     case 0:
#         print("x is zero");    
#     case 4:
#         print("its 4");
#     case _:
#         print(x);

match x:
    case 0:
        print("x is zero");    
    case 4:
        print("its 4");
    case _ if x!=90:
        print(x is not 90)
    case _:                  # default case
        print(x);