def count_frequency(lst):

    freq = {}
    for i in lst:
        freq[i] = freq.get(i, 0) + 1

    return freq

elements = [1,2,2,3,3,3,4,4,4,4]
print(count_frequency(elements))