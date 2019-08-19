class Emp:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):     #Two String method         #Not given then Object Clss method invoked
        return self.name

obj=Emp("Jen",45)
print(obj)
