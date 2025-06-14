import schedule 
import time
from datetime import datetime

def Display():
    print("Lunch Time!")

def Display1():
    print("Wrap up work")    


def MySchedule():
    schedule.every().day.at("13:00").do(Display)
    schedule.every().day.at("18:00").do(Display1)

def main():
    MySchedule()

while True:    
    schedule.run_pending()
    time.sleep(1)

if __name__=="__main__":
    main()