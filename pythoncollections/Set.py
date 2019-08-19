
set=set()
print(type(set))
set={10,20,20,10,40}
print(set)
#insersion Order not preserved
set.add(105)
print(set)
print(set.pop())

days1={"Monday","Tuesday","Wednesday","Thursday"}
days2={"Friday","Saturday","Sunday"}
#union
print(days1|days2)
#or
print(days1.union(days2))

#intersection
set1={1,2,5,7,8}
set2={3,4,5,9,8}
print(set1&set2)
#or
print(set1.intersection(set2))

#Difference

print(set1-set2)

college={"Sachin","Ayush","John","Ron","Jacob"}
failed={"Ayush","Rahul","Ron"}
passed=college-failed
print(passed)