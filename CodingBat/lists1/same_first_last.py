# Given an array of ints, return True if array is length 1 or more, and the first element and the last element are equal.


def same_first_last(nums):
    if len(nums) >= 1:
        return (nums[0] == nums[-1])


print(same_first_last([1, 3, 4, 1]))  # True
print(same_first_last([3, 2, 4]))  # False
print(same_first_last([5, 3, 4, 5]))  # True
print(same_first_last([5]))  # True
