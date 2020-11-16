MORSE_CODE = {'..-.': 'F', '-..-': 'X', '...---...': 'SOS', '-.-.--': '!',
                     '.--.': 'P', '-': 'T', '..---': '2', '.-.-.-': '.',
                     '....-': '4', '-----': '0', '--...': '7',
                     '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                     '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                     '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                     '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                     '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                     '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}

def decode_bits(bits):
    # Accept 0's and 1's, return dots, dashes and spaces
    # return bits.replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')
    # print(bits)
    # tukar1 = bits.replace('1111110','-')             # ('110', '.')
    # print(tukar1)
    # tukar2 = tukar1.replace('110', '.')           # ('00','  ')
    # print(tukar2)
    # tukar3 = tukar2.replace('00',' ')            # ('0', ' ')
    # print(tukar3)
    # tukar4 = tukar3.replace('0', '')             # ('1111','-')
    # print(tukar4)
    # # tukar5 = tukar4.replace('-.','-')
    # # print(tukar5)
    # return tukar4.replace('  ', ' ')
    # return bits.replace('1111110','-').replace('110', '.').replace('00',' ').replace('0', '').replace('  ', ' ')
    if len(bits) > 3:
        bits = bits + '00'
        return bits.replace('1111110','-').replace('110', '.').replace('00',' ').replace('0', '').replace('  ', ' ').replace('0', '').replace('1', '')
    else:
        return bits.replace('111', '-').replace('101', '..').replace('1', '.').replace('0', '')

def decode_morse(morse_code):
    morse_code = morse_code.strip()
    text = ''
    for x in morse_code.split(' '):
        if x != '':
            text = text + MORSE_CODE[x]
        else:
            text = text + ' '
    return text.replace('  ', ' ')




class Test:
    def assert_equals(value, expected):
        from nose.tools import assert_equal
        try:
            assert_equal(value, expected)
            print('EQUAL   --> v =', value, " ==  x =", expected)
        except:
            print("Got = {}, Expected = {}".format(value, expected))
            print('UNEQUAL!! --> v =', value, " !=  x =", expected)

    @classmethod
    def describe(cls, param):
        print(param)

Test.describe("Example from description")
Test.assert_equals(decode_morse(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')), 'HEY JUDE')

Test.describe("Your own tests")
Test.assert_equals(decode_morse(decode_bits('1')), 'E')
Test.assert_equals(decode_morse(decode_bits('101')), 'I')
Test.assert_equals(decode_morse(decode_bits('10001')), 'EE')
Test.assert_equals(decode_morse(decode_bits('10111')), 'A')
Test.assert_equals(decode_morse(decode_bits('1110111')), 'M')
Test.assert_equals(decode_morse(decode_bits('111')), 'E')
Test.assert_equals(decode_morse(decode_bits('1111111')), 'E')
Test.assert_equals(decode_morse(decode_bits('111000111')), 'I')
Test.assert_equals(decode_morse(decode_bits('111110000011111')), 'I')
Test.assert_equals(decode_morse(decode_bits('111000000000111')), 'EE')
Test.assert_equals(decode_morse(decode_bits('01110')), 'E')

bit1 = '111111000000111111000000111111000000111111000000000000000000111111000000000000000000111111111111111111000000111111000000111111111111111111000000111111111111111111000000000000000000000000000000000000000000111111000000111111111111111111000000111111111111111111000000111111111111111111000000000000000000111111000000111111000000111111111111111111000000000000000000111111111111111111000000111111000000111111000000000000000000111111'
Test.assert_equals(decode_morse(decode_bits(bit1)), 'HEY JUDE')

bit2 = '00011100010101010001000000011101110101110001010111000101000111010111010001110101110000000111010101000101110100011101110111000101110111000111010000000101011101000111011101110001110101011100000001011101110111000101011100011101110001011101110100010101000000011101110111000101010111000100010111010000000111000101010100010000000101110101000101110001110111010100011101011101110000000111010100011101110111000111011101000101110101110101110'
Test.assert_equals(decode_morse(decode_bits(bit1)), 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')

bit3 = '11111111111111100000000000000011111000001111100000111110000011111000000000000000111110000000000000000000000000000000000011111111111111100000111111111111111000001111100000111111111111111000000000000000111110000011111000001111111111111110000000000000001111100000111110000000000000001111111111111110000011111000001111111111111110000011111000000000000000111111111111111000001111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000111110000000000000001111100000111111111111111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111111111111111000001111111111111110000000000000001111111111111110000011111000000000000000000000000000000000001111100000111110000011111111111111100000111110000000000000001111111111111110000011111111111111100000111111111111111000000000000000111111111111111000001111100000111110000011111111111111100000000000000000000000000000000000111110000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111111111111100000000000000011111111111111100000111111111111111000000000000000111110000011111111111111100000111111111111111000001111100000000000000011111000001111100000111110000000000000000000000000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111000001111111111111110000000000000001111100000000000000011111000001111111111111110000011111000000000000000000000000000000000001111111111111110000000000000001111100000111110000011111000001111100000000000000011111000000000000000000000000000000000001111100000111111111111111000001111100000111110000000000000001111100000111111111111111000000000000000111111111111111000001111111111111110000011111000001111100000000000000011111111111111100000111110000011111111111111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111111111111110000011111111111111100000111110000000000000001111100000111111111111111000001111100000111111111111111000001111100000111111111111111'
Test.assert_equals(decode_morse(decode_bits(bit1)), 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')
#
