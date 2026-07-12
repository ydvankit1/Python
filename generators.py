def my_generator():
    for i in range(5):
        yield i  # pauses and resume the function exactly from where it stops


gen=my_generator()   # memory optimized = getting one value at a time instead of simple loop that load entire value once in memory
print(next(gen)) #0
print(next(gen)) #1
print(next(gen)) #2
