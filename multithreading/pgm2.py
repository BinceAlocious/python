from threading import *

def display():
    for i in range(1,10):
        print("Child thread executing")
    print(current_thread().getName())
t=Thread(target=display)   #Thread is a class display fn assigned to constructor
t.start()
for i in range(1,10):
    print("Main Thread executing")
print(current_thread().getName())

