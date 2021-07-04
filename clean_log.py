import os

def clean_log():
    if os.stat('log.txt').st_size > 10000000:
        open('log.txt', 'w').close()