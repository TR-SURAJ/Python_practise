def word_location(full_string,search_string):

    l = full_string.split()
    idx = l.index(search_string) + 1
    print(idx)

full_string = 'geeksforgeeks is best for geeks'
search_string = 'best'
word_location(full_string,search_string)