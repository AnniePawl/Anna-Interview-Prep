# Given an array length 2, return True if it contains a 2 or a 3


def has23(nums):
    return 2 in nums or 3 in nums


print(has23([1, 4, 3]))  # True
print(has23([4, 4, 2]))  # True
print(has23([5, 4, 6]))  # False
