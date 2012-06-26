#!/usr/bin/env python3

import functools
import itertools
import factors

"""
Very brute force and inefficient solution.
"""


def find_consecutive(howmany):
    latest = [] # factors of the previous consecutive numbers
    for n in itertools.count(2):
        facn = factors.factor_count(n).items()
        if len(facn) != howmany:
            latest = []
            continue
        latest.append(set(facn))
        latest = latest[-howmany:]

        ## are they distinct?
        all_factors = functools.reduce(set.union, latest)
        if len(all_factors) == howmany**2:
            return n - howmany + 1


def run():
    print(find_consecutive(4))





if __name__ == '__main__':
    run()

