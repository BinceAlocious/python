no=int(input("Enter Size of List "))
lst=[]
for i in range(0,no):
    e=int(input("Element "))
    lst.append(e)
print("List= ",lst)
max=max(lst)
lst.sort()
lst2=[]
for i in range(1,max):
    lst2.append(i)
m=len(lst2)
for j in range(0,m):
    if(lst[j]!=lst2[j]):
        les=lst2[j]
        break
    else:
        les=0

print("Least Positive Integer=",les)





   




