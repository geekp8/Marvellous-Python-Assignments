def LargestNumber(no1,no2,no3):
    if(no1>no2):
        print("Largest number is:",no1)
    elif(no2>no1):
        print("Largest number is:",no2)
    elif(no2>no3):
        print("Largest number is:",no2) 
    elif(no3>no1):
        print("Largest number is:",no3)    
    elif(no3>no2):
        print("Largest number is:",no3)       

print("Enter 3 numbers:")
no1=int(input())
no2=int(input())
no3=int(input())

LargestNumber(no1,no2,no3)
        