def find_second_largest(nums):

    first = second = float('-inf')
    for n in nums:
        if n > first:
            second = first
            first = n 
        elif n > second and n < first:
            second = n 
    return second


nums = [10,5,8,20,15]
print(find_second_largest(nums))