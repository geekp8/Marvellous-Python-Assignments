import threading

def display():
   
   for i in range(1,51):#start from 1 and end on 50(51 is not inclusive)
       print(i)


def display1():
   
   for i in range(50,0,-1):#start reverse with one decrease
       print(i)

def main():
    thread1=threading.Thread(target=display)
    thread2=threading.Thread(target=display1)

    thread1.start()
    thread1.join()
    print("-----------------------")
    thread2.start()
    thread2.join()


if __name__=="__main__":
    main()    

