#!/usr/bin/env python3

def fibo_generator():
    term = 0
    p, n = 0, 1
    while True:
        term += 1
        yield term, n
        n, p = n+p, n


def run():
    thousand_digits = 10**999
    for term, n in fibo_generator():
        if n > thousand_digits:
            print(term)
            break


if __name__ == '__main__':
    run()

