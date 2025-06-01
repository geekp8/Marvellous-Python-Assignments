from functools import reduce 

def CheckEven(no):
    return no%2==0

Square=lambda A:A*A

Addition=lambda A,B:A+B

userinput=input("Input data:")    
inputData=[int(x) for x in userinput.split()] #square bracket for list

FData=list(filter(CheckEven,inputData))
print("Even numbers are:",FData)


MData=list(map(Square,FData))
print("List after map:",MData)

if MData:
    RData=reduce(Addition,MData)
    print("List after reduce:",RData)
