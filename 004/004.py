#!/usr/bin/env python3

def ispali(n):
    return  str(n) == ''.join(reversed(str(n)))


def run():
    pali = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            mul = i*j
            if mul>pali and ispali(mul):
                pali = mul
    print(pali)


if __name__ == '__main__':
    run()

