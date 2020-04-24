# Return "centered" average of array of ints, which we'll say is mean average, ignoring largest and smallest values in array. If multiple copies of largest or smallest, just ignore one.


def centered_average(nums):
    nums.sort()
    return int((sum(nums[1:-1]))/(len(nums)-2))


print(centered_average([1, 2, 3, 4, 100]))  # 3
print(centered_average([1, 1, 5, 5, 10, 8, 7]))  # 5
print(centered_average([-10, -4, -2, -4, -2, 0]))  # -3
