def rgb(r, g, b):
    int_to_hex = lambda number: "%0.2X" % number if (0 <= number <= 255) else '00' if number < 0 else 'FF'
    return int_to_hex(r) + int_to_hex(g) + int_to_hex(b)

# def int_to_hex(num):
#     if num <= 0:
#         num = 0
#     elif num >= 255:
#         num = 255
#     return "%0.2X" % num

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

# Test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
# Test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
# Test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
# Test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
# Test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")

Test.assert_equals(rgb(0,0,0),"000000")
Test.assert_equals(rgb(1,2,3),"010203")
Test.assert_equals(rgb(255,255,255), "FFFFFF")
Test.assert_equals(rgb(254,253,252), "FEFDFC")
Test.assert_equals(rgb(-20,275,125), "00FF7D")

Test.assert_equals(rgb(148, 0, 211), "9400D3")
Test.assert_equals(rgb(254,253,300), "FEFDFF")
