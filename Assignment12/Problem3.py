class Arithmetic:

    def __init__(self):
        self.value1=0
        self.value2=0
        
    def Accept(self):
        self.value1=int(input("Enter value1 : "))
        self.value2=int(input("Enter value2 : "))

    def Addition(self):
        
        Result=self.value1+self.value2
        return Result

    def Substraction(self):
        
        Result=self.value1-self.value2
        return Result

    def Multiplication(self):
        Result=self.value1*self.value2
        return Result 
    
    def Division(self):
        Result=round(self.value1/self.value2,2)
        return Result


def main():
    obj1=Arithmetic()
    obj1.Accept()
    Result=obj1.Addition()
    Result1=obj1.Substraction()
    Result2=obj1.Multiplication()
    Result3=obj1.Division()

    print("Addition of numbers is:",Result)
    print("Substraction of numbers is:",Result1)
    print("Multiplication of numbers is:",Result2)
    print("Division of numbers is:",Result3)

if __name__=="__main__":
    main()    