num=int(input("Input:"))

if num > 1:
    for i in range(2,num):
        if num % i==0:
            print("It is not a Prime number")
            break
        else:
            print("It is a Prime number")


