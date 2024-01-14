def remove_ith_char(s,pos):
    if pos == 0:
        return s[1:]
    
    return s[:pos-1] + s[pos:]

my_string = "GeeksForGeeks"
pos = 3
new_str = remove_ith_char(my_string,pos)
print(new_str)