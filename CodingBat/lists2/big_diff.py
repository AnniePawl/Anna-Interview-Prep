# Given an array of 1 or more integers, return difference between largest and smalled values


def big_diff(nums):
    return max(nums) - min(nums)


print(big_diff([3, 5, 1, 9]))  # 8
print(big_diff([10, 3, 5, 6]))  # 7
