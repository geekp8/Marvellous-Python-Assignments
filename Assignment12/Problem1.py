class Demo:
    Value=0     #class variable
    def __init__(self,no1,no2):
        print("Inside constructor")
        self.no1=no1 #instance variables
        self.no2=no2 #instance variables

    def Fun(self):
            print(f"Fun method-> no1: {self.no1},no2:{self.no2},Value:{Demo.Value}")

    def Gun(self):
             print(f"Fun method-> no1: {self.no1},no2:{self.no2},Value:{Demo.Value}")


obj1=Demo(11,21)
obj2=Demo(51,101)

obj1.Fun()
obj2.Fun()

obj1.Gun()
obj2.Gun()


