def mod(no):
    lst=[]
    for i in range(1,no+1):
        rem=no%i
        lst.append(rem)
    print(lst)
n=int(input("Enter No: "))
mod(n)
