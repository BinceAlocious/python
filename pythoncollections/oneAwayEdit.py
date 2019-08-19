str=input("Enter String 1: ")
str2=input("Enter String 2: ")
# lst=[i for i in str for j in str2 if i==j]
# s=len(str)
# l=len(lst)
# if(s-l==1):
#     print("True:One Away Edit")
# else:
#     print(False)
dict={}
for i in str:
    if(i not in dict):
        dict.update({i:1})
    else:
        count=dict[i]
        count+=1
        dict[i]=count
for j in str2:
    if(j not in dict):
        dict.update({j:1})
    else:
        co=dict[j]
        co+=1
        dict[j]=co
count2=0
for k in dict:
    if(dict[k]==1):
        count2+=1
if(count2==2):
    print("One Away Edit")
else:
    print("Not One Away Edit")
print(dict)