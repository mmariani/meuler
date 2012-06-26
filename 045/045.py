#!/usr/bin/env python3

import itertools


# brute force, still under a minute

def run():
    p = set()
    h = set()
    for n in itertools.count(285):
        t = n*(n+1)//2
        p.add(n*(3*n-1)//2)
        h.add(n*(2*n-1))
        if {t} == set.intersection(p, h):
            break

    print(t)





if __name__ == '__main__':
    run()

