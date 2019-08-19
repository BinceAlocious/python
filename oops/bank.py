class Bank:
    bname="SBT"
    def setValues(self,ac):
        # self.bname="SBT"
        self.minbal=3000
        self.acno=ac
        self.balance=self.minbal
    def withdrawal(self,amt):
        # self.amt=amt
        self.balance=self.balance+amt
        print("Bank_Name=",Bank.bname)
        print("Deducted_Amt=",amt)
        print("Balance=",self.balance)
        print("Account_No=",self.acno)
    def deposit(self,amt):
        # self.amt=amt
        self.balance=self.balance+amt
        print("Bank_Name=",Bank.bname)
        print("Amount_Added=",amt)
        print("Balance=",self.balance)
        print("Account_No=", self.acno)
    def balenq(self):
        print("Bank_Name=",Bank.bname)
        print("Minimum_Balance=", self.minbal)
        print("Account_No=", self.acno)
obj=Bank()
obj.setValues("AC12345")
obj.balenq()
obj.withdrawal(100)
obj.deposit(1500)
