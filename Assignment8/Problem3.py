#import for using threads
import threading

def evenlist(numbers):
    #this part iterates through each numbers in list and check if num is even %2==0(remainder is 0)
    #sum is used a s function for adding all the numbers
    
    evenlistsum=sum(num for num in numbers if num %2==0)
    print("Sum of even numbers:",evenlistsum)        

def oddlist(numbers):
    #condition is opp to that of even as remainder is 1
    oddlistsum=sum(num for num in numbers if num%2!=0)
    print("Sum of odd numbers:",oddlistsum)

def main():
    #accepting list as input parameter
    numlist=input("Enter list of numbers:")
    numbers=list(map(int,numlist.split()))

    #creating threads
    #call them by passing arguments
    evenlistthread=threading.Thread(target=evenlist,args=(numbers,))
    oddlistthread=threading.Thread(target=oddlist,args=(numbers,))


    evenlistthread.start()#starts thread activity
    oddlistthread.start()


if __name__=="__main__":
    main()