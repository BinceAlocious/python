# def sumofel(lst,sum):
#     for i in lst:
#         for j in lst:
#             if (i + j == sum):
#                 print("Elements are ", i, j)
#             break
#         else:
#             print("No Such Elements Exist ")
# no=int(input("Enter Size of List "))
# lst=[]
# for i in range(0,no):
#     el=int(input("Enter Element "))
#     lst.append(el)
# sum=int(input("Enter Sum of Elements  "))
# sumofel(lst,sum)
#or
def sumofelm(lst,sum):
    low=0
    leng=len(lst)
    up=leng-1
    while(low!=up):
        s=lst[low]+lst[up]
        if(s==sum):
            print(lst[low],lst[up])
            break
        elif(s<sum):
            low+=1
        elif(s>sum):
            up-=1
    else:
        print("No such elements Exist ")

no=int(input("Enter Size of List "))
lst=[]
for i in range(0,no):
    el=int(input("Enter Element "))
    lst.append(el)
sum=int(input("Enter Sum of Elements "))
sumofelm(lst,sum)



