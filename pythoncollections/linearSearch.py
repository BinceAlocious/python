def linearSearch(lst,el):
    for i in lst:
        flag=0 #or give flag before Loop
        if(i==el):
            flag+=1
            break
        else:
            pass
    if(flag==1):
        return True
    else:
        return False

lst=[]

n=int(input("Enter Size of List "))

for i in range(0,n):
    val=int(input("Enter Element "))
    lst.append(val)
element=int(input("Enter Element to Search For "))
bool=linearSearch(lst,element)
print(bool)
