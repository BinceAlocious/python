#With extending Thread Class
from threading import *
class MyThread(Thread):  #inheritance of Thread class
    def run(self):
        for i in range(10):
            print("Inside MyThread run method")
        print(current_thread().getName())
t=MyThread()
t.start() #by inheritance start() is called;start() has run fn;Thread class has run() which is overridden by run in child class
for i in range(10):
    print("Inside Main Thread")
