#!/usr/bin/env python3

digits = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]

decades = {
        10: 3,
        11: 6,
        12: 6,
        13: 8,
        14: 8,
        15: 7,
        16: 7,
        17: 9,
        18: 8,
        19: 8,
        20: 6,
        30: 6,
        40: 5,
        50: 5,
        60: 5,
        70: 7,
        80: 6,
        90: 6,
        }


def word_len(n):
    if n < 10:
        return digits[n]
    elif n < 100:
        try:
            return decades[n]
        except KeyError:
            d, n = divmod(n, 10)
            return decades[d*10]+digits[n]
    elif n < 1000:
        c, n = divmod(n, 100)
        return [7, 10][n>0] + digits[c] + word_len(n)
    elif n == 1000:
        return 11


def run():
    print(sum(word_len(n) for n in range(1, 1001)))


if __name__ == '__main__':
    run()

