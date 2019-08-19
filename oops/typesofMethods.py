class Student:
    schoolname="Luminar_Tech "
    def setValues(self,rol,nam,mark1,mark2,mark3):
        self.rol=rol
        self.nam=nam
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def displayValues(self):
        print("School Name=",Student.schoolname)
        print("Roll No=",self.rol)
        print("Name=",self.nam)
        print("Mark1=",self.mark1)
        print("Mark2=",self.mark2)
        print("Mark3=",self.mark3)
        print("Average Marks=",self.avg)
    def calavg(self):
        self.avg=(self.mark1+self.mark2+self.mark3)/3
    @classmethod #decorator
    def info(cls):
        cls.schoolname="Techno Lab "
    @staticmethod
    def staticMeth():
        print("inside Static Method ")

obj=Student()
obj.setValues(10,"Zack",90,70,60)
obj.calavg()
obj.displayValues()
obj2=Student()
obj2.setValues(10,"John",60,40,60)
obj2.calavg()
Student.info() #invoke clss method
Student.staticMeth() #invoke static Method
obj2.displayValues()

