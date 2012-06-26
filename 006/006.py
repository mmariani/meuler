#!/usr/bin/env python3

def run():
    sum_of_squares = sum(x**2 for x in range(1, 101))
    square_of_sums = sum(range(1, 101))**2
    print(square_of_sums-sum_of_squares)


if __name__ == '__main__':
    run()

