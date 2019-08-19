no=int(input("Enter Size of List "))
lst=[]
for i in range(0,no):
    el=int(input("Enter Value "))
    lst.append(el)
print(lst)
lst.sort()
print('sorted ',lst)
