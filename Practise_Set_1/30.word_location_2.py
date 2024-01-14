def word_location(full_string,search_string):
    words = full_string.split()
    
    for i, word in enumerate(words):
        if word == search_string:
            res = i + 1
            break 
        else:
            res = -1
            
    print(res)

full_string = 'geeksforgeeks is best for geeks'
search_string = 'best'
word_location(full_string,search_string)