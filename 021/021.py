#!/usr/bin/env python3

import math


memo = {}


def _divisors(n):
    ret = set()
    for i in range(1, math.floor(math.sqrt(n)+1)):
        d, r = divmod(n, i)
        if not r:
            ret.add(i)
            ret.add(d)
    ret.discard(n)
    return ret


def divisors(n):
    try:
        return memo[n]
    except KeyError:
        memo[n] = _divisors(n)
        return memo[n]


def find_amicable(top):
    amicable = set()
    for n in range(1, top+1):
        if n in amicable:
            continue
        friend = sum(divisors(n))
        if friend == n:
            continue
        if n == sum(divisors(friend)):
            amicable.add(friend)
            amicable.add(n)
    return amicable


def run():
    print(sum(find_amicable(10000)))





if __name__ == '__main__':
    run()

