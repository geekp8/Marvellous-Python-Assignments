#Print numbers using recursion but first iteration

def Print(no):
    for i in range(1,no+1):
        print(i)



def main():
    
    print("Enter number")
    no=int(input())
    Print(no)


if __name__=="__main__":
    main()    
