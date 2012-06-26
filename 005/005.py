#!/usr/bin/env python3

import collections
import itertools
import primes


def factor_count(n):
    """
    returns a dictionary of {factor: times_occuring} for the number n
    """
    ret = collections.defaultdict(int)
    for p in itertools.takewhile(lambda p: p<=n, primes.generate()):
        while not n % p:
            ret[p] += 1
            n = n // p
    return ret


def run():
    factors = collections.defaultdict(int)
    for n in range(2, 21):
        for f, count in factor_count(n).items():
            factors[f] = max(factors[f], count)

    mul = 1
    for f in factors:
        mul *= f**factors[f]
    print(mul)


if __name__ == '__main__':
    run()

