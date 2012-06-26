#!/usr/bin/env python3

import os


def run():
    names_txt = os.path.join(os.path.dirname(__file__), 'names.txt')
    names = sorted(n.strip('"') for n in open(names_txt).read().split(','))

    tot = 0
    for idx, name in enumerate(names, start=1):
        score = sum(ord(c)-ord('A')+1 for c in name) * idx
        tot += score

    print(tot)


if __name__ == '__main__':
    run()


