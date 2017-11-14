import threading
from queue import Queue
import time

start = time.time()

print_lock = threading.Lock()

def exampleJob(worker):
    time.sleep(1) # In seconds

    with print_lock:
        print(threading.current_thread().name, worker)

def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()
        
q = Queue()
for worker in range(20):
    q.put(worker)
    
for x in range(10):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

q.join()

print("Entire job took", time.time()-start)



