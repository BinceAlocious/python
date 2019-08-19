def pattern(lst):
    leng=len(lst)
    pr=1
    lst2=[]
    for i in range(0,leng):
        for j in range(0,leng):
            if(i==j):
                continue
            else:
                pr=pr*lst[j]
        lst2.append(pr)
        pr=1
    print(lst2)


lst=[2,3,4,5]
pattern(lst)