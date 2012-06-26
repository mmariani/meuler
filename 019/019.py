#!/usr/bin/env python3

import calendar
import itertools
import operator

def run():
    # cheating :)
    sundays = sum(calendar.weekday(year, month, 1) == calendar.SUNDAY
                    for year in range(1901, 2001)
                    for month in range(1, 13))

    print(sundays)


if __name__ == '__main__':
    run()

