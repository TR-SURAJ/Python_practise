#Given an array of integers and target check if sum of and two elements in the array matches the target

def two_pointer_find_sum_match_target(arr: list(), target: int) -> bool:
    start,end = 0, len(arr) - 1

    while start < end:
        if(arr[start] + arr[end]) == target:
            return True 
        elif(arr[start] + arr[end]) > target:
            end -= 1
        else:
            start += 1
    return False



if __name__ == '__main__':
    arr = [1,3,5,7,9,11]
    target = 68
    print(two_pointer_find_sum_match_target(arr,target))