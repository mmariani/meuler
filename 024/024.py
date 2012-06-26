#!/usr/bin/env python3

def iter_permute(seq):
    if len(seq) == 1:
        yield seq
    for i in range(len(seq)):
        for p in iter_permute(seq[:i]+seq[i+1:]):
            yield seq[i] + p

def run():
    for idx, p in enumerate(iter_permute('0123456789'), start=1):
        if idx == 1000000:
            print(p)
            break


if __name__ == '__main__':
    run()

