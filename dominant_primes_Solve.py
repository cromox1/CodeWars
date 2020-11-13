from nose.tools import assert_equal

# no 1
def solve(a, b):
    primes = [False,2] + [x for x in range(3, b+1, 2) if all(x % d for d in range(3, int(x**.5+1), 2))]
    dom_pos = [primes[x] for x in primes if x < len(primes)]
    return sum(x for x in dom_pos if a <= x <= b)

# no 2

n = 500000
sieve, PRIMES = [0]*(n//2+1), [0,2]
for i in range(3, n+1, 2):
    if not sieve[i//2]:
        PRIMES.append(i)
        for j in range(i**2, n+1, i*2): sieve[j//2] = 1

DOMINANTS = []
for p in PRIMES:
    if p >= len(PRIMES): break
    DOMINANTS.append(PRIMES[p])

def solve2(a,b):
    return sum(p for p in DOMINANTS if a <= p <= b)

# no3

def solve3(a, b):
    range_n = b + 1
    is_prime = [True] * range_n
    primes = [0]
    result = 0
    for i in range(2, range_n):
        if is_prime[i]:
            primes += i,
            for j in range(2 * i, range_n, i):
                is_prime[j] = False

    for i in range(2, len(primes)):
        if primes[i] >= a and is_prime[i]: result += primes[i]

    return result

# no 4

def solve4(a, b):
    arr = [0] * (b + 1)
    arr[0] = arr[1] = 1
    prime = []
    result = 0

    for num in range(b + 1):
        if (arr[num] == 0):
            i = num * 2
            prime.append(num)
            while (i <= b):
                arr[i] = 1
                i += num

    for idx in range(len(prime)):
        if (arr[idx + 1] == 0 and a <= prime[idx]):
            result += prime[idx]

    return result

# no 5

def solve5(start,n):
    prime = [True for i in range(n+1)]
    p=2
    while p*p <= n:
        if prime[p]:
            for i in range(p*2,n+1,p):
                prime[i]=False
        p+=1
    prime[0],prime[1]=False,False
    total=0
    position=0
    for i in range(n+1):
        if prime[i]:
            position+=1
            if prime[position] and i >=start:
                total+=i
    return total

# no 6

def list_simple_num(a):
    lst = list(range(a + 1))
    lst[1] = 0
    for l in lst:
        if l != 0:
            for j in range(2 * l, len(lst), l):
                lst[j] = 0
    return lst


def solve6(a, b):
    lst = tuple(filter(bool, list_simple_num(b)))
    ind = list_simple_num(len(lst))[1:]
    return sum(lst for ind, lst in zip(ind, lst) if ind != 0 and lst > a)

# to understand and try

def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int((n**0.5)+1),2):
        if n%i==0:
            return False
    return True
def solve99(a,b):
    p=[i for i in range(b+1) if is_prime(i)]
    s=0
    for i in range(len(p)):
        if is_prime((i+1)):
            if p[i]>a-1:
                s+=p[i]
    return s

### TDD

def Test_assert_equals(a, b, expected):
    domprime = solve6(a, b)
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
Test_assert_equals(4000,450000,806250440)