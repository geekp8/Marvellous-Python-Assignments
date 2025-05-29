import time
import multiprocessing
import threading

def SumAll(start,end):
    return sum(range(start,end))

def normal_sum():
    start_time=time.time()
    total=SumAll(1,10_000_001)
    end_time=time.time()

    print(f"Normal function Sum:{total},Time:{end_time-start_time:.4f}seconds")

def threadSum():
    start_time=time.time()
    total=0
    result=[0,0]

    