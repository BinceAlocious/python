def pairs(lst,s):
    lst4=[]
    lst2=[{a,b} for a in lst for b in lst if a+b==s and a!=b]
    lst3=[{a,b,c} for a in lst for b in lst for c in lst if a+b+c==s and a!=b and b!=c and a!=c]
    for i in lst2:
        if(i not in lst4):
            lst4.append(i)
    for j in lst3:
        if(j not in lst4):
            lst4.append(j)
    print(lst4)

lst=[1,2,3,4,5]
s=int(input("Enter Sum: "))
pairs(lst,s)
