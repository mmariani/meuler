#!/usr/bin/env python3

import itertools

def run():
    # stdlib cheat
    for idx, p in enumerate(itertools.permutations('0123456789'), start=1):
        if idx == 1000000:
            print(''.join(p))
            break


if __name__ == '__main__':
    run()

