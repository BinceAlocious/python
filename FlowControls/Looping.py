#While Loop
# i=0
# while(i<10):
#     print(i)
#     i+=1
#
# i=10
# while(i>=0):
#     print(i)
#     i-=1

#Print 0 to a range
# range=int(input("Enter Range "))
# i=0
# while(i<=range):
#     print(i)
#     i+=1

#Print nos from lower to upper limit

# low=int(input("Enter Lower Limit "))
# up=int(input("Enter Upper Limit "))
# i=low
# while(i<=up):
#     print(i)
#     i+=1

#Print Even nos to given Range

# range=int(input("Enter Range "))
# i=2
# while(i<=range):
#     print(i)
#     i+=2

#Reverse a no 123 to 321

no=int(input("Enter No to Reverse "))
res=0
while(no!=0):
    digit=no%10
    res=res*10+digit
    no=no//10
print(res)

