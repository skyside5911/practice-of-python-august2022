from threading import *
class Test:
    def display(self):
        for i in range(10):
            print("class_method 2",current_thread().getName())
obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print("main_method 2")