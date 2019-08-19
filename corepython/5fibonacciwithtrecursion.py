#5 With recursion
def fibo(no):
    if(no<=1):
        return no
    else:
        return(fibo(no-1)+fibo(no-2))

n=int(input("Enter No of Elements:"))
lst=[]
for i in range(0,n+1):
    lst.append(fibo(i))
print(lst)