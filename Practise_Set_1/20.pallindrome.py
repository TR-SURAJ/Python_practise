def is_palindrome(input_str):
    return input_str == input_str[::-1]



word = "radar"
print(is_palindrome(word))