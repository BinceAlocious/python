def lcm(a,b):
    m=max(a,b)
    p=a*b
    for i in range(m,p+1):
        if(i%a==0 and i%b==0):
            print("LCM=",i)
            break
        else:
            pass
no1=int(input("Enter No1: "))
no2=int(input("Enter No2: "))
lcm(no1,no2)

