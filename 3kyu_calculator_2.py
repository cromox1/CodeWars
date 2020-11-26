class Calculator(object):
    def evaluate(self, string):
        print('###############################')
        print(string)
        liststring = string.split(' ')
        liststring = [liststring[i][x] for i in range(len(liststring)) for x in range(len(liststring[i]))]
        print(liststring)
        frontclose = [i for i in range(len(liststring)) if liststring[i] == '(']
        backclose = [i for i in range(len(liststring)) if liststring[i] == ')']
        print(frontclose)
        print(backclose)
        sementara = 0
        newlist = []
        if len(frontclose) >= 1:
            for k in range(len(frontclose)):
                print(liststring[frontclose[-k-1] + 1 : backclose[k]])
                #try int(k)
                sementara = eval(''.join(liststring[frontclose[-k-1] + 1 : backclose[k]]))
                print(k, sementara)
            # print(liststring[frontclose[-1] + 1 : backclose[0]])
            # print(eval(''.join(liststring[frontclose[-1] + 1 : backclose[0]])))
            # sementara = eval(''.join(liststring[frontclose[-1] + 1 : backclose[0]]))
            return sementara
        else:
            return int(eval(string))

        print('front = ', frontclose, ' / back = ', backclose)

        return len(string.split(' '))

    def timdivsumsub(self, string):
        return eval(string)

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
# Test.assert_equals(Calculator().evaluate("3 * 4 + 3 * 7 - 6"), 27)
# Test.assert_equals(Calculator().evaluate('1 + 1'), 2)
Test.assert_equals(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )"), 2)
# Test.assert_equals(Calculator().evaluate("( ( ( ( ( ( ( 5 ) ) ) ) ) ) )"), 5)
Test.assert_equals(Calculator().evaluate("2 * ( 2 * ( 2 * (2 * 1 ) ) )"), 16)
# Test.assert_equals(Calculator().evaluate("3 * ( 4 + 7 ) - 6"), 27)