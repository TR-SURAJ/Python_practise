def count_matching_char(str1,str2):
    s1 = set(str1)
    s2 = set(str2)
    cnt = 0

    for i in s1:
        if i in s2:
            cnt+=1
    return cnt


str1 = 'aabcddekll12@'
str2 = 'bb22ll@55k'

count_matching = count_matching_char(str1,str2)
print(count_matching)