#Given a sorted array and a target, return the index of the array whose sum is equal to target. Add the index by one and return.

def twoSum(numbers: list(), target:int) -> list():
    start,end = 0,len(numbers) - 1
    while start < end:
        if (numbers[start] + numbers[end]) == target:
            return [start+1,end+1]
        elif (numbers[start] + numbers[end]) > target:
            end -= 1
        else:
            start += 1
    
    return [-1,-1]



if __name__ == '__main__':    
    numbers = [2,7,11,15]
    target = 9
    outcome = twoSum(numbers,target)
    print(outcome)


