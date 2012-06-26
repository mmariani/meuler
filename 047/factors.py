
import collections
import itertools

import primes


# XXX slow start, and is the million enough?
primelist = list(itertools.takewhile(lambda n: n<1000000, primes.erat3()))

def factor_count(n):
    """
    returns a dictionary of {factor: times_occuring} for the number n
    """
    ret = collections.defaultdict(int)
    for p in itertools.takewhile(lambda p: p<=n, primelist):
        while not n % p:
            ret[p] += 1
            n = n // p
    return ret

