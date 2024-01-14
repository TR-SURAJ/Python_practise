def odd_freq_chars(s):
    
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return [i for i,j in d.items() if j%2 != 0]

test_str = 'geekforgeeks'
odd_strs = odd_freq_chars(test_str)
print(odd_strs)