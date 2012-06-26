#!/usr/bin/env python3

import itertools
import primes

def run():
    print(sum(itertools.takewhile(lambda n:n<2e6, primes.generate())))


if __name__ == '__main__':
    run()

