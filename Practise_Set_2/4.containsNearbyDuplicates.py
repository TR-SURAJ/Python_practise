def containsNearbyDuplicates(li,k):

    hset = {}

    for idx in range(len(li)):
        
        if li[idx] in hset and abs(idx - hset[li[idx]]) <= k:
            return True
        hset[li[idx]] = idx 
    return False



print(containsNearbyDuplicates([1,2,3,1],3))
