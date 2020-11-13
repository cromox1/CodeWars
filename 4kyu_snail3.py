def snail(snail_map):
    n = len(snail_map)

    out = []
    if len(snail_map[0]) != n:
        print('ERROR')
    else:
        for total in range(2*(n-1)):
            j = total
            i = total - j
            while i < n and j < n:
                out = outall(out, snail_map[i][j])
                j += 1


    return out

def outall(listfinal, newvalue):
    if newvalue not in listfinal:
        return listfinal + [newvalue]
    else:
        return listfinal


#### TDD TESTING
class Test:
    def assert_equals(value, expected):
        from nose.tools import assert_equal
        try:
            assert_equal(value, expected)
            print('EQUAL   --> got =', value, " ==  ex =", expected)
        except:
            message = ' // # ' + str(value) + ' should == ' + str(expected)
            print('UNEQUAL!! --> got =', value, " !=  ex =", expected, message)

    @classmethod
    def describe(cls, param):
        print(param)

## TDD
array = [[1,2,3],[4,5,6],[7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
Test.assert_equals(snail(array), expected)


array = [[1,2,3],[8,9,4],[7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
Test.assert_equals(snail(array), expected)
