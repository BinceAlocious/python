f=open("name.txt")
lst=[]
for i in f:
    lst.append(i.rstrip("\n"))
    # lst.append(i[:-1])
print(lst)
g=open("phone.txt")
lst2=[]
for j in g:
    lst2.append(j.rstrip("\n"))
    # lst2.append(j[:-1])
print(lst2)
#use .rstrip("\n")
h=open("Output2.txt","a")
leng=len(lst)
leng2=len(lst2)
for i in range(0,leng):
    for j in range(0,leng2):
        if(i==j):
            h.write(lst[i]+" "+lst2[j]+"\n")