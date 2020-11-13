def word_sub(w):
    long_word = ""
    for word in w:
        temp_word = ''
        j = 0
        for letter in word:
            for i in range(j, len(w)):
                if letter == w[i]:
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

print(word_sub('abcd'))