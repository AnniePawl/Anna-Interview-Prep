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

def sum13_v2(nums):
    while 13 in nums:
        if nums.index(13) < len(nums)-1:
            nums.pop(nums.index(13)+1)
        nums.pop(nums.index(13))
    return sum(nums)

# Does not account for index after 13... 
def sum13_v3(nums):
    return sum(num for num in nums if num != 13 )

# print(sum13([1, 2, 3, 4]))  # 10
# print(sum13([]))  # 0
# print(sum13([1, 24, 13]))  # 25
# print(sum13([5, 5, 13, 5]))  # 10

# print(sum13_v2([1, 2, 3, 4]))  # 10
# print(sum13_v2([]))  # 0
# print(sum13_v2([1, 24, 13]))  # 25
# print(sum13_v2([5, 5, 13, 5]))  # 10


print(sum13_v3([1, 2, 3, 4]))  # 10
print(sum13_v3([]))  # 0
print(sum13_v3([1, 24, 13]))  # 25
print(sum13_v3([5, 5, 13, 5]))  # 10