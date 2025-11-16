import datetime

def time_until_jan1():
    now = datetime.datetime.now()
    next_year = now.year + 1

    jan_1 = datetime.datetime(next_year, 1, 1)
    remaining = jan_1 - now

    print("Time left until January 1st:", remaining)

time_until_jan1()
