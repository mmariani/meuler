#!/usr/bin/env python3

import itertools
import primes


def truncations(n):
    # also yields the whole number
    s = str(n)
    s1 = str(n)
    while s:
        yield int(s)
        s = s[1:]
    while s1:
        yield int(s1)
        s1 = s1[:-1]


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

