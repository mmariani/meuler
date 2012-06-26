#!/usr/bin/env python3

import itertools
import primes


def iter_factors(n):
    for p in itertools.takewhile(lambda p: p<=n, primes.generate()):
        while not n % p:
            yield p
            n = n // p


def run():
    print(max(iter_factors(600851475143)))


if __name__ == '__main__':
    run()

