def reverse_words_string(s):

    rs = s.split()[::-1]
    l = []

    for i in rs:
        l.append(i)

    print(" ".join(l))



my_string = "geeks quiz practice code"
reverse_words_string(my_string)