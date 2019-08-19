class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return(self.a+self.b)
    def sub(self):
        return(self.a-self.b)
    def mul(self):
        return(self.a*self.b)
    def div(self):
        if(self.b!=0):
            return(self.a/self.b)
        else:
            print("MATH ERROR")
no1=int(input("Enter No1:"))
no2=int(input("Enter No2:"))
obj=Calc(no1,no2)
val=int(input("""Select any one operation:
                1.ADD:
                2.SUBTRACT:
                3.MULTIPLICATION:
                4.DIVISION:\n"""))
if(val==1):
    print("SUM=",obj.add())
elif(val==2):
    print("DIFFERENCE=",obj.sub())
elif(val==3):
    print("PRODUCT=",obj.mul())
elif(val==4):
    print("DIVIDENT=",obj.div())
else:
    print("Enter a Valid Input")
