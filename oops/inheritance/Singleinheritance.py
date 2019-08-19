class Person:
    def setPerson(self,age,name,gender):
        self.age=age
        self.name=name
        self.gender=gender
    def displayPerson(self):
        print("Age=",self.age)
        print("Name=",self.name)
        print("Gender=",self.gender)

class Student(Person):   #here we define Student is a Person So this is ISA relationship
    school = "Luminar"
    def __init__(self,mk1,mk2):
        self.mk1=mk1
        self.mk2=mk2
    def cal(self):
        self.total=self.mk1+self.mk2
        print("Total=",self.total)
        print("School=",Student.school)

obj=Student(40,55)
obj.setPerson(12,"Jennifer","Female")
obj.displayPerson()
obj.cal()

