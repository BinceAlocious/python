import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
def greet():
    print("Hello")
    greet()             #if No limit Then 992 times hello printed
greet()