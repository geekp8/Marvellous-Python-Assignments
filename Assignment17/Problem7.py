import schedule
import time
from datetime import datetime


def backup():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("backup_log.txt", "a") as log:
        log.write(f"[{now}] Backup completed.\n")
    print("Backup completed and logged.")



def main():
    schedule.every().hour.do(backup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()        



