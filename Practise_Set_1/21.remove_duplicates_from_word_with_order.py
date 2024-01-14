def remove_dup_order(s):
    new_str = ""

    for i in s:
        if i in new_str:
            pass 
        else:
            new_str = new_str + i 

    return new_str


my_str = "geeksforgeeks"
final_str = remove_dup_order(my_str)
print(final_str)