#!/usr/bin/env python3

def run():
    # bigint cheat
    tot = sum((n**n) for n in range(1, 1001))
    print('{:010d}'.format(tot%10**10))


if __name__ == '__main__':
    run()

