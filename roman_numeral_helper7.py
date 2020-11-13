#we don't want to pollute namespace
def RomanNumerals():
  vals = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
    (1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1))
  class X: pass
  x = X()
  X.to_roman = lambda s,n: next(c + RomanNumerals.to_roman(n-v) for c,v in vals if v <= n) if n != 0 else ""
  X.from_roman = lambda s,roman: next(v + RomanNumerals.from_roman(roman[len(c):]) for c,v in vals if roman.startswith(c)) if roman != "" else 0
  return x
RomanNumerals = RomanNumerals()