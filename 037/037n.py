#!/usr/bin/env python3

"""
Problem 37 without string conversions.
"""

import itertools
import math
import primes


def truncations(n):
    # also yields the whole number
    n1 = n
    while n1:
        yield n1
        n1 //= 10
    while n:
        yield n
        n = n % (10**math.floor(math.log10(n)))


def run():
    found = set()
    primeset = set()
    for p in primes.eratosthenes():
        primeset.add(p)
        if p <= 7:
            continue
        if set(truncations(p)).issubset(primeset):
            found.add(p)
            # the problems states there are only 11 such numbers
            if len(found) == 11:
                break
    print(sum(found))



if __name__ == '__main__':
    run()

