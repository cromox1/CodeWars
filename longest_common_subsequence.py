from nose.tools import assert_equal

# def lcs(x, y):
#     '''TODO'''
#     # pass
#     # print([x1 for x1 in x], [y1 for y1 in y])
#     list1 = [x]
#     for i in range(len(x)):
#         list1.append(x.replace(x[i],''))
#     # print()
#     print(list1)
#     list2 = [y]
#     for i in range(len(y)):
#         list2.append(y.replace(y[i], ''))
#     # print()
#     print(list2)
#     return y

def lcs(s, d):
    long_word = ""
    for word in d:
        temp_word = ''
        j = 0
        for letter in word:
            for i in range(j, len(s)):
                if letter == s[i]:
                    temp_word += letter
                    j = i
                    break
                else:
                    continue

        if (temp_word) == word and len(long_word) < len(temp_word):
            long_word = temp_word
        else:
            continue
    return long_word

class test:
    def assert_equalx(seq1, seq2, seqx, message='unequal'):
        val1 = lcs(seq1, seq2)
        try:
            assert_equal(val1, seqx)
            print('EQUAL   --> v =', val1, " ==  x =", seqx)
        except:
            print('UNEQUAL!! --> v =', val1, " !=  x =", seqx, " // ", message)

# test.assert_equalx("a", "b", "")
# test.assert_equalx("abcdef", "abc", "abc")
test.assert_equalx("abcdef", "acf", "acf")
# test.assert_equalx("132535365" , "123456789", "12356")