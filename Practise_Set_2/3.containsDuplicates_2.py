def containsDuplicates(l):

    if(len(l) != len(set(l))):
        return True 
    return False

print(containsDuplicates([1,2,3,1]))
print(containsDuplicates([4,5,6,7,8]))