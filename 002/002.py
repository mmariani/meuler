#!/usr/bin/env python3

def fibo_generator(top):
    p, n = 0, 1
    while n <= top:
        yield n
        n, p = n+p, n


def run():
    print(sum(x for x in fibo_generator(top=4e6) if x%2==0))


if __name__ == '__main__':
    run()

