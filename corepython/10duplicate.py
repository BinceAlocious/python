#10
def remove(lst):
    set1=set()
    lst2=[]
    for i in lst:
        if(i not in set1):
            set1.add(i)
    for j in set1:
        lst2.append(j)
    print(lst2)
lst=[]
n=int(input("Enter No of Elements in List: "))
for i in range(0,n+1):
    el=int(input("Enter Element: "))
    lst.append(el)
remove(lst)