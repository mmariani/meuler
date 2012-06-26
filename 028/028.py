#!/usr/bin/env python3



def diagsum(n):
    # brute force
    ret = el = 1
    for i in range(1, n//2+1):
        for j in range(4):
            el += i*2
            ret += el
    return ret


def run():
    print(diagsum(1001))



if __name__ == '__main__':
    run()

