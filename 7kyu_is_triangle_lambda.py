is_triangle = lambda a,b,c: a < (b+c) and b < (a+c) and c < (a+b)

#### TDD TESTING
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

Test.describe('is_triangle')
# Test.it("works for some examples")
Test.assert_equals(is_triangle(1, 2, 2), True)
Test.assert_equals(is_triangle(7, 2, 2), False)
Test.assert_equals(is_triangle(1, 2, 3), False)
Test.assert_equals(is_triangle(1, 3, 2), False)
Test.assert_equals(is_triangle(3, 1, 2), False)
Test.assert_equals(is_triangle(5, 1, 2), False)
Test.assert_equals(is_triangle(1, 2, 5), False)
Test.assert_equals(is_triangle(2, 5, 7), False)
Test.assert_equals(is_triangle(2, 5, 6), True)
Test.assert_equals(is_triangle(4, 2, 3), True)
Test.assert_equals(is_triangle(5, 1, 5), True)
Test.assert_equals(is_triangle(2, 2, 2), True)
Test.assert_equals(is_triangle(-1, 2, 3), False)
Test.assert_equals(is_triangle(1, -2, 3), False)
Test.assert_equals(is_triangle(1, 2, -3), False)
Test.assert_equals(is_triangle(0, 2, 3), False)
Test.assert_equals(is_triangle(0, 2, 4), False)