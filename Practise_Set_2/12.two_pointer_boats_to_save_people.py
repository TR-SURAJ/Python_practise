#You are given an array people where people[i] is the weight of the ith person, 
#and an infinite number of boats where each boat can carry a maximum weight of limit. 
#Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

#Input: people = [1,2], limit = 3
#Output: 1
#Explanation: 1 boat (1, 2)

def numResueBoats(people: [], limit: int) -> int:
    people.sort()
    left = 0
    right = len(people) - 1
    count = 0

    while left <= right:
        if (people[left] + people[right]) <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        
        count += 1
    return count 

bo = numResueBoats([3,2,2,1],3)
print(bo)