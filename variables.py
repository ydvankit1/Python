# local v/s gllobal variable

# x=4;

# def hello():
#     x=5;
#     print(f"the local x is {x}");

# hello();

# print(f"the global x is {x}");


# updating global variable inside function

x=10;

def func():
    global x;
    x=4;
    y=5;
    print(y);

func();
print(x);
# print(y) # this will throw error because y is local variable cant access outside
    