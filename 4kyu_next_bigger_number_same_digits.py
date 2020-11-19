def next_bigger(n):
    nstring = str(n)
    for i in range(len(nstring)):
        print(nstring[i])


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