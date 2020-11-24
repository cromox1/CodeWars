def next_bigger(n):
    nstring = str(n)
    # print(nstring)
    # chars = list(nstring)

    chars = [int(x) for x in list(nstring)]
    print(chars)
    print(sorted(chars))
    print([chars[x] - sorted(chars)[x] for x in range(len(chars))])

    lennstring = len(nstring)
    # print(n, lennstring, int(lennstring/2))
    if lennstring > 2:
        for i in range(-1, -(lennstring)+1, -1):
            chars = list(nstring)
            if nstring[i - 2] < nstring[i - 1] < nstring[i]:
                chars[i - 2], chars[i - 1], chars[i] = chars[i - 2], chars[i], chars[i - 1]
            elif nstring[i - 2] < nstring[i] < nstring[i - 1]:
                chars[i - 2], chars[i - 1], chars[i] = chars[i - 1], chars[i], chars[i - 2]
            elif nstring[i - 1] < nstring[i] < nstring[i - 2]:
                chars[i - 2], chars[i - 1], chars[i] = chars[i - 1], chars[i - 2], chars[i]
            elif nstring[i - 1] < nstring[i - 2] < nstring[i]:
                chars[i - 2], chars[i - 1], chars[i] = chars[i - 2], chars[i], chars[i - 1]
            elif nstring[i - 2] < nstring[i] < nstring[i - 1]:
                chars[i - 2], chars[i - 1], chars[i] = chars[i - 2], chars[i - 1], chars[i]
            else:
                return -1

            # if nstring[i] > nstring[i-1]:
            #     chars[i], chars[i-1] = chars[i-1], chars[i]
            # elif nstring[i-1] > nstring[i-2] and nstring[i] == nstring[i-1]:
            #     chars[i-1], chars[i-2] = chars[i-2], chars[i-1]
            # elif nstring[i-2] < nstring[i-1] < nstring[i] :
            #     chars[i], chars[i-1], chars[i-2] = chars[i], chars[i-2], chars[i-1]
            nstring = ''.join(chars)
            return int(nstring)
        # return -1
    elif lennstring == 2:
        chars = list(nstring)
        if chars[-1] != chars[-2]:
            chars[-1], chars[-2] = chars[-2], chars[-1]
            nstring = ''.join(chars)
            return int(nstring)
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
#### failed
# Test.assert_equals(next_bigger(1234567890),1234567908)
# Test.assert_equals(next_bigger(59884848459853),59884848483559)
# Test.assert_equals(next_bigger(80852318796877),80852318797678)
# Test.assert_equals(next_bigger(25087654),25405678)
Test.assert_equals(next_bigger(82174),82417)
Test.assert_equals(next_bigger(2964),4269)
Test.assert_equals(next_bigger(8890),8908)
Test.assert_equals(next_bigger(21652),22156)
Test.assert_equals(next_bigger(67651),71566)
Test.assert_equals(next_bigger(74965),75469)
Test.assert_equals(next_bigger(284),428)

