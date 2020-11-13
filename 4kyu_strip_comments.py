def solution(string,markers):
    list1 = string.split('\n')
    print(list1)
    laststring = ''
    for m in markers:
        for sentence in list1:
            if m in sentence:
                string2 = sentence.split(m)
                print()
            else:
                string2 = sentence
        laststring = laststring + string2
    print(laststring)



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
Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
Test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")