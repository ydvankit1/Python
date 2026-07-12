# def calculateGmean(a,b):
#     mean=(a*b)/(a+b)
#     print(mean);

# calculateGmean(8,7); 
# calculateGmean(b=7, a=8);  // can change order to 


# def calculateGmean(a,b):
#     mean=(a*b)/(a+b)
#     return mean;   

# ans=calculateGmean(8,7); 
# print(ans) 



# take tuple in arguments  

# def avg(* no):
#     sm=0;
#     for i in no:
#         sm+=i;
#     print("avg is: ", sm/len(no));

# avg(5, 6, 7);



#  taking dictionary in arguments

# def name(** name):
#     print("Hello,", name["fname"], name["lname"]);

# name(fname="Ankit", lname="Yadav");


# def order(var=[]):
#     var.append("Masala")
#     print(var)

# order()

# returning multiple value

# def fn():
#     return 100, 200, 300

# a, b, c = fn()
# print(a, b, c)


# variable scoping in function

def fn():   # pure function
    var= "lemon"  # enclosing
    def order():
        var="ginger"   # innner
        print("Inner: ",var)
    order()
    print("outer: ",var)

var="Tulsi" # global
fn()
print("global: ",var)



def fn():
    var="eliachi"
    def update():
        nonlocal var  # nonlocal update enclosing variable
        var="kesar"
    update()
    print("after update", var)

fn()


var= "plain"

def fn():
    def update():   # impure function
        global var   # update global variable
        var="Irani"
    update()

fn()
print("after update: ", var)
