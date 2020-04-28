#  Given an array of ints, return True if 6 appears in either first of last element in array.


def first_last6(nums):
    return (nums[0] == 6 or nums[-1] == 6)

def first_last6_v2(nums):
    return 6 in [nums[0],nums[-1]]

print(first_last6([1, 3, 6]))  # True
print(first_last6([6, 3, 2]))  # True
print(first_last6([12, 6, 7]))  # False

print(first_last6_v2([1, 3, 6]))  # True
print(first_last6_v2([6, 3, 2]))  # True
print(first_last6_v2([12, 6, 7]))  # False