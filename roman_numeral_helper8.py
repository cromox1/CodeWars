pairs = [
    ('M', 1000),
    ('CM', 900), ('D', 500), ('C', 100),
    ('XC', 90), ('L', 50), ('X', 10),
    ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
]

class RomanNumerals(object):
    @staticmethod
    def to_roman(i):
        result = []
        for char, value in pairs:
            result.append(char * (i / value))
            i %= value
        return ''.join(result)
    @staticmethod
    def from_roman(s):
        d, result = dict(pairs), 0
        while s:
            try:
                result += d[s[:2]]
                s = s[2:]
            except KeyError:
                result += d[s[0]]
                s = s[1:]
        return result