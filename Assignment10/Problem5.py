from functools import reduce 

def CheckPrime(n):
    return n > 1 and all(n % i != 0 for i in range(2, n))

Multiplication=lambda A:A*2

def Maximum(a,b):
    return max(a,b)


userinput=input("Input data:")    
inputData=[int(x) for x in userinput.split()] #square bracket for list

FData=list(filter(CheckPrime,inputData))
print("List after filter:",FData)


MData=list(map(Multiplication,FData))
print("List after map:",MData)

if MData:
    RData=reduce(Maximum,MData)
    print("List after reduce:",RData)
