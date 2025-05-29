import threading
import time


def display():
    for i in range(1,6):
        print(i)

def display1():
    for i in range(1,6):
        print(i)

def display3():
    for i in range(1,6):
        print(i)


def main():
    #create threads first

    thread1=threading.Thread(target=display)
    time.sleep(1)
    thread2=threading.Thread(target=display1)
    time.sleep(1)
    thread3=threading.Thread(target=display3)
    time.sleep(1)

    
    thread1.start()
    thread2.start()
    thread3.start()



if __name__=="__main__":
    main()                        
