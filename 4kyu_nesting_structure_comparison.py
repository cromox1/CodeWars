def same_structure_as(original,other):
    if type(original) == list and type(other) == list:
        for x in ['[',']']:
            if x in original:
                original.remove(x)
            if x in other:
                other.remove(x)
        asalstr = str(original).replace(' ', '')
        asallist = [[x for x in range(len(asalstr)) if asalstr[x] == '['],
                     [x for x in range(len(asalstr)) if asalstr[x] == ']']]
        lainstr = str(other).replace(' ', '')
        lainlist = [[x for x in range(len(lainstr)) if lainstr[x] == '['],
                     [x for x in range(len(lainstr)) if lainstr[x] == ']']]
        return asallist == lainlist
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
Test.assert_equals(same_structure_as([1,[1,1]],[2,[2,2]]), True)
Test.assert_equals(same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] ), True)
Test.assert_equals(same_structure_as([1,[1,1]],[[2,2],2]), False)
Test.assert_equals(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] ), False)
Test.assert_equals(same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] ), True)
Test.assert_equals(same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] ), False)
Test.assert_equals(same_structure_as([1,'[',']'], ['[',']',1] ), True)
Test.assert_equals(same_structure_as([],1), False)
Test.assert_equals(same_structure_as([],']['), False)

