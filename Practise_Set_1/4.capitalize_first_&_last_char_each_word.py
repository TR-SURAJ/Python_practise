def cap_upper_lower_char(s):
    s = s.split()
    ns = []
    for i in s:
        ns.append(i[0].upper() + i[1:-1] + i[-1].upper())

    return ' '.join(ns)


my_str = "hello world"
new_str = cap_upper_lower_char(my_str)
print(new_str)