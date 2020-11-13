def valid_parentheses(string):
    depan = [i for i in range(len(string)) if string[i] == '(']
    belkg = [i for i in range(len(string)) if string[i] == ')']
    if len(depan) != len(belkg):
        return False
    else:
        for i in range(len(depan)):
            if depan[i] > belkg[i]:
                return False
        return True

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

Test.assert_equals(valid_parentheses("  ("),False)
Test.assert_equals(valid_parentheses(")test"),False)
Test.assert_equals(valid_parentheses(""),True)
Test.assert_equals(valid_parentheses("hi())("),False)
Test.assert_equals(valid_parentheses("hi(hi)()"),True)