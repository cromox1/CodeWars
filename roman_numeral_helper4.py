class RomanNumerals(object):
    table = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    def to_roman(integer):
        roman = ''
        table = RomanNumerals.table.copy()
        while integer:
            symbol, numeral = table.popitem()
            roman += (integer // numeral) * symbol
            integer %= numeral
        return roman

    def from_roman(roman):
        if len(roman) == 1:
            return RomanNumerals.table[roman]
        elif not roman:
            return 0
        else:
            first = RomanNumerals.table[roman[0]]
            second = RomanNumerals.table[roman[1]]

            if first >= second:
                return first + RomanNumerals.from_roman(roman[1:])
            else:
                return second - first + RomanNumerals.from_roman(roman[2:])