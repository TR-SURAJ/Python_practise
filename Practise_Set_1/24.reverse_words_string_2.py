def reverse_words_string_2(s):
    ls = s.split()

    rs = ''
    for i in range(len(ls)-1,-1,-1):
        rs += ls[i] + ' '

    return rs

string = "geeks quiz practice code"
reversed_string = reverse_words_string_2(string)
print(reversed_string)