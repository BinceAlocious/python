def sta():
    stack=[]
    size=int(input("Enter Size of Stack: "))
    op=int(input("Enter Your Choice: 1.Push 2.Pop 3.Display 4.Exit"))
    while(op!=4):
        if(op==1):
            top=-1
            element=int(input("Enter Element to Push: "))
            if(top<size):
                top+=1
                stack.insert(top,element)
                op=int(input("Enter Your Choice: 1.Push 2.Pop 3.Display 4.Exit"))
            elif(top==size):
                print("Stack Full")
        elif(op==2):
            if(top<0):
                print("Stack Empty ")
            else:
                element=stack[top]
                top-=1
                print(element,"Was Removed")
                op=int(input("Enter Your Choice: 1.Push 2.Pop 3.Display 4.Exit"))
        elif(op==3):
            for i in range(0,top):
                print(stack[i])
        elif(op==4):
            break
sta()