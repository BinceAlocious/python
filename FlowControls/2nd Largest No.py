#  Second Largest No
no1=int(input("Enter No 1 "))
no2=int(input("Enter No 2 "))
no3=int(input("Enter No 3 "))

if((no1>no2)&(no1>no3)):
    print("Largest is No 1 ")
    if(no2>no3):
        print("Second Largest is No 2")
    else:
        print("Second Largest is No 3")
elif((no2>no1)&(no2>no3)):
    print("Largest is No 2")
    if(no1>no3):
        print("Second Largest is No 1")
    else:
        print("Second Largest is No 3")
else:
    print("Largest is No 3")
    if(no1>no2):
        print("Second Largest is No 1")
    else:
        print("Second Largest is No 2")
