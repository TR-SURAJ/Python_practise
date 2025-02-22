def isPalindrome(s:str) -> bool:
    start,end = 0,len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False 
        start += 1
        end -= 1
    return True


if __name__ == '__main__':
    print(isPalindrome("ababa"))