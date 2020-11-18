MORSE_CODE = {'..-.': 'F',
              '-..-': 'X',
              '...---...': 'SOS',
              '-.-.--': '!',
              '.--.': 'P',
              '-': 'T',
              '..---': '2',
              '.-.-.-': '.',
              '....-': '4',
              '-----': '0',
              '--...': '7',
              '...-': 'V',
              '-.-.': 'C',
              '.': 'E',
              '.---': 'J',
              '---': 'O',
              '-.-': 'K',
              '----.': '9',
              '..': 'I',
              '.-..': 'L',
              '.....': '5',
              '...--': '3',
              '-.--': 'Y',
              '-....': '6',
              '.--': 'W',
              '....': 'H',
              '-.': 'N',
              '.-.': 'R',
              '-...': 'B',
              '---..': '8',
              '--..': 'Z',
              '-..': 'D',
              '--.-': 'Q',
              '--.': 'G',
              '--': 'M',
              '..-': 'U',
              '.-': 'A',
              '...': 'S',
              '.----': '1'}

CODE_MORSE = {v:k for k,v in MORSE_CODE.items()}

bitx1 = '0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000'
expx1 = 'HEY JUDE'

bits = bitx1
print(bits)
bits = bits.strip('0')
print(bits)

onezero = [i + 1 for i in range(len(bits) - 1) if bits[i] + bits[i + 1] == '10']
zeroone = [i + 1 for i in range(len(bits) - 1) if bits[i] + bits[i + 1] == '01']
print(onezero)
print(zeroone)
onezero_org = onezero + [len(bits)]
zeroone_org = [0] + zeroone
print(onezero_org)
print(zeroone_org)
oneloccount = {zeroone_org[i]: onezero_org[i] - zeroone_org[i] for i in range(len(zeroone_org))}
print('1_loc_count = ', oneloccount)
zeroloccount = {onezero[i]:zeroone[i]-onezero[i] for i in range(len(onezero))}
print('0_loc_count = ', zeroloccount)

maxone = sorted(oneloccount.values())
print(maxone)
maxzero = sorted(zeroloccount.values())
print(maxzero)
divide = maxone[-1]/2
print(divide)
dots = ''
for i in range(len(bits)):
    if i in oneloccount.keys():
        if oneloccount[i] > divide:
            dots = dots + '-'
        else:
            dots = dots + '.'
    elif i in zeroloccount.keys():
        if zeroloccount[i] > divide:
            dots = dots + ' '
        else:
            dots = dots + ''
print(dots)

def decode_morse(morse_code):
    morse_code = morse_code.strip()
    text = ''
    for x in morse_code.split(' '):
        if x != '':
            text = text + MORSE_CODE[x]
        else:
            text = text + ' '
    return text.replace('  ', ' ')

print(decode_morse(dots))