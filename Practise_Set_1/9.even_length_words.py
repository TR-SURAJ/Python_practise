def even_length_string(s):
    slist = s.split()
    even_list = []
    for i in slist:
        if(len(i)%2 == 0):
            even_list.append(i)
    even_str = ' '.join(even_list)
    return even_str

my_string = "This is a python language"
even_str = even_length_string(my_string)
print(even_str)
