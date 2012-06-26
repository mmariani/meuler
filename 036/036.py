#!/usr/bin/env python3

import itertools
import math



def iter_pali():
    for n in range(1, 10**6):
        if str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[2::][::-1]:
            yield n


def run():
    tot = 0
    for n in iter_pali():
        tot += n
    print(tot)


if __name__ == '__main__':
    run()

