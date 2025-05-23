def CheckEvenOdd(value):
    if value %2==0:
        print("Number is even:",value)
    else:
        print("Number is odd:",value)

print("Enter a number:")
no=int(input())

CheckEvenOdd(no)
