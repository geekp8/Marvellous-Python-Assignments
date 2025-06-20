import os
import sys
import psutil
import logging
import getpass
from datetime import datetime
import smtplib
from email.message import EmailMessage


def SetupLogger(log_file):
    logging.basicConfig(filename=log_file,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')


def GetAllProcessInfo():
    info_list = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            info = proc.info
            info_list.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return info_list


def GetProcess(name):
    return [proc.info for proc in psutil.process_iter(['pid', 'name', 'username']) if proc.info['name'].lower() == name.lower()]


def SaveInfo(info_list, log_file):
    for info in info_list:
        logging.info(f"Name: {info['name']}, PID: {info['pid']}, User: {info['username']}")


def SendMail(log_file, to_email):
    msg = EmailMessage()
    msg['Subject'] = 'Process Info Log File'
    msg['From'] = 'pathakmana98@gmail.com'  
    msg['To'] = 'pathakmana98@gmail.com'

    msg.set_content('Attached is the log file containing process information.')

    with open(log_file, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='text', subtype='plain', filename=os.path.basename(log_file))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login('pathakmana98@gmail.com', 'Wishescometrue#7') 
            smtp.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")


def main():
    args = sys.argv
    if len(args) == 1:
        # Task 1
        log_file = "process_log.txt"
        SetupLogger(log_file)
        SaveInfo(GetAllProcessInfo(), log_file)
    elif len(args) == 2:
        # Task 2
        process_name = args[1]
        log_file = f"{process_name}_log.txt"
        SetupLogger(log_file)
        info = GetProcess(process_name)
        if info:
            SaveInfo(info, log_file)
        else:
            logging.info(f"No process found with name: {process_name}")
    elif len(args) == 3:
        # Task 3
        directory = args[2]
        os.makedirs(directory, exist_ok=True)
        log_file = os.path.join(directory, "process_log.txt")
        SetupLogger(log_file)
        SaveInfo(GetAllProcessInfo(), log_file)
    elif len(args) == 4:
        # Task 4
        directory = args[2]
        email = args[3]
        os.makedirs(directory, exist_ok=True)
        log_file = os.path.join(directory, "process_log.txt")
        SetupLogger(log_file)
        SaveInfo(GetAllProcessInfo(), log_file)
        SendMail(log_file, email)
    else:
        print("Invalid arguments.")

if __name__ == "__main__":
    main()
