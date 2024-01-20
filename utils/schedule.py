import random
import math
from datetime import datetime, date


# выдает радномную минуту
def rand_min() -> int:
    return random.randint(0, 59)


# отдает рандомную минуту, которая будет идти с определенным интервалом, для всех минут в списке
def rm_with_interval(rml: list, interval: int) -> int:

    rm = rand_min()

    while any(abs(rm - i) < interval for i in rml):
        rm = rand_min()

    return rm


# отдает массив рандомных минут с определенным интервалом
def get_rm_list(amount: int, interval: int) -> list:

    rm_list = [rand_min()]

    for _ in range(amount-1):
        rm_list.append(rm_with_interval(rm_list, interval))

    return sorted(rm_list)


# возвращает список со списком/списками минут с определенным интервалом для n-числа часов
def get_list_for_hours(hours: int, amount: int, interval: int) -> list:

    list_for_hours = [get_rm_list(amount, interval)]

    if hours > 1:
        for h in range(hours-1):

            next_hour = get_rm_list(amount, interval)
            first_minute = next_hour[0] + 60
            last_minute = list_for_hours[-1][-1]

            while first_minute - last_minute <= 5:
                next_hour = get_rm_list(amount, interval)
                first_minute = next_hour[0] + 60

            list_for_hours.append(next_hour)

    return list_for_hours


def get_schedule_for_period(amount, interval, start=9, end=18):

    year = date.today().year
    month = date.today().month
    day = date.today().day

    count = end - start

    list_for_hours = get_list_for_hours(count, amount, interval)

    schedule = []

    for num_list, hour in enumerate(range(start, end)):
        for minute in list_for_hours[num_list]:
            schedule.append(datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=0))

    return schedule
