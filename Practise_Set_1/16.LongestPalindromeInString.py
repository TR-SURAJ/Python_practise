#Longest palindrome string in a string
#ex: ababbdabab -> aba, malayalam -> malayalam

def longestPalindrome(s):
    if s == '':
        return None 
    max_len = 0
    max_pali = ""
    for first in range(0,len(s)):
        for second in range(first+1,len(s)+1):
            word = s[first:second]
            if word == word[::-1]:
                if max_len < len(word):
                    max_len = len(word)
                    max_pali = word 
    return max_pali