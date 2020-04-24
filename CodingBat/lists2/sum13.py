# Return sum of numbers in array, returning 0 if empty, except number 13 and number that immediately follows 13


def sum13(nums):
    sum = 0
    position = 0
    while position < len(nums):
        if nums[position] == 13:
            position += 1
        else:
            sum += nums[position]
        position += 1
    return sum


print(sum13([1, 2, 3, 4]))  # 10
print(sum13([]))  # 0
print(sum13([1, 24, 13]))  # 25
print(sum13([5, 5, 13, 5]))  # 10
