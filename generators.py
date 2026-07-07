def my_generator():
    for i in range(5):
        yield i


gen=my_generator()
print(next(gen)) #0
print(next(gen)) #1
print(next(gen)) #2