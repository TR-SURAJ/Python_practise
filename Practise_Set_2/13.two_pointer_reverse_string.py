#Reverses a string in-place by modifying the input array 's'.

def reverse_string(s):
    left,right = 0, len(s) - 1

    while left < right:
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1

    return s


s = ["h","e","l","l","o"]
print(reverse_string(s))