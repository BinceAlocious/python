list=[10,20,31,25,70]
print(list)
# n=len(list)
# for i in range(0,n):
#     if(list[i]%2==0):
#         print(list[i])
#         i+=1
#     else:
#         pass

list.append(5)
print(list)

for i in list:
    print(i)

even=[]
odd=[]
for i in list:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)
print("Odd Nos",len(odd))
print("Even Nos",len(even))

print(odd.count(5))

print(max(odd))

print(min(even))


