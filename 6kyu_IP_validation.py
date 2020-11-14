'''
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Input to the function is guaranteed to be a single string.

Examples

Valid inputs:

1.2.3.4
123.45.67.89

Invalid inputs:

1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089

Note that leading zeros (e.g. 01.02.03.04) are considered invalid.
'''

def is_valid_IP(strng):
    if len(strng.split('.')) != 4:
        return False
    else:
        try:
            result = 1
            for ipx in strng.split('.'):
                if ' ' in ipx:
                    result = result * 0
                elif len(ipx) > 1 and ipx[0] == '0':
                    result = result * 0
                elif int(ipx) >= 0 and int(ipx) <= 255:
                    result = result * 1
                else:
                    result = result * 0
            return result == 1
        except:
            return False

## CLEVER SOLUTION FROM OTHER PEOPLE
# def is_valid_IP(s):
#     return len(s.split('.')) == 4 and False not in [(eval(i)>=0 and eval(i)<=255) for i in s.split('.')] if False not in [(a.isnumeric() and (a[0] != '0' or len(a) == 1)) for a in s.split('.')] else False

# is_valid_IP = lambda str: all(False if not(i.isdigit()) else False if "{}".format(int(i))!=i else int(i)>-1 and int(i)<256 for i in str.split('.')) and len(str.split('.'))==4

# def is_valid_IP(s):
#     return s.count('.') == 3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))

# def is_valid_IP(string):
#     return len([x for x in string.split('.') if x.isdigit() and 0 <= int(x) <= 255 and x.lstrip('0') == x]) == 4
# (not working for '0' but working for '045', '067' etc...

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

Test.assert_equals(is_valid_IP('12.255.56.1'),     True)
Test.assert_equals(is_valid_IP(''),                False)
Test.assert_equals(is_valid_IP('abc.def.ghi.jkl'), False)
Test.assert_equals(is_valid_IP('123.456.789.0'),   False)
Test.assert_equals(is_valid_IP('12.34.56'),        False)
Test.assert_equals(is_valid_IP('12.34.56 .1'),     False)
Test.assert_equals(is_valid_IP('12.34.56.-1'),     False)
Test.assert_equals(is_valid_IP('123.045.067.089'), False)
Test.assert_equals(is_valid_IP('127.1.1.0'),        True)
Test.assert_equals(is_valid_IP('0.0.0.0'),          True)
Test.assert_equals(is_valid_IP('0.34.82.53'),       True)
Test.assert_equals(is_valid_IP('192.168.1.300'),   False)