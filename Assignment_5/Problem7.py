def AreaCheck(no1,no2):
    Area=0
    Area=no1*no2
    print("Area:",Area)
    return Area
    


def Perimetercheck(no1,no2):
    Perimeter=0
    Perimeter=2*(no1+no2)
    print("Perimeter:",Perimeter)
    return Perimeter


value=int(input("Enter length:"))
value1=int(input("Enter width:"))

AreaCheck(value,value1)
Perimetercheck(value,value1)



