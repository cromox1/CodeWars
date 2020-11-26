## https://www.codewars.com/kata/5235c913397cbf2508000048/train/python

class Calculator(object):
    def evaluate(self, string):
        return int(eval(string))

########### TDD

class Test:
    def assert_equals(value, expected):
        from nose.tools import assert_equal
        try:
            assert_equal(value, expected)
            print("EQUAL -- > Got = {}  ==  Expected = {} ".format(value, expected))
        except:
            print("UNEQUAL -- > Got = {}  !=  Expected = {} ".format(value, expected))

    @classmethod
    def describe(cls, param):
        print(param)

########### TDD TESTING SECTION

Test.describe("Sample tests")
Test.assert_equals(Calculator().evaluate("2 / 2 + 3 * 4 - 6"), 7)
Test.assert_equals(Calculator().evaluate("3 * 4 + 3 * 7 - 6"), 27)
Test.assert_equals(Calculator().evaluate('1 + 1'), 2)
Test.assert_equals(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )"), 2)
Test.assert_equals(Calculator().evaluate("( ( ( ( ( ( ( 5 ) ) ) ) ) ) )"), 5)
Test.assert_equals(Calculator().evaluate("2 * ( 2 * ( 2 * (2 * 1 ) ) )"), 16)
Test.assert_equals(Calculator().evaluate("3 * ( 4 + 7 ) - 6"), 27)