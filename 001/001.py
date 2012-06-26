#!/usr/bin/env python3

def run():
    # brute force
    print(sum(x for x in range(1000) if not x%3 or not x%5))


if __name__ == '__main__':
    run()

