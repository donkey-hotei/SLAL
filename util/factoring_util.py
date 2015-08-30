from functools import reduce
import operator

# euclid's algorithm for gcd


def gcd(x, y): return x if y == 0 else gcd(y, x % y)


def dumb_factor(x, primeset):
    """
    Input: x -> an integer
           primeset -> a set of prime numbers
    Output: a set of pairs (p_i, a_i) s.t. x is
            the product of p_i to the power of a_i

    If x can't be factored over the set of primes
    return an empty list.
    """
    factors = []
    for p in primeset:
        exponent = 0
        while x % p == 0:
            exponent = exponent + 1
            x = x // p
        if exponent > 0:
            factors.append((p, exponent))
    return factors if x == 1 else []


def primes(limit):
    """
    Input: limit -> an integer
    Output: a list of all primes in the range [0, .., limit]
    """
    primeset = set()
    a = [True] * limit  # initialize the primality list
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            primeset.add(i)
            for n in range(i * i, limit, i):  # mark factors as non-prime
                a[n] = False
    return primeset


def intsqrt(x):
    """
    Input: x -> an integer
    Output: the integer square root of x
    """
    L = 1  # low
    H = x  # high
    if H < L:
        L, H = H, L
    while H - L > 1:
        m = int((L + H) // 2)
        d = x // m
        if d > m:
            L = m
        else:
            H = m
    return L if L * L == x else H


def prod(factors):
    """
    Input: factors -> a list of factors
    Output: the product of those factors.
    """
    # 1 is the multiplicative identity
    return reduce(operator.mul, factors, 1)
