def hex_string_to_RGB(hex_string):
    # your code here
    # pass
    hex_to_num = lambda hex: int(hex, 16)
    # print(hex_string[-6:-4], hex_string[-4:-2], hex_string[-2:])
    return {'r': hex_to_num(hex_string[-6:-4]), 'g': hex_to_num(hex_string[-4:-2]), 'b': hex_to_num(hex_string[-2:])}


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

Test.assert_equals(hex_string_to_RGB("#FF9933"), {'r':255, 'g':153, 'b':51})
Test.assert_equals(hex_string_to_RGB("#beaded"), {'r':190, 'g':173, 'b':237})
Test.assert_equals(hex_string_to_RGB("#000000"), {'r':0, 'g':0, 'b':0})
Test.assert_equals(hex_string_to_RGB("#111111"), {'r':17, 'g':17, 'b':17})
Test.assert_equals(hex_string_to_RGB("#Fa3456"), {'r':250, 'g':52, 'b':86})