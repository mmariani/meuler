#!/usr/bin/env python3

"""
Problem 35 without string conversions.
"""

import itertools
import math
import primes


def rotations(n):
    digits = math.ceil(math.log10(n))
    d = 10**(digits-1)
    for i in range(digits):
        yield n
        f, n = divmod(n, d)
        n = (n*10)+f


def run():
    # all primes below a million
    primeset = set(itertools.takewhile(lambda i:i<1000000, primes.eratosthenes()))
    print(len([n for n in primeset if set(rotations(n)).issubset(primeset)]))



if __name__ == '__main__':
    run()

