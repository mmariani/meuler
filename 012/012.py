#!/usr/bin/env python3

import functools
import itertools
import operator

import factors


def count_divisors(n):
    fdict = factors.factor_count(n)
    if not fdict:
        return 1
    return functools.reduce(operator.mul, (c+1 for c in fdict.values()))


def run():
    tri = 0
    for n in itertools.count(1):
        tri += n
        div = count_divisors(tri)
        if div > 500:
            print(tri)
            break


if __name__ == '__main__':
    run()

