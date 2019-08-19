class Person:
    def setValues(self,nam,age,gen):
        self.nam=nam
        self.age=age
        self.gen=gen
    def display(self):
        print("Name=",self.nam)
        print("Age=",self.age)
        print("Gender=",self.gen)
class Employee(Person):
    cmpname="BPCL"
    def __init__(self,sal):
        self.sal=sal
    def income(self):
        print("Company=",Employee.cmpname)
        print("Salary=",self.sal)
obj=Employee(20000)
obj.setValues("John",44,"Male")
obj.display()
obj.income()

