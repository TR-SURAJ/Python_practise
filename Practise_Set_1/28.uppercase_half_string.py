def upper_case_half(my_str):
    half_idx = len(my_str)//2

    return my_str[:half_idx] + my_str[half_idx:].upper()

my_str = 'geeksforgeek'
new_str = upper_case_half(my_str)
print(new_str)