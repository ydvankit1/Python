
def fn1():
    try:
        num=int(input("enter an integer: "))
        a=[6,3]
        print(a[num]);
    except ValueError:
        print("no. entered is not a integer")
    except IndexError:
        print("index error");
    finally:
        print("I always ececuted"); # always execute either function return 1 or 0

print(fn1);


# raising error:

a=int(input("enter value between 5 and 9"))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")