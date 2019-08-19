#for "hai hello hai how are" you highest frequent word print
str="hai hello hai how are you"
lst=str.split(" ")
leng=len(lst)
# for i in range(0,leng):
#     for j in range(i+1,leng):
#         if(lst[i]==lst[j]):
#             lst2.append(lst[i])
lst2=[lst[i] for i in range(0,leng) for j in range(i+1,leng) if lst[i]==lst[j]]
print(lst2)
print("Count=",len(lst2))