# Given an array or integers, return True is array contains 2 next to another 2


def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False

def has22_v2(nums):
    while 2 in nums:
        return nums[nums.index(2)+1 ] == 2



print(has22([1, 2, 2]))  # True
print(has22([2, 1, 2]))  # False
print(has22([2, 2, 1]))  # True


print(has22_v2([1, 2, 2]))  # True
print(has22_v2([2, 1, 2]))  # False
print(has22_v2([2, 2, 1]))  # True