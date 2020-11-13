'''
Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Task:
Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).

Example:
dbl_linear(10) should return 22

Note:
Focus attention on efficiency
'''
### YOUR CODE
import bisect

def dbl_linear(n):
    u = [1]
    for i in range(n):
        x = u[i]
        y = (2 * x) + 1
        z = (3 * x) + 1

        ## Y
        x1 = len(u)
        for j in range(len(u)):
            if u[j] > y:
                if u[j - 1] < y:
                    xx = j
                    x1 = j
                    print('x1 = ', x1 , ' // y = ', y)
                    j = len(u)

                # break
                # break
                # j = len(u)
        if x1 < len(u):
            # print('x1 = ', x1)
            # print(u[:x1])
            # print(u[x1:])
            # u = u[:x1] + [y] + u[x1:]
            u[x1:x1] = [y]
        elif x1 == len(u):
            u = u + [y]

        ## Z
        x2 = len(u)
        for k in range(len(u)):
            if u[k] > z:
                if u[k - 1] < z:
                    x2 = k
                    print('x2 = ', x2 , ' // z = ' , z)
                    # break
                    # j = len(u)
                    k = len(u)
        if x2 < len(u):
            # print('x2 = ', x2)
            # print(u[:x2])
            # print(u[x2:])
            # u = u[:x2] + [z] + u[x2:]
            u[x2:x2] = [z]
        elif x2 == len(u):
            u = u + [z]

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