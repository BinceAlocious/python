import time
from threading import *

def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double Values=",2*n)
def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print("Squares=",n*n)
numbers=[1,2,3,4,5]
t=Thread(target=doubles,args=(numbers,)) #Here we pass args as tuple so ','
h=Thread(target=squares,args=(numbers,))
begintime=time.time()
t.start()
h.start()
#doubles(numbers)
#squares(numbers)
t.join()
h.join()
endtime=time.time()

print("Total Time Elapsed=",endtime-begintime)