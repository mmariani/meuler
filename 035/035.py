#!/usr/bin/env python3

import itertools
import primes


def rotations(n):
    s = str(n)
    for i in range(len(s)):
        yield int(s)
        s = s[1:] + s[0]


def run():
    # all primes below a million
    primeset = set(itertools.takewhile(lambda i:i<1000000, primes.eratosthenes()))
    print(len([n for n in primeset if set(rotations(n)).issubset(primeset)]))



if __name__ == '__main__':
    run()

