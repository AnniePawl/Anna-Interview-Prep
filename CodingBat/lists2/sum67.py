# Return sum of numbers in array, except ignore sections of numbers starting with 6 and extending to next 7. Every 6 will be followed by at least one 7


def sum67(nums):
    # Remove region between 6 and 7
    while 6 in nums:
        position6 = nums.index(6)
        position7 = nums[position6:].index(7) + position6
        del nums[position6:position7+1]
    return reduce(lambda x, y: x+y, nums, 0)


print(sum67([1, 2, 2]))  # 5
print(sum67([1, 2, 2, 6, 99, 99, 7]))  # 5
print(sum67([1, 1, 6, 7, 2]))  # 4
