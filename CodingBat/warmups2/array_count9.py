# Gicen an array of integers, return number of 9s in array


def array_count9(nums):
    count = 0
    for i in range(len(nums)):
        if 9 in nums:
            count + 1
    return count


print(array_count9([9, 1, 1]))  # 1
print(array_count9([9, 3, 9, 2, 9, 1]))  # 3
