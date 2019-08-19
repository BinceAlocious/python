def leaspos(lst):
    lst.sort()
    for i in lst:
        if(i>=0):
            print(i)
            break

no=int(input("Enter Size of List "))
lst=[]
for i in range(0,no):
    el=int(input("Enter Element: "))
    lst.append(el)
leaspos(lst)