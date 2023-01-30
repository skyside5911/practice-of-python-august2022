import threading
from threading import *
def display():
    print("current threading name is ", threading.current_thread().getName())
t=Thread(target=display)
t.start()  
print("current threading name is ", threading.current_thread().getName())  
