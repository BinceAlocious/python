f=open("employee.txt","r")
lst2=[]
for i in f:
    lst2.append(i[:-1].split(","))
# sort=sorted(lst2,key=lambda k:k[2],reverse=True)
# print(sort)
# print("Employees Above Salary 19000:")
# for j in lst2:
#     if(int(j[2])>19000):
#         print(j)

class Employee:
    def __init__(self,id,name,sal,job):
        self.id=id
        self.name=name
        self.sal=sal
        self.job=job

# obj=Employee()
# obj2=Employee()
# obj3=Employee()
# obj4=Employee()
# obj5=Employee()
# lst=[obj,obj2,obj3,obj4,obj5]
emlst=[]  #to store list of Objects
leng=len(lst2)
for j in lst2:
    emlst.append(Employee(j[0],j[1],j[2],j[3]))
sort=sorted(emlst,key=lambda emp:emp.sal,reverse=True)
for k in sort:
    print(k.name,":",k.sal)
print("\nSalary Above 19000:")
fil=filter(lambda emp:int(emp.sal)>19000,emlst)
for l in fil:
    print(l.name,":",l.sal)