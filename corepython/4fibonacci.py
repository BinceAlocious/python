#4 Without Recursion
def series(n):
    no=[0]
    a=0
    i=1
    while(i<=n):
        c=a+i
        a=i
        no.append(i)
        i=c
    print(no)
no=int(input("Enter Limit"))
series(no)
