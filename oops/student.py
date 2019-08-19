# class Student:
#     def displayDetails(self,name,rolno,clg):
#         self.name=name
#         self.rolno=rolno
#         self.clg=clg
#         print("Name=",self.name)
#         print("Roll No=",self.rolno)
#         print("College=",self.clg)
# obj=Student()
# obj.displayDetails("Zack",10,"MIT")
# obj1=Student()
# obj1.displayDetails("Jen",90,"Luminar")
class Student:
    def setValues(self,rol,nam,cl):
        self.rol=rol
        self.name=nam
        self.clg=cl
    def display(self):
        print("Roll No=",self.rol)
        print("Name=",self.name)
        print("College=",self.clg)
obj=Student()
obj.setValues(23,"Zack","MIT")
obj.display()

