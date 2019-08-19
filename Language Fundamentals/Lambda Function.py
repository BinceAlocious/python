def square(no):                      #this is a boiler plate code
    return no*no
print(square(3))

#use Lambda Function Nameless fuctions

res=lambda no:no*no
print(res(20))

val=lambda x:True if x%2==0 else False
for i in range(10):
    print(val(i))