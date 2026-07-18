# threading with a CPU-bound task
# For CPU-bound work like this counting loop, 
# threads in Python usually don't provide a speedup because of the GIL - Global Interpreter Lock

import threading
import time

def make_food():
    print(f"{threading.current_thread().name} started making")
    count = 0
    for _ in range(100_000_000):   # keeps cpu busy 
        count += 1
    print(f"{threading.current_thread().name} finished making")

    # program typically takes about as long as running the two counting loops sequentially, 
    # sometimes a bit longer because of thread scheduling overhead cause mutex 


if __name__ == "__main__":
    thread1 = threading.Thread(target=make_food, name="rice")
    thread2 = threading.Thread(target=make_food, name="dal")

    start = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end = time.time()

    print(f"Total time taken: {end - start:.2f} seconds")



    # solution is I/O bound disk read/write by web request
    # each thread writing into seperate memory location make's faster