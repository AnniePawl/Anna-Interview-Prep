# Given an array length 2, return True if it contains a 2 or a 3


def has23(nums):
    return 2 in nums or 3 in nums

def has23_v2(nums):
    for num in nums:
        if num == 2 or num ==3:
            return True
    return False
    


print(has23([1, 4, 3]))  # True
print(has23([4, 4, 2]))  # True
print(has23([5, 4, 6]))  # False

print(has23_v2([1, 4, 3]))  # True
print(has23_v2([4, 4, 2]))  # True
print(has23_v2([5, 4, 6]))  # False
