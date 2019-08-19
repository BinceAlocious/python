class Employee:
    def __init__(self,id,sal,name):
        self.id=id
        self.sal=sal
        self.name=name
    def __str__(self):
        return self.name
        # return str(self.sal)

def getename(emp):
    return emp.name
obj1=Employee("A1900",20000,"Sara")
obj2=Employee("A1234",30000,"John")
obj3=Employee("A1233",10000,"Rahul")
obj4=Employee("A9088",24000,"Jen")
lst=[]
lst.append(obj1)
lst.append(obj2)
lst.append(obj3)
lst.append(obj4)
namesort=sorted(lst,key=getename,reverse=True)
for i in namesort:
    print(i)

#OR
name=sorted(lst,key=lambda emp:emp.sal,reverse=True)
for i in name:
    print(i)