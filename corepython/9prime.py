def checkprime(no):
    flag=0
    for i in range(2,no):
        if(no%i==0):
            flag+=1
    if(flag!=0):
        print("FALSE:Not a Prime Number")
    else:
        print("TRUE:Prime Number")

n=int(input("Enter No to Check: "))
checkprime(n)
