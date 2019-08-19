tup=(1,2,3,4,7,3,"a")
print(tup)
# tup[0]=100  immutable

#insersion Order preserved

print(3 in tup)
tup2=(100,50)
employees=[(101,"Ayush",22,22000),(102,"John",29,23000),(103,"David",45,18000)]
for i in employees:
    print(i)
#to get only names
for i in employees:
    print(i[1])
for i in employees:
    if(i[3]>20000):
        print(i)
