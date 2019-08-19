#First in first out
front=0
rear=-1
q=[]
size=int(input("Enter Size of Queue: "))
def add():
    global q
    global rear
    global size
    if(rear==size-1):
        print("Queue Full")
    else:
        elm=int(input("Enter Element: "))
        rear+=1
        q.insert(rear,elm)
def delete():
    global front
    global rear
    if(front>rear or rear<0):
        print("Queue Empty")
    else:
        print(q[front],"DELETED")
        front+=1
def disp():
    global front
    global size
    global rear
    if(front==0):
        print("Queue Empty")
    else:
        for i in range(front,rear+1):
            print(q[i])
op=int(input("Enter Option: 1.ADD 2.DELETE 3.DISPLAY 4.EXIT"))
while(op!=4):
    if(op==1):
        add()
        op=int(input("Enter Option: 1.ADD 2.DELETE 3.DISPLAY 4.EXIT"))
    elif(op==2):
        delete()
        op=int(input("Enter Option: 1.ADD 2.DELETE 3.DISPLAY 4.EXIT"))
    elif(op==3):
        disp()
        op=int(input("Enter Option: 1.ADD 2.DELETE 3.DISPLAY 4.EXIT"))
    elif(op==4):
        break
    else:
        print("INVALID INPUT")
        op = int(input("Enter Option: 1.ADD 2.DELETE 3.DISPLAY 4.EXIT"))
