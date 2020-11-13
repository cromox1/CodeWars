class RomanNumerals():
    @staticmethod
    def to_roman(n):
        def generator(n):
            for v, c in ((1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')):
                while n >= v:
                    n -= v
                    yield c
        return ''.join(generator(n)).replace('IIII', 'IV').replace('DCCCC', 'CM').replace('LXXXX', 'XC')

    @staticmethod
    def from_roman(c, acc=0):
        if c == '':
            return acc
        if c[:2] == 'IV':
            return RomanNumerals.from_roman(c[2:], acc + 4)
        return RomanNumerals.from_roman(c[1:], acc + {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}[c[0]])