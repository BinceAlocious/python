class One:
    def m1(self):
        print("Inside Method M1")
class Two:
    def m2(self):                         #if Same Method name then 1st arg inherited executed
        print("Inside Method M2")
class Three(Two,One):                  #Two Parent Clss
    def __init__(self):
        pass
obj=Three()
obj.m1()
obj.m2()
