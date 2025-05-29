import os
import time
import multiprocessing

def fact(no):
    
    if(no==0):
        return 1
    return no*fact(no-1)

def main():
    

    numbers=input("Enter list of numbers:")
    numlist=list(map(int,numbers.split())) 
    
    # The multiprocessing.Pool class in Python provides a convenient way to parallelize the execution of a 
    # function across multiple input values,
    # distributing the input data across processes. This allows you to leverage multiple 
    # CPU cores for faster processing times.
    
    p = multiprocessing.Pool()
    result = p.map(fact,numlist)

    p.close()
    p.join()
    
    print(result)

   

if __name__ == "__main__":
    main()