from functools import reduce 

def Greater(numbers):
    return [num for num in numbers if num >=70]
    
Increase=lambda no:no+10   

Multiplication=lambda A,B:A*B


userinput=input("Input data:")    
inputData=[int(x) for x in userinput.split()] #square bracket for list

Result=Greater(inputData)
print("Nos greater than 70 are:",Result)


MData=list(map(Increase,Result))
print("List after map:",MData)

if MData:
    RData=reduce(Multiplication,MData)
    print("List after map:",RData)
