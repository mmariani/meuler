#!/usr/bin/env python3


def run():
    ret = 0
    n = 2**1000
    while n:
        n, d = divmod(n, 10)
        ret += d
    print(ret)


if __name__ == '__main__':
    run()

