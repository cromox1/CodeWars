def next_smaller(n):
    from itertools import permutations
    print(n)
    chars = tuple(str(n))
    print(chars)
    index = sorted(list(set(permutations(chars, len(chars))))).index(chars)
    print(index)
    print(chars[index + 1])
    if int(''.join(chars[index + 1])) < n:
        return int(''.join(chars[index + 1]))
        # break
    return -1

    # return sorted(list(set(permutations(chars, len(chars))))).index(chars)[index + 1]

    # for xx in sorted(list(set(permutations(chars, len(chars)))), reverse=True):
    #     nexnum = int(''.join(xx))
    #     if nexnum < n:
    #         return nexnum
    #         break
    # return -1


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

    @classmethod
    def it(cls, param):
        print(param)

########### TDD TESTING SECTION

Test.it("Smaller numbers")
Test.assert_equals(next_smaller(907), 790)
Test.assert_equals(next_smaller(531), 513)
Test.assert_equals(next_smaller(135), -1)
Test.assert_equals(next_smaller(2071), 2017)
Test.assert_equals(next_smaller(414), 144)
Test.assert_equals(next_smaller(123456798), 123456789)
Test.assert_equals(next_smaller(123456789), -1)
Test.assert_equals(next_smaller(1234567908), 1234567890)
Test.assert_equals(next_smaller(9),-1)
Test.assert_equals(next_smaller(111),-1)
Test.assert_equals(next_smaller(513),351)
#### failed (previously - now passed !! )
Test.assert_equals(next_smaller(1234567890),1234567809)
Test.assert_equals(next_smaller(59884848459853),59884848459835)
Test.assert_equals(next_smaller(80852318796877),80852318796787)
Test.assert_equals(next_smaller(25087654),25087645)
Test.assert_equals(next_smaller(82174),82147)
Test.assert_equals(next_smaller(2964),2946)
Test.assert_equals(next_smaller(8890),8809)
Test.assert_equals(next_smaller(21652),21625)
Test.assert_equals(next_smaller(67651),67615)
Test.assert_equals(next_smaller(74965),74956)
Test.assert_equals(next_smaller(284),248)
Test.assert_equals(next_smaller(911111112),291111111)
Test.assert_equals(next_smaller(900000001),190000000)
Test.assert_equals(next_smaller(900000000001),190000000000)

