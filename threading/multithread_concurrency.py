# threading = concurrency

import threading
import time

def take_order():
    for i in range (1,4):
        print(f"Taking order for {i}")
        time.sleep(2)

def making_food():
    for i in range(1,4):
        print(f"making food for {i}")
        time.sleep(3)

# create threads
# multiple thread executing at a same time

order_thread = threading.Thread(target=take_order)    # multithreading
make_thread = threading.Thread(target=making_food)

order_thread.start()
make_thread.start()

# wait for both to finish

order_thread.join()
make_thread.join()

print("all order taken and food maked")


# Taking order for 1
# making food for 1
# Taking order for 2
# making food for 2
# Taking order for 3
# making food for 3
# all order taken and food maked