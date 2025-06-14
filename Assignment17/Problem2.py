import schedule
import time
from datetime import datetime



def display_time():
    now = datetime.now()
    print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))


def main():
    schedule.every(1).minutes.do(display_time)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()        