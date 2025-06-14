import schedule
import time
from datetime import datetime


def Display():
    print("Namaskar...")


schedule.every().day.at("09:00").do(Display)


while True:
    schedule.run_pending()
    time.sleep(1)
