#factorial using recursion

Fact=1

def Factorial(no):
    global Fact
    if(no>1):
        Fact=Fact*no
        no=no-1
        Factorial(no)
    return Fact    


def main():
    print("Enter number:")
    no=int(input())
    Result=Factorial(no)
    print("Factorial of {} is: {}".format(no,Result))#Eg-output is Factorial of 5 is 120

if __name__=="__main__":
    main()    