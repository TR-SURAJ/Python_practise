def all_substring_freq(s):

    temp = [s[idx:j] for idx in range(len(s)) for j in range(idx+1, len(s)+1)]
    d = {}

    for i in temp:
        d[i] = d.get(i,0) + 1

    return d

test_str = "abababa"
final_list = all_substring_freq(test_str)
print(final_list)

