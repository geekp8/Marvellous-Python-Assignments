
from Arithmetic import Add,Sub,Mult,Div

def main():
    value1=int(input("Enter first number:"))
    value2=int(input("Enter second number:"))
    Result=0
    Result=Add(value1,value2)
    Result1=Sub(value1,value2)
    Result2=Mult(value1,value2)
    Result3=Div(value1,value2)
    print("Output:",Result)
    print("Output:",Result1)
    print("Output:",Result2)
    print("Output:",Result3)



if __name__=="__main__":
    main()
