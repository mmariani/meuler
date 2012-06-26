#!/usr/bin/env python3


def cfsum(n):
    # closed form summation
    return n*(n+1)//2


def run():
    m3 = cfsum(999//3)*3
    m5 = cfsum(999//5)*5
    m15 = cfsum(999//15)*15

    # inclusion-exclusion principle
    print(m3+m5-m15)


if __name__ == '__main__':
    run()

