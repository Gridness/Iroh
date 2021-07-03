import os
import datetime

def write_log(detailed, log_text):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if not os.path.exists('./log.txt'):
        log = open('log.txt', 'w')
    else:
        log = open('log.txt', 'a')
        
    if detailed:
        log.write(f'[{now.day}.{now.month}.{now.year} | {current_time}] {log_text}\n')
    else:
        log.write(f'[{current_time}] {log_text}\n')