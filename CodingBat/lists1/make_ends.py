# Given an array of ints, returnn new array len 2 containing fist and last elements from original array.


def make_ends(nums):
    return[nums[0], nums[-1]]


print(make_ends([1, 2, 3]))  # [1,3]
print(make_ends([6, 2, 7]))  # [6,7]
print(make_ends([1, 2, 3]))  # [1,3]
