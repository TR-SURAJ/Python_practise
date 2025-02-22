#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets.

def three_sum(nums:list()) -> list():
    nums.sort()
    n = len(nums)
    answer = []
    
    for i in range(n):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue

        lo,hi = i+1,n-1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum == 0:
                answer.append([nums[i],nums[lo],nums[hi]])
                lo,hi = lo+1,hi-1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi+1]:
                    hi -= 1
            elif sum < 0:
                lo += 1
            else:
                hi -= 1
    return answer



nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))