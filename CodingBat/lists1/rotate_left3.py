# Given an array of ints length 3, return an array with elements rotated left so [1,2,3] -> [2,3,1]


def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]


print(rotate_left3([1, 2, 3]))  # [2,3,1]
print(rotate_left3([7, 6, 5]))  # [6,5,7]
print(rotate_left3([7, 0, 0]))  # [0,0,7]
