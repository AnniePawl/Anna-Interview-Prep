#  Given an array of ints, return True if 6 appears in either first of last element in array.


def first_last6(nums):
    return (nums[0] == 6 or nums[-1] == 6)


print(first_last6([1, 3, 6]))  # True
print(first_last6([6, 3, 2]))  # True
print(first_last6([12, 6, 7]))  # False
