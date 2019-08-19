lst=[10,20,30,49,67,70]
# for i in lst:
#     if(i%2==0):
#         print(i)
def iseven(n):
    if(n%2==0):
        return True
    else:
        False
eve=list(filter(iseven,lst))
print(eve)
#or
eve=list(filter(lambda x:x%2==0,lst))
print(eve)

lst2=["sachin","sewag","yuvi","virat"]
name=list(filter(lambda str:str[0]=="s",lst2))
print(name)
