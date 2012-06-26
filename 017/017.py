#!/usr/bin/env python3

digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

decades = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        }


def as_words(n):
    if n < 10:
        return digits[n]
    elif n < 100:
        try:
            return decades[n]
        except KeyError:
            d, n = divmod(n, 10)
            return decades[d*10]+'-'+digits[n]
    elif n < 1000:
        c, n = divmod(n, 100)
        return '%s hundred %s %s' % (digits[c], ['', 'and'][n>0], as_words(n))
    elif n == 1000:
        return 'one thousand'


def run():
    tot = 0
    for n in range(1, 1001):
        w = as_words(n)
        letters = w.replace(' ', '').replace('-', '')
        tot += len(letters)
    print(tot)


if __name__ == '__main__':
    run()

