#import for using threads
import threading

def small(userparam):
    
    
    count=sum(1 for char in userparam if char.islower())
    print("Total small characters in the string are:",count) 
    currentthread=threading.current_thread()
    print(f"Thread id: { currentthread.ident},Thread name:{ currentthread.name}")
    #print(f"Total small char :{smallstring}")        

def capital(userparam):
    #condition is opp to that of even as remainder is 1
    count=sum(1 for char in userparam if char.isupper())#python doesnt have iscapital it has isupper
    print("Total capital characters in the string are:",count)
    currentthread=threading.current_thread()
    print(f"Thread id: { currentthread.ident},Thread name:{ currentthread.name}")


def digits(userparam):
    #input=int(userparam)
    count=sum(1 for char in userparam if char.isdigit())#use to check if char is having digits isdigit
    print("Total digits are:",count)    
    currentthread=threading.current_thread()
    print(f"Thread id: { currentthread.ident},Thread name:{ currentthread.name}")

def main():
    #accepting string as input parameter
    userparam=input("Enter string as parameter:")


    #creating threads
    #call them by passing arguments
    smallthread=threading.Thread(target=small,args=(userparam,))
    capitalthread=threading.Thread(target=capital,args=(userparam,))
    digitsthread=threading.Thread(target=digits,args=(userparam,))


    smallthread.start()#starts thread activity
    capitalthread.start()
    digitsthread.start()


if __name__=="__main__":
    main()