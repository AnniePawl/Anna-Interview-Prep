# Given an array in integers, return True is sequence of numbers 1,2,3 appears somewhere in the array


def array123(nums):
    # iterate w/ len-2 to use i+1 and i+2 in loop
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1] ==2 and nums[i+2] ==3:
            return True
    return False


def array123_v2(nums):
    for i in range(0, len(nums)-2):
        if [1,2,3] == nums[i:i+3]:
            return True
    return False


print(array123([1, 2, 3, 4]))  # True
print(array123([2, 3, 1, 2, 3]))  # True
print(array123([4, 3, 2, 1]))  # False

print(array123_v2([1, 2, 3, 4])) # True
print(array123_v2([2, 3, 1, 2, 3]))  # True
print(array123_v2([4, 3, 2, 1]))  # False

