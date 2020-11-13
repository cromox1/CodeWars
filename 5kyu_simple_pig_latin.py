def pig_it(text):
    textit = ''
    for list in text.split(' '):
        if len(list) > 1 or list.isalpha():
            listit = [list[i - (len(list) - 1)] for i in range(len(list))]
            textit = textit + ''.join(listit) + 'ay '
        else:
            textit = textit + ''.join(list) + ' '
    return textit[:-1]

class Test:
    def assert_equals(value, expected):
        from nose.tools import assert_equal
        try:
            assert_equal(value, expected)
            print('EQUAL   --> v =', value, " ==  x =", expected)
        except:
            message = ' // # ' + str(value) + ' should == ' + str(expected)
            print('UNEQUAL!! --> v =', value, " !=  x =", expected, message)

    @classmethod
    def describe(cls, param):
        print(param)

## TEST
Test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
Test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')
Test.assert_equals(pig_it('Quis custodiet ipsos custodes ?'),'uisQay ustodietcay psosiay ustodescay ?')
Test.assert_equals(pig_it('O tempora o mores !'),'Oay emporatay oay oresmay !')

# You should 'pig' "Quis custodiet ipsos custodes ?": 'uisQay ustodietcay psosiay ustodescay ?ay' should equal 'uisQay ustodietcay psosiay ustodescay ?'
# You should 'pig' "O tempora o mores !": 'Oay emporatay oay oresmay !ay' should equal 'Oay emporatay oay oresmay !'