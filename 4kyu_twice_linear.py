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

def dbl_linear(n):
    u = [1]
    for i in range(n):
        x = u[i]
        y = (2 * x) + 1
        z = (3 * x) + 1
        if y not in u:
            u.append(y)
        if z not in u:
            u.append(z)
    print(insertion_sort(u))
    return insertion_sort(u)[n]

def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = cursor
    return arr


        # if y not in u and len(u) > 3:
        #     for j in range(len(u)):
        #         if u[j] > y:
        #             break
        #     u = u[:j] + [y] + u[j:]
        # elif y not in u:
        #     u.append(y)
        #
        # if z not in u and len(u) > 3:
        #     for j in range(len(u)):
        #         if u[j] > z:
        #             break
        #     u = u[:j] + [z] + u[j:]
        # elif z not in u:
        #     u.append(z)

    print(u)
    #     if y not in u:
    #         u.append(y)
    #     if z not in u:
    #         u.append(z)
    # # print(u)
    # u = insertion_sort(u)
    # u.sort()
    # print(u)
    return u[n]

def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = cursor
    return arr

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