def SumFactors(value):
    no=0
    value=int(input("Enter number:"))
    for i in range(1,value):
        if value % i ==0:
            no =no +i

    print("Output:",no)

number=0
SumFactors(number)   