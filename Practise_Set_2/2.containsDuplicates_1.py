def containsDuplicates(l):

    hashset = set()
    for i in l:
        if i in hashset:
            return True 
        hashset.add(i)
    return False

print(containsDuplicates([1,2,3,1]))
print(containsDuplicates([4,5,6,7,8]))