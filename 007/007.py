#!/usr/bin/env python3

import primes


def nth_prime(n):
    for idx, p in enumerate(primes.generate(), start=1):
        if idx==n:
            return p


def run():
    print(nth_prime(10001))


if __name__ == '__main__':
    run()

