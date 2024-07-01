import time

def thread_function(name):
    print(f"{name} Time - {time.time()}")
    time.sleep(2)
    print(f"{name} Time - {time.time()}")

import threading

x = threading.Thread(target=thread_function, args=(1, ))

print("Prima di thread")
x.start()
print("Thread partito")
print("Thread finito?=?")
