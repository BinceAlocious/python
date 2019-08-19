# def sq(n):
#     lst=[]
#     for i in range(0,n+1):
#         sq=i*i
#         lst.append(sq)
#     print(lst)
# no=int(input("Enter Upper Limit: "))
# sq(no)

#or
#List Comprehension
square=[i**2 for i in range(1,101)]
print(square)