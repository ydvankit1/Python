def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

# @greet # either decorete here or call greet with hello
def hello():
    print("Hello world")

# hello()
greet(hello)()

# O/p-
# Good Morning
# Hello World
# Thanks for using this function