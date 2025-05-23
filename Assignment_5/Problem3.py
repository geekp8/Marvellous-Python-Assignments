def VotingChecker(value):
    if value>18:
        print("Eligible to vote")
   

print("Enter age:") 
no=int(input())  

VotingChecker(no)
