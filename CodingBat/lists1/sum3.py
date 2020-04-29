# Given an array of ints length 3, return sum of all elements


def sum3(nums):
    result = 0
    for num in nums:
        result += num
    return result

def sum3_v2(nums):
    return sum(nums)

print(sum3([1, 2, 3]))  # 6
print(sum3([2, 3, 4]))  # 9
print(sum3([3, 4, 5]))  # 12

print(sum3_v2([1, 2, 3]))  # 6
print(sum3_v2([2, 3, 4]))  # 9
print(sum3_v2([3, 4, 5]))  # 12
