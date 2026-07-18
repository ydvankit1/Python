# parallelism  =  multiprocessing

from multiprocessing import Process
import time

def make_food(name):
    print(f"start making {name}")
    time.sleep(3)
    print(f"end making {name}")

if __name__ == "__main__":
    food=[
        Process(target=make_food, args=(f"food {i+1}", ))
        for i in range(3)
    ]
    

    # start all process
    for p in food:
        p.start()

    # wait for all to complete
    for p in food:
        p.join()

    print("all food served")


# start making food 1
# start making food 2
# start making food 3
# end making food 1
# end making food 2
# end making food 3
# all food served
