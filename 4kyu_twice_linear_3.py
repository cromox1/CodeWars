def dbl_linear(n):
    u = [1]*3
    i = 0
    while i < n:
        x = u[i]
        y = (2 * x) + 1
        z = (3 * x) + 1
        ## u[0], u[1], u[2]
        u[0] = 1
        u[1] = (2 * u[0]) + 1
        u[2] = (3 * u[0]) + 1
        # u = u + [y] + [z]
        if i > 2:
            ## Y
            x1 = len(u)
            j = 2
            while j < len(u):
                if u[j] > y:
                    if u[j - 1] < y:
                        x1 = j
                        print('x1 = ', x1, ' // y = ', y)
                        j = len(u)
                j = j + 1
            if x1 < len(u):
                u[x1:x1] = [y]
            elif x1 == len(u):
                u = u + [y]
            ## Z
            x2 = len(u)
            k = 2
            while k < len(u):
                if u[k] > z:
                    if u[k - 1] < z:
                        x2 = k
                        print('x2 = ', x2, ' // z = ', z)
                        k = len(u)
                k = k + 1
            if x2 < len(u):
                u[x2:x2] = [z]
            elif x2 == len(u):
                u = u + [z]
        i = i + 1



    print(u)
    return u[n]


### TDD
class Test:
    def assert_equals(value, expected):
        from nose.tools import assert_equal
        try:
            assert_equal(value, expected)
            print('EQUAL   --> v =', value, " ==  x =", expected)
        except:
            message = ' // # ' + str(value) + ' should == ' + str(expected)
            print('UNEQUAL!! --> v =', value, " !=  x =", expected, message)

    @classmethod
    def describe(cls, param):
        print(param)

    @classmethod
    def it(cls, param):
        print(param)

Test.describe("dbl_linear")
Test.it("Basic tests")
Test.assert_equals(dbl_linear(10), 22)
Test.assert_equals(dbl_linear(20), 57)
# Test.assert_equals(dbl_linear(30), 91)
# Test.assert_equals(dbl_linear(50), 175)