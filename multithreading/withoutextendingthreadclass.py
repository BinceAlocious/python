#Creating threading without extending Thread Class

from threading import *
import time

class Test:
    def mi(self):
        for i in range(10):
            time.sleep(5)     #for 5 sec thread goes to Wait Stage So Main thread Works
            print("Inside Test")
obj=Test()
t=Thread(target=obj.mi) #Don't Use Function brackets
t.start()
for i in range(10):
    print("inside Main Thread")
