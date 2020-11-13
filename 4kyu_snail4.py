def snail(array):
    size = len(array)
    out = []
    if len(array[0]) != size:
        return []
    else:
        for step in range(1, 2 * size):
            if step == 1:
                nodenum = size
            else:
                nodenum = [x for x in range(size, 1, -1) for i in range(2)][step - 2]
            elements = chkelements(array, step, nodenum, size)
            for element in elements:
                out = addvaluetolist(out, element)
        return out

def chkelements(array, stepnum, side, size):
    if stepnum % 4 == 1:   # j increase
        ifix = int(stepnum / 4)
        jlow = size - int(stepnum / 4) - side
        jup = size - int(stepnum / 4)
        elements = []
        for j in range(jlow, jup):
            elements = elements + [array[ifix][j]]
        return elements
    elif stepnum % 4 == 2:   # i increase
        jfix = int(size - int(stepnum / 4) - 1)
        ilow = size - int(stepnum / 4) - side
        iup = size - int(stepnum / 4)
        elements = []
        for i in range(ilow, iup):
            elements = elements + [array[i][jfix]]
        return elements
    elif stepnum % 4 == 3:   # j decrease
        ifix = int(size - int(stepnum/4) - 1)
        jup = size - int(stepnum/4) - 1
        jlow = size - int(stepnum/4) - side -1
        elements = []
        for j in range(jup, jlow, -1):
            elements = elements + [array[ifix][j]]
        return elements
    elif stepnum % 4 == 0:  # i decrease
        jfix = int((stepnum/4) - 1)
        iup = size - int(stepnum/4)
        ilow = size - int(stepnum/4) - side
        elements = []
        for i in range(iup, ilow, -1):
            elements = elements + [array[i][jfix]]
        return elements

def addvaluetolist(listfinal, newvalue):
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
            print(' UNEQUAL !!!! // ### ')
            print('  v = ' + str(value))
            print('  x = ' + str(expected))
    @classmethod
    def describe(cls, param):
        print(param)

## TDD
array = [[1,2,3],[4,5,6],[7,8,9]]    ## 3 x 3
expected = [1,2,3,6,9,8,7,4,5]
Test.assert_equals(snail(array), expected)

array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]    ## 4 x 4
expected = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
Test.assert_equals(snail(array), expected)

array = [[1,2,3,4],[5,6,7,8],[6,7,8,9],[10,12,11,10]]    ## 4 x 4
expected = [1,2,3,4,8,9,10,11,12,10,6,5,6,7,8,7]
Test.assert_equals(snail(array), expected)

# array = [[1,2],[3,4]]    ## 2 x 2
# expected = [1,2,4,3]
# Test.assert_equals(snail(array), expected)
#
array = [[1,2,3],[8,9,4],[7,6,5]]     ## 3 x 3
expected = [1,2,3,4,5,6,7,8,9]
Test.assert_equals(snail(array), expected)

# array = [[1]]                          ## 1 x 1
# expected = [1]
# Test.assert_equals(snail(array), expected)
#
# array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]] ## 5 x 5
# expected = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
# Test.assert_equals(snail(array), expected)
#
# array = [[1, 2, 3, 4, 5, 6], [20, 21, 22, 23, 24, 7], [19, 32, 33, 34, 25, 8], [18, 31, 36, 35, 26, 9], [17, 30, 29, 28, 27, 10], [16, 15, 14, 13, 12, 11]]
# expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
# Test.assert_equals(snail(array), expected)
#
# array = [[632, 337, 530, 903, 853, 350], [28, 318, 219, 719, 952, 389], [719, 289, 644, 681, 838, 895], [633, 429, 249, 418, 209, 623], [274, 338, 973, 892, 46, 504], [877, 311, 597, 907, 609, 294]]
# expected = [632, 337, 530, 903, 853, 350, 389, 895, 623, 504, 294, 609, 907, 597, 311, 877, 274, 633, 719, 28, 318, 219, 719, 952, 838, 209, 46, 892, 973, 338, 429, 289, 644, 681, 418, 249]
# Test.assert_equals(snail(array), expected)
#
# array = [[719, 372, 84, 494, 745], [373, 382, 564, 816, 201], [887, 783, 474, 979, 708], [11, 593, 302, 875, 172], [500, 69, 648, 784, 941]]
# expected = [719, 372, 84, 494, 745, 201, 708, 172, 941, 784, 648, 69, 500, 11, 887, 373, 382, 564, 816, 979, 875, 302, 593, 783, 474]
# Test.assert_equals(snail(array), expected)
