import random
from datetime import datetime, date


year = date.today().year
month = date.today().month
day = date.today().day

d1 = datetime(year=year, month=month, day=day, hour=12, minute=30, second=15)


def get_random_minute():
    return random.randint(1, 59)


def get_random_minute_with_condition(rlm):
    r = get_random_minute()
    while any(abs(r - i) < 5 for i in rlm):
        r = get_random_minute()
    return r


def get_list_random_minutes():
    rand_list = [get_random_minute()]

    for _ in range(4):
        rand_list.append(get_random_minute_with_condition(rand_list))

    return sorted(rand_list)


schedule = []

for h in range(9, 18):
    for m in get_list_random_minutes():
        schedule.append(datetime(year=year, month=month, day=day, hour=h, minute=m, second=0))

for i in schedule:
    print(i)
