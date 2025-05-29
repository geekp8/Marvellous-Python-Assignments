#Multiprocessing
#first square of numbers from list
#then write for multiprocessing

import multiprocessing
import multiprocessing.process

def square(numbers):
    for num in numbers:
        result=num **2
        print("Square of the given numbers is:",result)




def main():
    numlist=input("Enter list of numbers:")
    numbers=list(map(int,numlist.split()))#map needs two parameters one here is int and second is split
    #square(numbers)

    p1=multiprocessing.Process(target=square,args=(numbers,))#giving arguments remember give in brackets

    p1.start()


if __name__=="__main__":
    main()