import schedule
import time
from datetime import datetime


def Log():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("Marvellous.txt", "a") as f:
        f.write(f"Current Time: {now}\n")

schedule.every(5).minutes.do(Log)

while True:
    schedule.run_pending()
    time.sleep(1)




