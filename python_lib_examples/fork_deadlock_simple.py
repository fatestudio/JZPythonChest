from os import fork
from threading import Lock

# Lock is acquired in the parent process:
lock = Lock()
lock.acquire()

if fork() == 0:
    # In the child process, try to grab the lock:
    print("Acquiring lock...")
    lock.acquire()
    print("Lock acquired! (This code will never run)")
