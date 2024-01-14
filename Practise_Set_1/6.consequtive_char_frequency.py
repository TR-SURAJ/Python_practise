def consecutive_char_freq(mystr):
    res = []
    count = 1
    
    for i in range(len(mystr)-1):
        if mystr[i] == mystr[i+1]:
            count += 1
        else:
            res.append(count)
            count = 1            
    print(res)

test_str = "geekksforgggeeks"
consecutive_char_freq(test_str)