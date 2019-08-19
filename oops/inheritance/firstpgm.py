class One:
    def m1(self):
        print("Inside Parent Method M1")
class Two(One):        #Inheritence
    def m2(self):
        print("Inside Child Method M2 ")

obj=Two()
obj.m1()
obj.m2()
