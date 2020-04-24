# Given an array or integers, return True is array contains 2 next to another 2


def has22(nums):
    for i in range(len(nums)):
        return nums[i] == 2 and nums[i+1] == 22


print(has22([1, 2, 2]))  # True
print(has22([2, 1, 2]))  # False
print(has22([2, 2, 1]))  # True
