top=-1
stack=[]
size=int(input("Enter Size of Stack: "))
def push():
    global stack
    global size
    global top
    element=int(input("Enter Element To Push: "))
    if(top<size):
        top+=1
        stack.insert(top,element)
    elif(top==size):
        print("Stack Full")
def pop():
    global stack
    global size
    global top
    if(top<0):
        print("Stack Empty")
    else:
        element=stack[top]
        top-=1
        print(element,"Was Removed")
def display():
    global top
    global stack
    for i in range(0,top+1):
        print(stack[i])


op=int(input("Enter Your Choice: 1.Push 2.Pop 3.Display 4.Exit"))
while(op!=4):
    if(op==1):
        push()
        op = int(input("Enter Your Choice: 1.Push 2.Pop 3.Display 4.Exit"))
    elif(op==2):
        pop()
        op = int(input("Enter Your Choice: 1.Push 2.Pop 3.Display 4.Exit"))
    elif(op==3):
        display()
        op = int(input("Enter Your Choice: 1.Push 2.Pop 3.Display 4.Exit"))
    elif(op==4):
        break