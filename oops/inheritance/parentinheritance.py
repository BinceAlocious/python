class Parent:
    def phone(self):
        print("I have an Samsung")
    def bike(self):
        print("I have a Hero Honda")
class Child(Parent):
    def __init__(self):
        pass
    def phone(self):             #Parent Function Overridden
        print("I have an Iphone")
    # def bike(self):
    #     print("I have a Honda")


obj=Child()
obj.phone()
obj.bike()
