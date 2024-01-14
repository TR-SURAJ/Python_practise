def least_frequent_char(s):
    s = s.lower()
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    print(d)
    res = min(d, key = d.get)
    return res

my_str = "GeeksforGeeks"
fs = least_frequent_char(my_str)
print(fs)