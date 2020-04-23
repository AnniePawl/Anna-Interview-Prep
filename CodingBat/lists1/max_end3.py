# Given an array of ints len 3, figure out which num is largest between first and last. Set all elements to that value and return


def max_end3(nums):
    return [nums[0]]*3 if nums[0] >= nums[-1] else [nums[-1]]*3


print(max_end3([1, 2, 3]))  # [3,3,3]
print(max_end3([12, 29, 7]))  # [12,12,12]
print(max_end3([7, 2, 3]))  # [7,7,7]
