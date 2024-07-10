import time

def thread_function(name):
    print(f"{name} Time - {time.time()}")
    time.sleep(2)
    print(f"{name} Time - {time.time()}")

import threading

#   target = riferimento alla funzione, args = argomenti funzione (parametro, ) <- tupla di singolo elemento
x = threading.Thread(target=thread_function, args=(1, ))

print("Prima di thread")
x.start()
print("Thread partito")
print("Thread finito?=?")



from concurrent.futures import ThreadPoolExecutor 

#   max workers: numero di thread
#   len(secondo_argomento_di_map): numero di tasks
with ThreadPoolExecutor(max_workers=10) as executor:
    #   map prende la funzione e una lista di argomenti ognuno per task, in questo caso l'argomento è un range quindi ogni task avrà un argomento intero diverso
    #   avessimo voluto passare alla funzione una lista come argomento avremmo dovuto fare una lista di liste
    executor.map(thread_function, range(100))