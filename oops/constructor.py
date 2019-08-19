# class Student:
#     def __init__(self):
#         print("Hai i'm inside a Constructor")
#----------------------------------------------------------------------------------------------------------------------------------
class Student:
    def __init__(self,nam,rol):
        self.name=nam
        self.rol=rol
    def display(self):
        print("Name=",self.name)
        print("Roll No=",self.rol)
    def __str__(self):
        return self.name+str(self.rol)
obj=Student("Jen",23)
obj.display()
#-----------------------------------------------------------------------------------------------------------------------------------
print(obj)
