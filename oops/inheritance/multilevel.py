class One:
    def m1(self):
        print("Inside Method M1")
class Two(One):
    def m2(self):
        print("Inside Method M2")
class Three(Two):
    def __init__(self):
        pass
obj=Three()
obj.m1()
obj.m2()
