def find_missing_number(nums):

    n = len(nums) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum

sequence = [1,2,3,5,6,7,8]
missing_number = find_missing_number(sequence)
print(missing_number)