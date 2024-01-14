def find_uncommon_words(A,B):

    A = A.split()
    B = B.split()
    l = []
    for i in A:
        if i not in B:
            l.append(i)
    for j in B:
        if j not in A:
            l.append(j)

    return l

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
new_list = find_uncommon_words(A,B)
print(new_list)