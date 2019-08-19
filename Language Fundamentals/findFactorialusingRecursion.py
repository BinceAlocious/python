def factorial(no):
    if(no==0):
        return 1
    else:
        return no*factorial(no-1)
n=int(input("Enter No: "))
print(factorial(n))
