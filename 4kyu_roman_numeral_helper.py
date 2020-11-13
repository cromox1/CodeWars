"""TODO: create a RomanNumerals helper object

Task
Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
It should follow the API demonstrated in the examples below. Multiple roman numeral values will
be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most
digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M,
900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each
Roman symbol in descending order: MDCLXVI.

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000

Help
| Symbol | Value | |----------------| | I | 1 | | V | 5 | | X | 10 | | L | 50 | | C | 100 | | D | 500 | | M | 1000 |

"""

from nose.tools import assert_equal

class RomanNumerals:

    decode = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL",
                       10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

    def to_roman(numeral):
        try:
            if type(numeral) == int:
                roman = ''
                listkey = sorted(list(RomanNumerals.decode.keys()), reverse=True)
                while numeral >= listkey[0]:
                    numeral -= listkey[0]
                    roman += RomanNumerals.decode[listkey[0]]
                for i in range(1,len(listkey)):
                    while listkey[i] <= numeral < listkey[i-1]:
                        numeral -= listkey[i]
                        roman += RomanNumerals.decode[listkey[i]]
                message = str(numeral) + ' should == ' + roman
                return roman, message
        except:
            print('Not int -- ', numeral)

    def from_roman(roman):
        try:
            if type(roman) == str:
                numeral = 0 ; sort1 = []
                decode1 = {v:k for k,v in RomanNumerals.decode.items() if len(v) == 1}
                decode2 = {v:k for k,v in RomanNumerals.decode.items() if len(v) > 1}
                for xkey in decode2.keys():
                    if xkey in roman:
                        numeral += decode2[xkey]
                        roman = roman.replace(xkey, '')
                for kkey in roman:
                    numeral += decode1[kkey]
                    sort1.append(decode1[kkey])
                # check wheter roman given is valid
                sort2 = sorted(sort1, reverse=True)
                if sort1 != sort2:
                    message = ' // ERROR!! : ' + roman + ' is not in CORRECT order'
                else:
                    message = roman + ' should == ' + str(numeral)
                return numeral, message
        except:
            print('Not str -- ', roman)

class test:
    def assert_equalx(value, expected, message):
        try:
            assert_equal(value, expected, message)
            print('EQUAL   --> v =', value, " ==  x =", expected)
        except:
            print('UNEQUAL!! --> v =', value, " !=  x =", expected, message)

test.assert_equalx(RomanNumerals.to_roman(1000)[0], 'M', RomanNumerals.to_roman(1000)[1])
test.assert_equalx(RomanNumerals.to_roman(1990)[0], 'MCMXC', RomanNumerals.to_roman(1990)[1])
test.assert_equalx(RomanNumerals.to_roman(1666)[0], 'MDCLXVI', RomanNumerals.to_roman(1666)[1])
test.assert_equalx(RomanNumerals.to_roman(2008)[0], 'MMVIII', RomanNumerals.to_roman(2008)[1])
test.assert_equalx(RomanNumerals.to_roman(443)[0], 'CDXLIII', RomanNumerals.to_roman(443)[1])
test.assert_equalx(RomanNumerals.to_roman(4008)[0], 'MMMMVIII', RomanNumerals.to_roman(4008)[1])

test.assert_equalx(RomanNumerals.from_roman('XXI')[0], 21, RomanNumerals.from_roman('XXI')[1])
test.assert_equalx(RomanNumerals.from_roman('MMVIII')[0], 2008, RomanNumerals.from_roman('MMVIII')[1])
test.assert_equalx(RomanNumerals.from_roman('CM')[0], 900, RomanNumerals.from_roman('CM')[1])
test.assert_equalx(RomanNumerals.from_roman('IX')[0], 9, RomanNumerals.from_roman('IX')[1])
test.assert_equalx(RomanNumerals.from_roman('XIX')[0], 19, RomanNumerals.from_roman('XIX')[1])
test.assert_equalx(RomanNumerals.from_roman('XXI')[0], 21, RomanNumerals.from_roman('XXI')[1])
test.assert_equalx(RomanNumerals.from_roman('C')[0], 100, RomanNumerals.from_roman('C')[1])
test.assert_equalx(RomanNumerals.from_roman('D')[0], 500, RomanNumerals.from_roman('D')[1])
test.assert_equalx(RomanNumerals.from_roman('MM')[0], 2000, RomanNumerals.from_roman('MM')[1])
test.assert_equalx(RomanNumerals.from_roman('MCMXC')[0], 1990, RomanNumerals.from_roman('MCMXC')[1])
test.assert_equalx(RomanNumerals.from_roman('MMVIII')[0], 2008, RomanNumerals.from_roman('MMVIII')[1])
test.assert_equalx(RomanNumerals.from_roman('MDCLXVI')[0], 1666, RomanNumerals.from_roman('MDCLXVI')[1])
test.assert_equalx(RomanNumerals.from_roman('IIMDCLMXVI')[0], 0, RomanNumerals.from_roman('IIMDCLMXVI')[1])
# test.assert_equalx(RomanNumerals.from_roman('IIMDCLMXVI')[0], 2668, 'IIMDCLMXVI should == 0')

print(RomanNumerals.to_roman(5896)[0])
print(RomanNumerals.to_roman(5497)[0])
print(RomanNumerals.to_roman(3888)[0])
print(RomanNumerals.from_roman('IIMDCCCLXXXVIIM')[0], RomanNumerals.from_roman('IIMDCCCLXXXVIIM')[1])

# print()
#
# obj3 = tuple(str(i) if i%2==0 else i for i in range(30) if i%3 != 0 and i%5 != 0)
# obj3 = (str(i) if i%2==0 else i for i in range(30) if i%3 != 0 and i%5 != 0)
# print(obj3)
#
# for i in (int(x) for x in obj3):
#     print(RomanNumerals.to_roman(i))