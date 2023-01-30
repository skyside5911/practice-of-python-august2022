from threading import *
class MyThread(Thread):
    def fun(self):
        for i in range(10):
            print("class_thread 1")
t=MyThread()
t.start()
for i in range(10):
    print("main_thread_1")