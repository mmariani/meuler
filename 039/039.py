#!/usr/bin/env python3

import collections

"""
Very brute force and inefficient (still under a minute)
"""

def run():
    triangles = collections.defaultdict(int)
    for p in range(1, 1000):
        for a in range(1, p//2):
            for b in range(a+1, p-a-1):
                if (a*a+b*b)**.5 == p-a-b:
                    triangles[p] += 1

    print([k for k,v in triangles.items() if v==max(triangles.values())][0])





if __name__ == '__main__':
    run()

