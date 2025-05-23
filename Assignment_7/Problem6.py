import math

def Prime(no):
    if no<=1:
        return False
    if no==2:
        return True
    if no % 2==0:
        return False
    return not any(no%i==0 for i in range(3,int(math.sqrt(no))+1,2))

number=list(map(int,input("Enter list:").split()))#remember split and how its used

primecheck=list(filter(Prime,number))
print("Prime numbers:",primecheck)