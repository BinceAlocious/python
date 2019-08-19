no1=int(input("Enter No1 "))
no2=int(input("Enter No 2"))
no3=int(input("Enter No 3 "))

if((no1>no2)&(no1>no3)):
    print("Highest No is No1")
elif((no2>no1)&(no2>no3)):
    print("Highest No is NO2")
else:
    print("Highest No is No3")
