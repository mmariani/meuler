#!/usr/bin/env python3


memo = {1: 0}

def seqlen(n):
    try:
        return memo[n]
    except KeyError:
        if n%2:
            memo[n] = seqlen(3*n+1)
        else:
            memo[n] = seqlen(n/2)
    return memo[n]+1



def run():
    topn, toplen = None, 0
    for n in range(1, 1000000):
        sl = seqlen(n)
        if sl > toplen:
            topn, toplen = n, sl

    print(topn)


if __name__ == '__main__':
    run()


