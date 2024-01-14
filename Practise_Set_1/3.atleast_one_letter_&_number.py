def checkstring(s):
    flag_l = False 
    flag_n = False 

    for i in s:

        if i.isalpha():
            flag_l = True 

        if i.isdigit():
            flag_n = True 

    return flag_n and flag_l

my_str = 'thishasboth29'
is_true = checkstring(my_str)
print(is_true)   