class RomanNumerals:
    vals = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
           (1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1))
    values = [('M', 1000), ('CM', -200), ('D', 500), ('CD', -200),
          ('C', 100), ('XC', -20), ('L', 50), ('XL', -20),
          ('X', 10), ('IX', -2), ('V', 5), ('IV', -2),
          ('I', 1)]
    @classmethod
    def to_roman(self, n):
        if n == 0: return ""
        return next(c + RomanNumerals.to_roman(n-v) for c,v in RomanNumerals.vals if v <= n)
    @classmethod
    def from_roman(self, roman):
        return sum(roman.count(s)*v for s,v in RomanNumerals.values)
