def snail(array):
    size = len(array)
    out = []
    if len(array[0]) == size:
        matrixall = []
        nodenumlist = [x for x in range(size, 1, -1) for i in range(2)]
        for stepnum in range(1, 2 * size):
            if stepnum == 1:
                nodenum = size
            else:
                nodenum = nodenumlist[stepnum - 2]
            matrix = listnodes(stepnum, nodenum, size)
            for list in matrix:
                if list not in matrixall:
                    matrixall = matrixall + [list]
        for list in matrixall:
            out = out + [array[list[0]][list[1]]]
    return out

def listnodes(stepnum, nodenum, size):
    list = []
    if stepnum % 4 == 1:   # i fixed & j increase
        for j in range(size - int(stepnum / 4) - nodenum, size - int(stepnum / 4)):
            list = list + [[int(stepnum / 4), j]]
    elif stepnum % 4 == 2:   # i increase & j fixed
        for i in range(size - int(stepnum / 4) - nodenum, size - int(stepnum / 4)):
            list = list + [[i ,size - int(stepnum / 4) - 1]]
    elif stepnum % 4 == 3:   # i fixed & j decrease
        for j in range(size - int(stepnum/4) - 1, size - int(stepnum/4) - nodenum - 1, -1):
            list = list + [[size - int(stepnum/4) - 1, j]]
    elif stepnum % 4 == 0:  # i decrease & j fixed
        for i in range(size - int(stepnum/4), size - int(stepnum/4) - nodenum, -1):
            list = list + [[i ,int(stepnum/4) - 1]]
    return list


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

array = [[1,2],[3,4]]    ## 2 x 2
expected = [1,2,4,3]
Test.assert_equals(snail(array), expected)

array = [[1,2,3],[8,9,4],[7,6,5]]     ## 3 x 3
expected = [1,2,3,4,5,6,7,8,9]
Test.assert_equals(snail(array), expected)

array = [[1]]                          ## 1 x 1
expected = [1]
Test.assert_equals(snail(array), expected)

array = [[1,2,3],[7,8,9]]    ## 2 x 3
expected = []
Test.assert_equals(snail(array), expected)

array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]] ## 5 x 5
expected = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
Test.assert_equals(snail(array), expected)

array = [[1, 2, 3, 4, 5, 6], [20, 21, 22, 23, 24, 7], [19, 32, 33, 34, 25, 8], [18, 31, 36, 35, 26, 9], [17, 30, 29, 28, 27, 10], [16, 15, 14, 13, 12, 11]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
Test.assert_equals(snail(array), expected)

array = [[632, 337, 530, 903, 853, 350], [28, 318, 219, 719, 952, 389], [719, 289, 644, 681, 838, 895], [633, 429, 249, 418, 209, 623], [274, 338, 973, 892, 46, 504], [877, 311, 597, 907, 609, 294]]
expected = [632, 337, 530, 903, 853, 350, 389, 895, 623, 504, 294, 609, 907, 597, 311, 877, 274, 633, 719, 28, 318, 219, 719, 952, 838, 209, 46, 892, 973, 338, 429, 289, 644, 681, 418, 249]
Test.assert_equals(snail(array), expected)

array = [[719, 372, 84, 494, 745], [373, 382, 564, 816, 201], [887, 783, 474, 979, 708], [11, 593, 302, 875, 172], [500, 69, 648, 784, 941]]
expected = [719, 372, 84, 494, 745, 201, 708, 172, 941, 784, 648, 69, 500, 11, 887, 373, 382, 564, 816, 979, 875, 302, 593, 783, 474]
Test.assert_equals(snail(array), expected)

array = [['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']]    ## 4 x 4
expected = ['a','b','c','d','h','l','p','o','n','m','i','e','f','g','k','j']
Test.assert_equals(snail(array), expected)

array = [['a','b','d','e'],['c','b','a','f'],['d','x','f','g'],['h','i','j','k']]    ## 4 x 4
expected = ['a','b','d','e','f','g','k','j','i','h','d','c','b','a','f','x']
Test.assert_equals(snail(array), expected)

array = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42], [43, 44, 45, 46, 47, 48, 49]]
expected = [1, 2, 3, 4, 5, 6, 7, 14, 21, 28, 35, 42, 49, 48, 47, 46, 45, 44, 43, 36, 29, 22, 15, 8, 9, 10, 11, 12, 13, 20, 27, 34, 41, 40, 39, 38, 37, 30, 23, 16, 17, 18, 19, 26, 33, 32, 31, 24, 25]
Test.assert_equals(snail(array), expected)

array = [[35, 34, 33, 32, 31], [30, 29, 28, 27, 26], [25, 24, 23, 22, 21], [20, 19, 18, 17, 16], [15, 14, 13, 12, 11]]
expected = [35, 34, 33, 32, 31, 26, 21, 16, 11, 12, 13, 14, 15, 20, 25, 30, 29, 28, 27, 22, 17, 18, 19, 24, 23]
Test.assert_equals(snail(array), expected)