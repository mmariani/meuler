
import collections
import itertools

import primes


def factor_count(n):
    """
    returns a dictionary of {factor: times_occuring} for the number n
    """
    ret = collections.defaultdict(int)
    for p in itertools.takewhile(lambda p: p<=n, primes.generate()):
        while not n % p:
            ret[p] += 1
            n = n // p
    return ret

