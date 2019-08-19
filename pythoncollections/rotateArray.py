def rotate(lst,n):
    lst2=[]
    leng=len(lst)
    for i in range(n,leng):
        lst2.append(lst[i])
    for j in range(0,n):
        lst2.append(lst[j])
    print(lst2)

lst=[1,2,3,4,5,6]
n=int(input("Enter Position to Start Rotation: "))
rotate(lst,n)