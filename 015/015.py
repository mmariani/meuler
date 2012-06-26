#!/usr/bin/env python3


memo = {(1, 1): 2}

def count_paths(x, y):
    try:
        return memo[(x, y)]
    except KeyError:
        if x == 1:
            return count_paths(1, y-1) + 1
        if y == 1:
            return count_paths(x-1, 1) + 1
        paths = count_paths(x, y-1) + count_paths(x-1, y)
        memo[(x, y)] = paths
        return paths


def run():
    print(count_paths(20, 20))


if __name__ == '__main__':
    run()


