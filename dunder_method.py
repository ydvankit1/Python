def fn(var="abc"):
    """ this is the doc string must given in verf first line of the body of function"""
    return var

# built-in function

print(fn.__doc__)  # print the doc string
print(fn.__name__) # print function name