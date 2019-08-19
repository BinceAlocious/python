# def add():
#     no1=int(input("Enter No 1 "))
#     no2=int(input("Enter No 2"))
#     sum=no1+no2
#     print("Sum",sum)
#
# add()
# add()
# def mul(no1,no2):
#     pr=no1*no2
#     print("Product",pr)
# mul(10,2)
#
# def cube(no):
#     res=no**3
#     return res
#
# cu=cube(3)
# print("Cube",cu)

#Create a Funct to check if Prime return boolean Value

def checkprime():
    no=int(input("Enter the No "))
    for i in range(2,no):
        if(no%i==0):
            return False
            break
        else:
            return True

bool=checkprime()
print(bool)

