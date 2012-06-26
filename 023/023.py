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


def iter_abundant(top):
    for n in range(1, top+1):
        if sum(divisors(n)) > n:
            yield n


def run():
    top = 38123
    abset = set(iter_abundant(top))

    ret = 0
    for n in range(1, top+1):
        for a in range(1, n):
            if (a in abset) and (n-a in abset):
                break
        else:
            ret += n
    print(ret)




if __name__ == '__main__':
    run()

