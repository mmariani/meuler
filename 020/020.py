#!/usr/bin/env python3

import operator
import functools


def run():
    ret = 0
    n = functools.reduce(operator.mul, range(1, 101))
    while n:
        n, d = divmod(n, 10)
        ret += d
    print(ret)


if __name__ == '__main__':
    run()

