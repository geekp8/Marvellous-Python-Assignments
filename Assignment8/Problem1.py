import threading

def print_even():
    for i in range(2,21,2):
        print(f"Even:{i}")

def print_odd():
    for i in range(1,20,2):
        print(f"Odd:{i}")

#create threads
even_thread=threading.Thread(target=print_even)        
odd_thread=threading.Thread(target=print_odd)

#start threads

even_thread.start()
odd_thread.start()


#wait for both threads to finish

even_thread.join()
odd_thread.join()

