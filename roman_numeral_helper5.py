"""TODO: create a RomanNumerals helper object"""
# in version 3.8
class RomanNumerals:
    @classmethod
    def to_roman(self,num):
        collotions = [('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]
        out = ''
        for key, value in collotions:
            while num >= value:
                out += key
                num -= value
        return out

    @classmethod
    def from_roman(self, roman):
        collotions = [('CM',900),('CD',400),('XC',90),('XL',40),('IX',9),('IV',4),('M',1000),('D',500),('C',100),('L',50),('X',10),('V',5),('I',1)]
        out = 0
        for key,value in collotions:
            out += value * roman.count(key)
            roman = roman.replace(key,'')
        return out