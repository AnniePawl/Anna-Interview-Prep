# Given an array on integers, return True if one of first 4 elements in the array is 9. The array might be less than 4.


def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4
    for i in range(end):
        if nums[i] == 9:
            return True
    return False


print(array_front9([1, 3, 9, 4, 3, 2]))  # True
print(array_front9([9, 2]))  # True
print(array_front9([1, 3, 5, 4, 3, 9]))  # False
