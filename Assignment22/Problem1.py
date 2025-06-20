import os
import sys
import time
import hashlib
import logging
import smtplib
from email.message import EmailMessage
from datetime import datetime


def SetupLogger(log_file):
    logging.basicConfig(filename=log_file,
                        level=logging.INFO,
                        format='%(asctime)s - %(message)s')


def HashFile(path, blocksize=65536):
    hasher = hashlib.sha1()
    try:
        with open(path, 'rb') as afile:
            buf = afile.read(blocksize)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(blocksize)
    except Exception as e:
        logging.warning(f"Could not read file {path}. Reason: {e}")
        return None
    return hasher.hexdigest()

def RemoveDuplicates(target_dir, log_file):
    scanned = 0
    duplicates = 0
    hash_dict = {}

    for foldername, subfolders, filenames in os.walk(target_dir):
        for filename in filenames:
            full_path = os.path.join(foldername, filename)
            scanned += 1
            file_hash = HashFile(full_path)
            if file_hash:
                if file_hash in hash_dict:
                    try:
                        os.remove(full_path)
                        logging.info(f"Deleted duplicate file: {full_path}")
                        duplicates += 1
                    except Exception as e:
                        logging.error(f"Error deleting {full_path}: {e}")
                else:
                    hash_dict[file_hash] = full_path

    return scanned, duplicates


def SendEmail(log_file, to_email, start_time, scanned, duplicates):
    msg = EmailMessage()
    msg['Subject'] = 'Duplicate File Removal Report'
    msg['From'] = 'pathakmana98@gmail.com'  # replace with sender email
    msg['To'] = to_email
    msg.set_content(f"""
Duplicate File Removal Report

Start Time: {start_time}
Total Files Scanned: {scanned}
Total Duplicate Files Removed: {duplicates}
    """)

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
    if len(sys.argv) != 4:
        print("Usage: DuplicateFileRemoval.py <Directory> <TimeIntervalInMinutes> <EmailID>")
        return

    target_dir = sys.argv[1]
    interval = int(sys.argv[2])
    email_id = sys.argv[3]

    if not os.path.isdir(target_dir):
        print("Invalid directory path.")
        return

    marvellous_dir = os.path.join(os.getcwd(), "Marvellous")
    os.makedirs(marvellous_dir, exist_ok=True)

    while True:
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file_name = f"Log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        log_file_path = os.path.join(marvellous_dir, log_file_name)
        SetupLogger(log_file_path)

        logging.info(f"Started duplicate file removal in: {target_dir}")
        scanned, duplicates = RemoveDuplicates(target_dir, log_file_path)

        SendEmail(log_file_path, email_id, start_time, scanned, duplicates)

        time.sleep(interval)

if __name__ == "__main__":
    main()
