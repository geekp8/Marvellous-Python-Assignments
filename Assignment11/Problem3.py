#reursive function to calculate Sum of digits of a number

def Total(no):
   return sum(no)

# def Total(no):
#     if not no:  # Base case: empty list
#         return 0
#     return no[0] + Total(no[1:])  # Recursive case

        

def main():
    print("Enter numbers for addition")
    #no=int(input())
    no=list(map(int,input().split()))#taking list as input with map

    Result=Total(no)
    print("Addition is:",Result)

if __name__=="__main__":
    main()      