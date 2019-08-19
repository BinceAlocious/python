#Print all nos to a given limit in a Single line

n=int(input("Enter No "))
no=0
i=0
while(i<=n):
    if(i<10):
        no=no*10+i
    elif(i>=10 & i<100):
        no=no*100+i
    elif(i>=100 & i<1000):
        no=no*1000+i
    i+=1
print(no)