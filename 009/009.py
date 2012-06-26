#!/usr/bin/env python3


def triplet(tot):
    for a in range(1, tot+1):
        for b in range(a+1, tot+1-a):
            c = 1000-b-a
            if a*a + b*b == c*c:
                return(a, b, c)


def run():
    a, b, c = triplet(1000)
    print(a*b*c)


if __name__ == '__main__':
    run()

