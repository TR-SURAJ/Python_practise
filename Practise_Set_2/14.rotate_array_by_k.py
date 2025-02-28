# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

#Input: nums = [1,2,3,4,5,6,7], k = 3
#Output: [5,6,7,1,2,3,4]

def roatate(nums, k):

    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]

    return nums


nums = [1,2,3,4,5,6,7]
k = 3
print(roatate(nums, 3))