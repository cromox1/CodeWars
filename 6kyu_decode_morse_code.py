def decodeMorse(morse_code):
    MORSE_CODE = {'..-.': 'F', '-..-': 'X', '...---...': 'SOS', '-.-.--': '!',
                     '.--.': 'P', '-': 'T', '..---': '2', '.-.-.-': '.',
                     '....-': '4', '-----': '0', '--...': '7',
                     '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                     '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                     '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                     '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                     '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                     '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}

    morse_code = morse_code.strip()
    text = ''
    for x in morse_code.split(' '):
        if x != '':
            text = text + MORSE_CODE[x]
        else:
            text = text + ' '
    return text.replace('  ', ' ')

    # return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')



class Test:
    def assert_equals(value, expected):
        from nose.tools import assert_equal
        try:
            assert_equal(value, expected)
            print('EQUAL   --> v =', value, " ==  x =", expected)
        except:
            print("<pre style='display:inline'>Got {}, expected {}</pre>".format(value, expected))
            print('UNEQUAL!! --> v =', value, " !=  x =", expected)

    @classmethod
    def describe(cls, param):
        print(param)

Test.describe("Example from description")
Test.assert_equals(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')
Test.assert_equals(decodeMorse(' . '), 'E')
Test.assert_equals(decodeMorse('   .   .  '), 'E E')
Test.assert_equals(decodeMorse('       ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-   '), 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')

Test.describe("Your own tests")