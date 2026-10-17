from datetime import datetime
import time


def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def date_difference(date1, date2):
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def formatted_date():
    return datetime.now().strftime("%A, %d %B %Y")


def stopwatch(start_time):
    return time.time() - start_time


def countdown(seconds):
    while seconds > 0:
        print("Time left:", seconds, "seconds")
        time.sleep(1)
        seconds -= 1

    print("Countdown finished!")