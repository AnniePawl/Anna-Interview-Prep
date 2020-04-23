# Given an array of ints length 3, return sum of all elements


def sum3(nums):
    result = 0
    for num in nums:
        result += num
    return result


print(sum3([1, 2, 3]))  # 6
print(sum3([2, 3, 4]))  # 9
print(sum3([3, 4, 5]))  # 12
