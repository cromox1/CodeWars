from nose.tools import assert_equal
from pbkdf2 import xrange

def listprime(a,b):
    list = []
    for p in range(a, b+1):
        for i in range(2,p):
            if p % i == 0:
                break
        else:
            if p not in list and p > 1:
                list.append(p)
    return list

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def sundaram3(max_n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/2073279#2073279
    numbers = list(range(3, max_n+1, 2))
    half = (max_n)//2
    initial = 4
    for step in range(3, max_n+1, 2):
        for i in range(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

def GetPrimes3(n):
    Sieve = [1 for x in xrange(n)]
    for q in xrange (3, n, 2):
        k = q
        for y in xrange(k*k, n, k << 1):
            Sieve[y] = 0
    return Sieve

from itertools import compress

def half_sieve(n):
    """
    Returns a list of prime numbers less than `n`.
    """
    if n <= 2:
        return []
    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = bytearray((n - i * i - 1) // (2 * i) + 1)
    primes = list(compress(range(1, n, 2), sieve))
    primes[0] = 2
    return primes

from math import sqrt

def sieve(size):
    prime=[True]*size
    rng=xrange
    limit=int(sqrt(size))

    for i in rng(3,limit+1,+2):
        if prime[i]:
            prime[i*i::+i]=[False]*len(prime[i*i::+i])

    return [2]+[i for i in rng(3,size,+2) if prime[i]]

# print(sieve(100))

# allprime = listprime(1,450000)
# allprime = get_primes(450000)
# allprime = sundaram3(450000)
# allprime = GetPrimes3(450)
allprime = sieve(460000)
# print(allprime)

def primes(n):
    primfac = 0
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac += 1
            n //= d
        d += 1
    if n > 1:
       primfac += 1
    return primfac

listprime1 = primes(450)
print(listprime1)

def solve(a, b):
    sumprime = 0
    if b > a and b < 500000:
        # listprime1 = allprime
        # print(listprime1)

        for ij in range(1, b+1):
            if ij in listprime1 and listprime1[ij-1] >= a and listprime1[ij-1] <= b:
                sumprime += listprime1[ij-1]
                # print(ij, listprime1[ij-1])
    return sumprime

### TDD

def Test_assert_equals(a, b, expected):
    domprime = solve(a, b)
    try:
        # domprime = solve(a, b)
        assert_equal(domprime, expected)
        print('Equal   --> ', 'range(' + str(a) + ',' + str(b) + ')', " / ", domprime, " == ", expected, '(expected)')
    except:
        # domprime = solve(a, b)
        print('UNEQUAL --> ', 'range(' + str(a) + ',' + str(b) + ')', " / ", domprime, " != ", expected, '(expected)')

Test_assert_equals(0,10,8)
Test_assert_equals(6,20,28)
Test_assert_equals(2,200,1080)
Test_assert_equals(200,2000,48132)
Test_assert_equals(500,10000,847039)
# Test_assert_equals(4000,450000,806250440)