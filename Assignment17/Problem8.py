import schedule
import time




def check_email():
    print("Checking mail...")

def scheduler():

    schedule.every(10).seconds.do(check_email)


def main():
    scheduler()


    # Scheduler loop
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()