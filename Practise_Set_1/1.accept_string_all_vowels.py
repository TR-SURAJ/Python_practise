def check_all_vowels(s):
    s = s.lower()
    vowels = set('aeiou')
    ns = set({})
    for i in s:
        if i in vowels:
            ns.add(i)
        else:
            pass 

    if len(ns) == len(vowels):
        print("Accepted")
    else:
        print("Not accepted")


my_str = "SEEquoiaL"
is_accept = check_all_vowels(my_str)