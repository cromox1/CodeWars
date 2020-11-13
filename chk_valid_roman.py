decode = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL",
                       10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
def from_roman(roman):
    # roman = ''
    # numeral = 0
    try:
        if type(roman) == str:
            # print(roman, ' = ', end='')
            numeral = 0
            sort1 = []
            decode1 = {v: k for k, v in decode.items() if len(v) == 1}
            decode2 = {v: k for k, v in decode.items() if len(v) > 1}

            for xkey in decode2.keys():
                if xkey in roman:
                    numeral += decode2[xkey]
                    roman = roman.replace(xkey, '')
            for kkey in roman:
                numeral += decode1[kkey]
                sort1.append(decode1[kkey])

            # for xkey in decode2.keys():
            #     roman = roman.replace(xkey, '')
            #     # sort1 = [x for x in decode1[]]
            # for kkey in roman:
            #     # numeral += decode1[kkey]
            #     sort1 = sort1.append(decode1[kkey])
            sort2 = sorted(sort1, reverse=True)
            print('SORT1 = ', sort1)
            print('SORT2 = ', sort2)
            print('ROMAN = ', roman)

            return roman, numeral
    except:
        print('Not str -- ', roman)
        return 'not_string', 0

print(from_roman('MMVIII')[0])
print(from_roman('MMVIII')[1])
print(from_roman('VVMMVIIIX')[0])