class Circle:
    def __init__(self,rad):
        self.rad=rad
    def perimeter(self):
        self.pi=3.14
        self.per=2*self.pi*self.rad
    def area(self):
        self.ar=self.pi*self.rad*self.rad
    def display(self):
        print("Perimeter=",self.per)
        print("Area=",self.ar)

no=int(input("Enter the Radius of Cirlce: "))
obj=Circle(no)
obj.perimeter()
obj.area()
obj.display()
