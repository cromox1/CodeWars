from nose.tools import assert_equal

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

listprime1 = get_primes(450010)
# print(listprime1)
count = len(listprime1)
# print('count = ', count)
# print('n = ', len(listprime1))

def solve(a,b):
    sumprime = 0
    if b > a and b < 500000:
        # print(listprime1)
        # for ij in range(1, len(listprime1)+1):
        if b < count:
            range1 = b
        else:
            range1 = count
        # print('range1 = ', range1)
        for ij in range(1, range1 + 1):
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
Test_assert_equals(4000,450000,806250440)