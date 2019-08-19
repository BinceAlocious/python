def lcm(no,a,b):
    if(no%a==0 and no%b==0):
        print("LCM=",no)
    else:
        no+=1
        lcm(no,a,b)
no1=int(input("Enter No1: "))
no2=int(input("Enter No2: "))
m=max(no1,no2)
lcm(m,no1,no2)
