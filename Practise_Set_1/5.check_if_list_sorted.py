def is_sorted(nums):
    return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))

numbers = [1,2,3,4,5]
print(is_sorted(numbers))