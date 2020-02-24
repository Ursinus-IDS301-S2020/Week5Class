import numpy as np
import matplotlib.pyplot as plt
from LeapYear import is_a_leap_year

def days_in_month(month, leap):
    """
    Return the number of days in a month
    Parameters
    ----------
    month: int
        The month (starting at 0 for January)
    leap: boolean
        Whether it's a leap year
    """
    res = 31
    if month == 1:
        if leap:
            res = 29
        else:
            res = 28
    elif month < 7 and month % 2 == 1:
        res = 30
    elif month >= 7 and month % 2 == 0:
        res = 30
    return res

time = np.array([0], dtype=np.int32)
year = 1970
finished = False
## Counting the years
while not finished:
    elapsed = 3600*24 # Seconds in a day
    if is_a_leap_year(year):
        elapsed = elapsed*366
    else:
        elapsed = elapsed*365
    if time + elapsed >= 0:
        year = year + 1
        time = time + elapsed
    else:
        finished = True

## Count the months
month = 0
finished = False
leap = is_a_leap_year(year)
while not finished:
    days = days_in_month(month, leap)
    elapsed = days*24*3600
    if time + elapsed >= 0:
        month = month + 1
        time = time + elapsed
    else:
        finished = True
print(month)

## Count the days
day = 1
finished = False
while not finished:
    elapsed = 24*3600
    if time + elapsed >= 0:
        day = day + 1
        time = time + elapsed
    else:
        finished = True
print(day)