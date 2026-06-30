# def double(x):
#     return x*2

# double = lambda x: x*2  # anynomous function get rid from indentation and used easily in one line
# avg = lambda x, y, z : (x+y+z)/3 # pass easily this function to other function as an argument 

# print(double(5))

def appl(fx, value):
    return 6+fx(value)

print(appl(lambda x: x*x*x, 2));

 
  
