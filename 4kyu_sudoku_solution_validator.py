def valid_solution(array):
    size = len(array)
    if len(array[0]) == size and len(array[-1]) == size and size == 9:
        result = 1
        for i in range(size):
            column = [array[x][i] for x in range(size)]
            for k in range(1, size + 1):
                if k not in array[i]:
                    result = result * 0
                elif k not in column:
                    result = result * 0
            if sorted(column) == column:
                result = result * 0
        return result == 1
    else:
        return False

### TDD
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

    @classmethod
    def it(cls, param):
        print(param)


## Testing
array1 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]]
Test.assert_equals(valid_solution(array1), True)

array2 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 0, 3, 4, 9],
        [1, 0, 0, 3, 4, 2, 5, 6, 0],
        [8, 5, 9, 7, 6, 1, 0, 2, 0],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 0, 1, 5, 3, 7, 2, 1, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 0, 0, 4, 8, 1, 1, 7, 9]]
Test.assert_equals(valid_solution(array2), False)

array3 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 0, 3, 4, 8],
        [1, 0, 0, 3, 4, 2, 5, 6, 0],
        [8, 5, 9, 7, 6, 1, 0, 2, 0],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 0, 1, 5, 3, 7, 2, 1, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 0, 0, 4, 8, 1, 1, 7, 9]]
Test.assert_equals(valid_solution(array3), False)

array4 = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
          [4, 9, 8, 2, 6, 1, 3, 7, 5],
          [7, 5, 6, 3, 8, 4, 2, 1, 9],
          [6, 4, 3, 1, 5, 8, 7, 9, 2],
          [5, 2, 1, 7, 9, 3, 8, 4, 6],
          [9, 8, 7, 4, 2, 6, 5, 3, 1],
          [2, 1, 4, 9, 3, 5, 6, 8, 7],
          [3, 6, 5, 8, 1, 7, 9, 2, 4],
          [8, 7, 9, 6, 4, 2, 1, 3, 5]]
Test.assert_equals(valid_solution(array4), False)

array5 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
          [2, 3, 4, 5, 6, 7, 8, 9, 1],
          [3, 4, 5, 6, 7, 8, 9, 1, 2],
          [4, 5, 6, 7, 8, 9, 1, 2, 3],
          [5, 6, 7, 8, 9, 1, 2, 3, 4],
          [6, 7, 8, 9, 1, 2, 3, 4, 5],
          [7, 8, 9, 1, 2, 3, 4, 5, 6],
          [8, 9, 1, 2, 3, 4, 5, 6, 7],
          [9, 1, 2, 3, 4, 5, 6, 7, 8]]
Test.assert_equals(valid_solution(array5), False)