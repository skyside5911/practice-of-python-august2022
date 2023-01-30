import numbers
from threading import *
import time
def double(numbers):
    for n in numbers:
        time.sleep(1)
        print("double",2*n)
def square(numbers):
    for i in numbers:
        time.sleep(1)
        print("square",i*i)
numbers=[1,2,3,4,5,6]
begintime=time.time()
t1=Thread(target=double,args=(numbers,))
t2=Thread(target=square,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime=time.time()
print("total time taken",endtime-begintime)