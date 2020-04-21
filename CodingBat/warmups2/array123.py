# Given an array in integers, return True is sequence of numbers 1,2,3 appears somewhere in the array


def array123(nums):
    target_sequence = [1, 2, 3]
    for i in range(len(nums)):
        subsequence = [i:i+3]
        if subsequence = target_sequence:
            return True


print(array123([1, 2, 3, 4]))  # True
print(array123([2, 3, 1, 2, 3]))  # True
print(array123([4, 3, 2, 1]))  # False
