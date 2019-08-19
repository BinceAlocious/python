class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):    #Magic methods(Special Methods)
        bk=Book(self.pages+other.pages)
        return bk
    def __str__(self):
        return str(self.pages)
    def __sub__(self,other):
        return self.pages-other.pages
    def __mul__(self,other):
        return self.pages*other.pages
    def __truediv__(self, other):
        return self.pages/other.pages

obj1=Book(23)
obj2=Book(30)
obj3=Book(20)
print(obj1+obj2+obj3)
print(obj1-obj2)
print(obj1*obj2)
print(obj1/obj2)

