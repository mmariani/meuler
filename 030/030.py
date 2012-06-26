#!/usr/bin/env python3

import itertools
import math


class BoundaryExceeded(Exception):
    pass



def sumn(n):
    tot = 0
    p10 = int(math.log(n, 10))
    while n:
        n, d = divmod(n, 10)
        tot += d**5
    if 9**5*(p10+1) < 10**p10:
        # we found them all already
        raise BoundaryExceeded
    return tot



def run():
    tot = 0
    # brute force
    try:
        for n in itertools.count(10):
            if n == sumn(n):
                tot += n
    except BoundaryExceeded:
        print(tot)


if __name__ == '__main__':
    run()

