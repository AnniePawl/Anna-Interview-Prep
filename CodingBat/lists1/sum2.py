# Given an array of ints, return sum of first 2 elements. If len < 2, just sum those elements. If len = 0 , return 0


def sum2(nums):
    return sum(nums[:2])


print(sum2([1, 2, 3]))  # 3
print(sum2([4, 6, 7]))  # 10
print(sum2([2]))  # 2
print(sum2([]))  # 0
