# for i in range(1,10):
#     print(i)
#Print multiplication table

no=int(input("Enter No "))
for i in range(1,11):
    print(i,"*",no,"=",no*i)

#Limit even nos

lim=int(input("Enter the upper Limit "))
for i in range(0,lim,2):
    print(i)
#continue and Break

for i in range(0,10):
    if(i==5):
        continue
    print(i)

