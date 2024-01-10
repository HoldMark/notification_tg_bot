import random
from datetime import datetime, date


def get_random_minute():
    return random.randint(1, 59)


def get_random_minute_with_condition(rlm: list, interval: int = 5):
    r = get_random_minute()
    while any(abs(r - i) < interval for i in rlm):
        r = get_random_minute()
    return r


def get_list_random_minutes(count: int = 7):
    rand_list = [get_random_minute()]

    for _ in range(count):
        rand_list.append(get_random_minute_with_condition(rand_list))

    return sorted(rand_list)


def get_schedule_for_today():
    year = date.today().year
    month = date.today().month
    day = date.today().day

    schedule = []

    for h in range(9, 18):
        for m in get_list_random_minutes():
            schedule.append(datetime(year=year, month=month, day=day, hour=h, minute=m, second=0))

    return schedule
