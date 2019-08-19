lst=[("Ajay",25000),("Sijo",20000),("Danie",4000),("Vishnu",18000)]
# print("Employees above Salary 19000 ")
# for i in lst:
#     if(i[1]>19000):
#         print(i[0])
#OR
emp=[name for (name,sal) in lst if sal>20000]
print(emp)

#To Count the no of employees Above Salary 20000

print(len(emp))