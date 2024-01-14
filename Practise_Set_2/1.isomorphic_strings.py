def isIso(str1, str2):
    if(len(str1) != len(str2)):
        return False 
    
    mapST, mapTS = {},{}
    for i in range(len(str1)):
        s1,s2 = str1[i],str2[i]
        if((s1 in mapST and mapST[s1] != s2) or (s2 in mapTS and mapTS[s2] != s1)):
            return False 
        mapST[s1] = s2
        mapTS[s2] = s1 
    return True


print(isIso('egg', 'add'))
print(isIso('foo', 'bar'))
print(isIso('paper', 'title'))