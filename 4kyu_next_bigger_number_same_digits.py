def next_bigger(n):
    chars = list(str(n))
    for i in range(n, int(''.join(sorted(chars, reverse=True))) + 1):
        if sorted(list(str(i))) == sorted(chars) and i > n:
            # print('n = ', n, ' / i = ', i)
            return i
            break
    return -1


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

Test.assert_equals(next_bigger(12),21)
Test.assert_equals(next_bigger(513),531)
Test.assert_equals(next_bigger(2017),2071)
Test.assert_equals(next_bigger(414),441)
Test.assert_equals(next_bigger(144),414)
Test.assert_equals(next_bigger(9),-1)
Test.assert_equals(next_bigger(111),-1)
Test.assert_equals(next_bigger(531),-1)
#### failed (previously - now passed !! )
Test.assert_equals(next_bigger(1234567890),1234567908)
Test.assert_equals(next_bigger(59884848459853),59884848483559)
Test.assert_equals(next_bigger(80852318796877),80852318797678)
Test.assert_equals(next_bigger(25087654),25405678)
Test.assert_equals(next_bigger(82174),82417)
Test.assert_equals(next_bigger(2964),4269)
Test.assert_equals(next_bigger(8890),8908)
Test.assert_equals(next_bigger(21652),22156)
Test.assert_equals(next_bigger(67651),71566)
Test.assert_equals(next_bigger(74965),75469)
Test.assert_equals(next_bigger(284),428)

